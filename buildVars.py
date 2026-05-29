from site_scons.site_tools.NVDATool.typings import (
	AddonInfo,
	BrailleTables,
	SpeechDictionaries,
	SymbolDictionaries,
)
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="accessibleBluetoothAudioReceiver",
	addon_summary=_("Accessible Bluetooth Audio Receiver"),
	addon_description=_("""Effortlessly stream audio from your phone to your PC!
	This add-on supercharges the Bluetooth Audio Receiver app with global hotkeys and smart connection toggling.
	No more menu diving, just press one key to connect or disconnect.
	Experience seamless audio control like never before. Check the readme for more details!"""),
	addon_version="1.2.0",
	addon_changelog=_("Updated NVDA 2026.1 compatibility, Python 3.13 tooling, and uv-based packaging."),
	addon_author="Muhammad <muha.aku@gmail.com>",
	addon_url="https://github.com/muhammadGagah/nvda-bluetooth-receiver",
	addon_sourceURL="https://github.com/muhammadGagah/nvda-bluetooth-receiver",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2024.1",
	addon_lastTestedNVDAVersion="2026.1.1",
	addon_updateChannel=None,
	addon_license="GPL-2.0",
	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

pythonSources: list[str] = ["addon/**/*.py"]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}

symbolDictionaries: SymbolDictionaries = {}

speechDictionaries: SpeechDictionaries = {}
