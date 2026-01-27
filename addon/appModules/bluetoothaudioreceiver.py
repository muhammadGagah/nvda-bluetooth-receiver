# -*- coding: utf-8 -*-
# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad
# addon/appModules/bluetoothaudioreceiver.py

import re
from typing import Any
import wx

import addonHandler
import appModuleHandler
import controlTypes
import scriptHandler
import ui
from NVDAObjects import NVDAObject
from logHandler import log

# Initialize translation
addonHandler.initTranslation()

# Constants for connection monitoring
MONITOR_INTERVAL_MS = 500
MONITOR_MAX_ATTEMPTS = 20  # Approx 10 seconds


class BluetoothListItem(NVDAObject):
	"""
	Overlay class for Bluetooth device list items.
	Provides enhanced name reporting and connection toggling.
	"""

	@property
	def name(self) -> str:
		"""
		Returns the friendly name of the device, parsing the status if relevant.
		"""
		try:
			text = self.parent.previous.name
			match = re.match(r"^\[(.*?)\]\s*(.*)$", text)
			if match:
				# Translators: The format for reporting a bluetooth device.
				# {0} is the device name. {1} is the status (e.g. Paired, Connected).
				return _("Device name: {0}, Status: {1}").format(
					match.group(1), match.group(2)
				)
			return text
		except Exception:
			# Fallback to default name if traversal fails
			return super().name

	def _monitorConnection(self, deviceName: str, targetConnected: bool, attempt: int = 0) -> None:
		try:
			# Re-fetch status from the UI
			if not self.parent or not self.parent.previous:
				# UI might have changed, stop monitoring
				return

			currentText = self.parent.previous.name
			isConnected = "Connected" in currentText

			# Check if we reached the desired state
			if (targetConnected and isConnected) or (
				not targetConnected and not isConnected
			):
				statusMsg = (
					# Translators: Message when successfully connected to a device.
					_("successfully connected with {}")
					if targetConnected
					# Translators: Message when successfully disconnected from a device.
					else _("successfully disconnected from {}")
				)
				ui.message(statusMsg.format(deviceName))
				return

			if attempt < MONITOR_MAX_ATTEMPTS:
				wx.CallLater(
					MONITOR_INTERVAL_MS,
					self._monitorConnection,
					deviceName,
					targetConnected,
					attempt + 1,
				)
			else:
				# Translators: Error message when connection status change times out.
				ui.message(_("Connection status change timed out for {}").format(deviceName))
		except Exception as e:
			log.debugWarning(f"Error in _monitorConnection: {e}")
			pass

	@scriptHandler.script(
		# Translators: Description for the toggle connection script.
		description=_("Connects or disconnects from the selected device."),
		gesture="kb:enter",
	)
	def script_toggleConnection(self, gesture: Any) -> None:
		"""
		Toggles the connection state of the selected bluetooth device.
		"""
		try:
			# 1. Get Status and Name
			if not self.parent or not self.parent.previous:
				return

			infoObj = self.parent.previous
			rawText = infoObj.name

			match = re.match(r"^\[(.*?)\]\s*(.*)$", rawText)
			deviceName = match.group(1) if match else rawText
			statusText = match.group(2) if match else rawText

			isConnected = "Connected" in statusText

			# 2. Determine Action
			if isConnected:
				# Disconnect Logic
				# Verify UI structure for Disconnect button
				targetButton = self.parent.next.next
				if not targetButton:
					# Translators: Error when disconnect button is not found.
					ui.message(_("Disconnect button not found"))
					return

				# Translators: Message when starting disconnection.
				ui.message(_("Disconnecting from {}...").format(deviceName))
				targetButton.doAction()

				# 3. Monitor for Disconnection
				wx.CallLater(
					MONITOR_INTERVAL_MS, self._monitorConnection, deviceName, False
				)

			else:
				# Connect Logic
				# Verify UI structure for Connect button
				targetButton = self.parent.next
				if not targetButton:
					# Translators: Error when connect button is not found.
					ui.message(_("Connect button not found"))
					return

				# Translators: Message when starting connection.
				ui.message(_("Connecting to {}...").format(deviceName))
				targetButton.doAction()

				# 3. Monitor for Connection
				wx.CallLater(
					MONITOR_INTERVAL_MS, self._monitorConnection, deviceName, True
				)

		except Exception as e:
			log.error(f"Failed to toggle connection: {e}")
			ui.message(_("Failed to toggle connection."))

class AppModule(appModuleHandler.AppModule):
	# Translators: The category for scripts in this app module.
	scriptCategory = _("Bluetooth Audio Receiver")

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[Any]) -> None:
		"""
		Injects the BluetoothListItem overlay for list items.
		"""
		if obj.role == controlTypes.Role.LISTITEM:
			clsList.insert(0, BluetoothListItem)
