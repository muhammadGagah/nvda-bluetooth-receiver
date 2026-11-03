# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad
# addon/appModules/bluetoothaudioreceiver.py

import re
import unicodedata
from typing import Any

import addonHandler
import appModuleHandler
import controlTypes
import scriptHandler
import ui
import wx
from logHandler import log
from NVDAObjects import NVDAObject

# Initialize translation
addonHandler.initTranslation()

# Constants for connection monitoring
MONITOR_INTERVAL_MS = 500
MONITOR_MAX_ATTEMPTS = 20  # Approx 10 seconds
DEVICE_STATUS_PATTERN = re.compile(r"^\[(?P<deviceName>.*?)\]\s*(?P<status>.*)$")


def _parseDeviceStatus(text: str) -> tuple[str, str]:
	match = DEVICE_STATUS_PATTERN.match(text)
	if not match:
		return text, text
	return match.group("deviceName"), match.group("status")


def _isConnectedStatus(statusText: str) -> bool | None:
	"""Return connection state, or None when the localized status is unknown."""
	status = "".join(
		character
		for character in unicodedata.normalize("NFKD", statusText.casefold())
		if not unicodedata.combining(character)
	)
	# ponytail: localized text heuristic; replace with a stable UIA state if the app exposes one.
	disconnectedTokens = (
		"disconnected",
		"not connected",
		"terputus",
		"tidak terhubung",
		"tidak tersambung",
		"getrennt",
		"nicht verbunden",
		"deconnecte",
	)
	if any(token in status for token in disconnectedTokens):
		return False
	connectedTokens = ("connected", "terhubung", "tersambung", "verbunden", "connecte")
	if any(token in status for token in connectedTokens):
		return True
	return None


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
		text = self._getStatusText()
		if text:
			deviceName, statusText = _parseDeviceStatus(text)
			if (deviceName, statusText) != (text, text):
				# Translators: The format for reporting a bluetooth device.
				# {0} is the device name. {1} is the status (e.g. Paired, Connected).
				return _("Device name: {0}, Status: {1}").format(
					deviceName,
					statusText,
				)
			return text
		return super().name

	def _getStatusText(self) -> str | None:
		try:
			return self.parent.previous.name
		except AttributeError:
			return None

	def _getToggleButton(self, isConnected: bool) -> NVDAObject | None:
		try:
			connectButton = self.parent.next
			if not isConnected:
				return connectButton
			return connectButton.next
		except AttributeError:
			return None

	def _monitorConnection(self, deviceName: str, targetConnected: bool, attempt: int = 0) -> None:
		try:
			currentText = self._getStatusText()
			if not currentText:
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
				return

			statusText = _parseDeviceStatus(currentText)[1]
			isConnected = _isConnectedStatus(statusText)
			if isConnected is None:
				if attempt < MONITOR_MAX_ATTEMPTS:
					wx.CallLater(
						MONITOR_INTERVAL_MS,
						self._monitorConnection,
						deviceName,
						targetConnected,
						attempt + 1,
					)
				else:
					ui.message(_("Connection status change timed out for {}").format(deviceName))
				return

			# Check if we reached the desired state
			if (targetConnected and isConnected) or (not targetConnected and not isConnected):
				statusMsg = (
					# Translators: Message when successfully connected to a device.
					_("successfully connected with {}")
					if targetConnected
					# Translators: Message when successfully disconnected from a device.
					else _("successfully disconnected from {}")
				)
				ui.message(statusMsg.format(deviceName))
				wx.CallAfter(self._restoreFocus)
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
				wx.CallAfter(self._restoreFocus)
		except Exception:
			log.debugWarning("Error while monitoring Bluetooth connection status", exc_info=True)

	def _restoreFocus(self) -> None:
		"""Return focus to the device row after the app refreshes its controls."""
		try:
			self.setFocus()
		except Exception:
			log.debugWarning("Unable to restore focus to Bluetooth device row", exc_info=True)

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
			rawText = self._getStatusText()
			if not rawText:
				gesture.send()
				return

			deviceName, statusText = _parseDeviceStatus(rawText)
			if (deviceName, statusText) == (rawText, rawText):
				gesture.send()
				return
			isConnected = _isConnectedStatus(statusText)
			if isConnected is None:
				gesture.send()
				return

			# 2. Determine Action
			if isConnected:
				# Disconnect Logic
				# Verify UI structure for Disconnect button
				targetButton = self._getToggleButton(isConnected=True)
				if not targetButton:
					# Translators: Error when disconnect button is not found.
					ui.message(_("Disconnect button not found"))
					gesture.send()
					return

				# Translators: Message when starting disconnection.
				ui.message(_("Disconnecting from {}...").format(deviceName))
				targetButton.doAction()
				wx.CallAfter(self._restoreFocus)

				# 3. Monitor for Disconnection
				wx.CallLater(
					MONITOR_INTERVAL_MS,
					self._monitorConnection,
					deviceName,
					False,
				)

			else:
				# Connect Logic
				# Verify UI structure for Connect button
				targetButton = self._getToggleButton(isConnected=False)
				if not targetButton:
					# Translators: Error when connect button is not found.
					ui.message(_("Connect button not found"))
					gesture.send()
					return

				# Translators: Message when starting connection.
				ui.message(_("Connecting to {}...").format(deviceName))
				targetButton.doAction()
				wx.CallAfter(self._restoreFocus)

				# 3. Monitor for Connection
				wx.CallLater(
					MONITOR_INTERVAL_MS,
					self._monitorConnection,
					deviceName,
					True,
				)

		except Exception as e:
			log.error(f"Failed to toggle connection: {e}")
			ui.message(_("Failed to toggle connection."))


class AppModule(appModuleHandler.AppModule):
	# Translators: The category for scripts in this app module.
	scriptCategory = _("Bluetooth Audio Receiver")

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[Any]) -> None:
		"""
		Inject the overlay only for rows that expose the expected device status.
		"""
		if obj.role == controlTypes.Role.LISTITEM:
			try:
				rawText = obj.parent.previous.name
				if rawText and _parseDeviceStatus(rawText) != (rawText, rawText):
					clsList.insert(0, BluetoothListItem)
			except AttributeError:
				pass
