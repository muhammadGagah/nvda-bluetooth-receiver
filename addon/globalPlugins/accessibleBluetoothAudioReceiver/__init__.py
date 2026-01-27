# -*- coding: utf-8 -*-
# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad
# addon/globalPlugins/accessibleBluetoothAudioReceiver/__init__.py

import os
import time
from typing import Any

import addonHandler
import appModuleHandler
import globalPluginHandler
import scriptHandler
import ui
import winUser
from logHandler import log

# Initialize translation
addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The category for scripts in this global plugin.
	scriptCategory = _("Bluetooth Audio Receiver")

	def __init__(self, *args, **kwargs) -> None:
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		# Explicitly map the app name to our app module.
		try:
			appModuleHandler.registerExecutableWithAppModule(
				"Bluetooth Audio Receiver.exe", "bluetoothaudioreceiver"
			)
			appModuleHandler.registerExecutableWithAppModule(
				"Bluetooth Audio Reveicer.exe", "bluetoothaudioreceiver"
			)
			# Register simplified names if needed
			appModuleHandler.registerExecutableWithAppModule(
				"bluetooth audio reveicer", "bluetoothaudioreceiver"
			)
		except Exception as e:
			log.debugWarning(f"Error registering app module mappings: {e}")

	@scriptHandler.script(
		# Translators: Description for the launch script.
		description=_("Launches Bluetooth Audio Receiver"), 
		gesture="kb:NVDA+windows+b"
	)
	def script_launchApp(self, gesture: Any) -> None:
		"""
		Starts the Bluetooth Audio Receiver application.
		Checks if it is already running to avoid multiple instances.
		"""
		shouldLaunch = True

		# 1. Attempt to check if already running using winUser
		try:
			# Check for ApplicationFrameWindow (UWP wrapper) with title
			hwnd = winUser.FindWindow(
				"ApplicationFrameWindow", "Bluetooth Audio Receiver"
			)
			if not hwnd:
				# Check for direct window
				hwnd = winUser.FindWindow(None, "Bluetooth Audio Receiver")

			if hwnd and winUser.isWindowVisible(hwnd):
				# Translators: Message displayed when the application is already running.
				ui.message(_("Bluetooth Audio Receiver is already running."))
				shouldLaunch = False
		except Exception as e:
			log.debugWarning(f"Error checking window status: {e}")

		# 2. Launch Application if not already running
		if shouldLaunch:
			try:
				# Translators: Message launching the application.
				ui.message(_("Launching Bluetooth Audio Receiver"))
				time.sleep(0.2)

				# Using the AUMID provided. 
				launchCmd = r"start shell:AppsFolder\55746MarkSmirnov.BluetoothAudioReveicer_xwrbx6997tsfc!App"
				os.system(launchCmd)
			except Exception as e:
				log.error(f"Failed to launch application: {e}")
				# Translators: Error message when launch fails.
				ui.message(_("Failed to launch: {}").format(e))
