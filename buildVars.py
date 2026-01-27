from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
	addon_name="accessibleBluetoothAudioReceiver",
	addon_summary=_("Accessible Bluetooth Audio Receiver"),
	addon_description=_("""Effortlessly stream audio from your phone to your PC!
	This add-on supercharges the Bluetooth Audio Receiver app with global hotkeys and smart connection toggling.
	No more menu diving, just press one key to connect or disconnect.
	Experience seamless audio control like never before. Check the readme for more details!"""),
	addon_version="1.1",
	addon_changelog=_("""Initial Release."""),
	addon_author="Muhammad <muha.aku@gmail.com>",
	addon_url="",
	addon_sourceURL="",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2024.1",
	addon_lastTestedNVDAVersion="2025.3.2",
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
