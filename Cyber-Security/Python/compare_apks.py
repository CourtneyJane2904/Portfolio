#!/usr/bin/python3

# https://androguard.readthedocs.io/en/latest/api/androguard.core.bytecodes.html
import androguard.core.bytecodes.dvm as dvm
# https://pypi.org/project/google-play-scraper/
# shortens grabbing the version from the play store but this can be done manually too!
from google_play_scraper import app

# Extract package name from AndroidManifest.xml of apk
try:	a = dvm.APK("questnative.apk")
except:	print("Invalid apk file given.") ; exit(1)
android_manifest = a.xml["AndroidManifest.xml"]
pkg_name = android_manifest.get("package")

# Gather the Google Play version of the apk using the app func from google_play_scraper
store_v = app(pkg_name)["version"]
# grab version of local apk from AndroidManifest.xml
local_v = android_manifest.get("{http://schemas.android.com/apk/res/android}versionName")

# Report if the store version of the apk is different to the local version and deal with accordingly
if local_v != store_v: print(f"Local version {local_v} of the apk doesn't match Play Store version {store_v}. Continue with local or download Playstore version?")
else:	print(f'Local version {local_v} matches Play Store version {store_v}, is good to test.')

exit(0)
