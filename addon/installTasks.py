# -*- coding: utf-8 -*-
# Accessible Bluetooth Audio Receiver for NVDA
# Copyright (C) 2026 Muhammad

import gui
import wx


def onInstall():
	gui.messageBox(
		"Thank you for installing Accessible Bluetooth Audio Receiver! We hope this add-on makes your experience smoother.\n\nRemember, your creativity has no limits. Keep creating and innovating!\n\nBest regards,\nMuhammad",
		"Accessible Bluetooth Audio Receiver",
		wx.OK | wx.ICON_INFORMATION,
	)
