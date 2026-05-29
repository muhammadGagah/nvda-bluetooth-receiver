# -*- coding: utf-8 -*-
# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad
# addon/globalPlugins/accessibleBluetoothAudioReceiver/__init__.py

import os
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

APP_MODULE_NAME = "bluetoothaudioreceiver"
APP_WINDOW_TITLE = "Bluetooth Audio Receiver"
APP_SHELL_URI = r"shell:AppsFolder\55746MarkSmirnov.BluetoothAudioReveicer_xwrbx6997tsfc!App"
APP_EXECUTABLE_ALIASES = (
	"bluetooth audio receiver",
	"bluetooth audio reveicer",
)


def _isAppWindowVisible() -> bool:
	hwnd = winUser.FindWindow(
		"ApplicationFrameWindow",
		APP_WINDOW_TITLE,
	)
	if not hwnd:
		hwnd = winUser.FindWindow(None, APP_WINDOW_TITLE)
	return bool(hwnd and winUser.isWindowVisible(hwnd))


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The category for scripts in this global plugin.
	scriptCategory = _("Bluetooth Audio Receiver")

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self._registeredExecutableAliases: list[str] = []
		for executableName in APP_EXECUTABLE_ALIASES:
			try:
				appModuleHandler.registerExecutableWithAppModule(executableName, APP_MODULE_NAME)
				self._registeredExecutableAliases.append(executableName)
			except Exception:
				log.debugWarning(
					f"Error registering app module mapping for {executableName!r}",
					exc_info=True,
				)

	def terminate(self) -> None:
		for executableName in self._registeredExecutableAliases:
			try:
				appModuleHandler.unregisterExecutable(executableName)
			except Exception:
				log.debugWarning(
					f"Error unregistering app module mapping for {executableName!r}",
					exc_info=True,
				)
		super().terminate()

	@scriptHandler.script(
		# Translators: Description for the launch script.
		description=_("Launches Bluetooth Audio Receiver"),
		gesture="kb:NVDA+windows+b",
	)
	def script_launchApp(self, gesture: Any) -> None:
		"""
		Starts the Bluetooth Audio Receiver application.
		Checks if it is already running to avoid multiple instances.
		"""
		try:
			if _isAppWindowVisible():
				# Translators: Message displayed when the application is already running.
				ui.message(_("Bluetooth Audio Receiver is already running."))
				return
		except Exception:
			log.debugWarning("Error checking Bluetooth Audio Receiver window status", exc_info=True)

		try:
			# Translators: Message launching the application.
			ui.message(_("Launching Bluetooth Audio Receiver"))
			os.startfile(APP_SHELL_URI)
		except Exception as e:
			log.error(f"Failed to launch application: {e}")
			# Translators: Error message when launch fails.
			ui.message(_("Failed to launch: {}").format(e))
