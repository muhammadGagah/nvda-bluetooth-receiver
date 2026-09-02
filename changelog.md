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
