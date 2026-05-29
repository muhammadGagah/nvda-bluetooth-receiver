v1.2.0

Compatibility
- Updated add-on metadata for NVDA 2026.1.1 while keeping the minimum supported NVDA version at 2024.1.
- Confirmed the add-on does not directly use the NVDA 2026.1 APIs that were removed or changed.
- Kept the add-on runtime dependency-free: it still uses NVDA APIs, Python standard library modules, and wx/NVDA-provided components only.

Build and packaging
- Synced the add-on build layout with the current nvaccess/AddonTemplate workflow.
- Added `pyproject.toml` project metadata and `uv.lock` so build, lint, type checking, and packaging dependencies are resolved with `uv`.
- Updated CI to use `astral-sh/setup-uv`, `uv sync`, `uv run pre-commit`, `uv run scons`, and `uv run scons pot`.
- Updated the add-on build helpers to support the newer template `speechDictionaries` configuration.
- Updated manifest generation so optional values such as `updateChannel = None` are omitted from the generated manifest.
- Included source and license metadata in the generated manifest: `sourceURL`, `license`, and `licenseURL`.

Runtime changes
- Registered Bluetooth Audio Receiver app module aliases using normalized executable names.
- Added cleanup so app module aliases are unregistered when the global plugin is unloaded.
- Replaced the old shell launch command with `os.startfile` for the Microsoft Store app URI.
- Removed the blocking launch delay.
- Centralized Bluetooth device status parsing and reduced silent broad exception handling in the app module.

Localization and documentation
- Updated Indonesian translation strings for the new install message and add-on changelog.
- Updated the README version badge to 1.2.0.

v1.1
- Initial release.
