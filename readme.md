# Accessible Bluetooth Audio Receiver

![Add-on Version](https://img.shields.io/badge/Version-1.1-blue)
![NVDA Compatible](https://img.shields.io/badge/NVDA-Compatible-green)

**Accessible Bluetooth Audio Receiver** is an add-on for the NVDA screen reader designed to improve the accessibility and usability of the [Bluetooth Audio Receiver](https://apps.microsoft.com/detail/9N9WCLWDQS5J?hl=en&gl=US&ocid=pdpshare) application on Windows.

This application allows you to stream music from your Bluetooth devices (like phones) to your PC speakers. This add-on makes it easier to launch the app and manage connections without navigating through complex UI elements.

## Features

- **Quick Launch Shortcut**: Open the application instantly from anywhere using a global hotkey.
- **Simplified Connection Toggling**: Connect or disconnect from a device simply by pressing `Enter` on the device in the list. The add-on handles finding and clicking the correct button for you.
- **Smart Status Reporting**: Automatically announces connection status changes (e.g., "successfully connected with [Device Name]").
- **Enhanced List Items**: Provides clear reporting of device names and their current status (Connected/Paired) when navigating the list.

## Prerequisites

1. **Windows 10 version 2004** or later (Required for Bluetooth A2DP Sink support).
2. A Bluetooth adapter (dongle or built-in).
3. The **Bluetooth Audio Receiver** application installed from the Microsoft Store.

   [**Download Bluetooth Audio Receiver**](https://apps.microsoft.com/detail/9N9WCLWDQS5J?hl=en&gl=US&ocid=pdpshare)

## Installation

1. Install the "Bluetooth Audio Receiver" app from the Microsoft Store link above.
2. Download the latest release of this NVDA add-on.
3. Open the `.nvda-addon` file and follow the prompts to install it in NVDA.
4. Restart NVDA when prompted.

## Usage

### Shortcuts

- **NVDA + Windows + B**: Launch the Bluetooth Audio Receiver application. If the app is already running, it will bring it to focus or notify you.

*Note: You can customize these shortcuts in NVDA via **Preferences** > **Input gestures...** > **Bluetooth Audio Receiver** category.*

### Managing Connections

1. Open the application using the shortcut (`NVDA + Windows + B`).
2. Navigate to the list of paired Bluetooth devices.
3. Select the device you want to use.
4. Press **Enter** on the device item:
   - If the device is **disconnected**, the add-on will attempt to **connect**.
   - If the device is **connected**, the add-on will attempt to **disconnect**.
5. The add-on will announce the progress ("Connecting to...", "Disconnecting from...") and the final result ("Successfully connected...").

*Note: You do not need to hunt for the "Open Connection" or "Close Connection" buttons; the `Enter` key handles this automatically.*

## Troubleshooting

- **"Bluetooth Audio Receiver is already running"**: The add-on prevents opening multiple instances. Check your taskbar or press Alt+Tab to find the open window.
- **Connection Timed Out**: If the device fails to connect, ensure your Bluetooth device (phone/tablet) is paired with Windows and is currently discoverable or trying to connect.

## Credits

Developed by Muhammad.

## License

This add-on is distributed under the GNU General Public License v2 (GPLv2).
