# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad

import addonHandler
import gui
import wx

# Initialize translation
addonHandler.initTranslation()

# Translators: Message shown after the add-on is installed.
INSTALL_MESSAGE = _(
	"Thank you for installing Accessible Bluetooth Audio Receiver! "
	"We hope this add-on makes your experience smoother.\n\n"
	"Remember, your creativity has no limits. Keep creating and innovating!\n\n"
	"Best regards,\n"
	"Muhammad",
)

# Translators: The title for the add-on installation message.
INSTALL_MESSAGE_TITLE = _("Accessible Bluetooth Audio Receiver")


def onInstall() -> None:
	"""Show a welcome message after installation."""
	gui.messageBox(
		INSTALL_MESSAGE,
		INSTALL_MESSAGE_TITLE,
		wx.OK | wx.ICON_INFORMATION,
	)
