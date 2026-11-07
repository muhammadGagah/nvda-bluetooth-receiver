# Version 1.3.1

## Compatibility

- Tested with NVDA 2026.3. The minimum supported NVDA version remains 2024.1.

## Fixes

- Fixed device rows that could fail to load in NVDA when the app refreshed its list while NVDA was reading it. Errors from the app's controls are now handled instead of only missing-attribute errors.
- Connection monitoring now keeps waiting when the device status cannot be read for a moment, and reports a timeout instead of stopping silently.
- Focus now returns to the device row after every timeout, not only after some of them.
- The launch command (NVDA+Windows+B) now restores the Bluetooth Audio Receiver window when it is minimized before bringing it to the front.

# Version 1.3.0

## Compatibility

- Updated and tested the add-on metadata for NVDA 2026.2.
- Kept the minimum supported NVDA version at 2024.1.
- Updated the build templates and manifest metadata for current NVDA add-on requirements.

## Bluetooth Behavior

- Improved recognition of localized connected and disconnected status text.
- Added safe handling for unknown and transitional connection states instead of assuming a device is disconnected.
- Added retry and timeout reporting while waiting for a connection-state change.
- Limited the custom Enter action to rows that expose a valid Bluetooth device status.
- Preserved the application's native Enter behavior for unsupported or non-device rows.
- Restored focus to the selected device row after connecting, disconnecting, or timing out.

## Application and Accessibility

- Brought an existing Bluetooth Audio Receiver window to the foreground instead of opening another instance.
- Improved reporting of device names and connection status.
- Added safer fallbacks when expected Connect or Disconnect controls cannot be found.

## Build and Packaging

- Removed `__pycache__`, `.pyc`, and `.pyo` files from release packages.
- Removed the invalid `updateChannel = "None"` manifest entry when no update channel is configured.
- Included source URL and license metadata in the generated manifest.
- Fixed the add-on build helper source-suffix configuration.
- Updated documentation and version badges for version 1.3.0.
