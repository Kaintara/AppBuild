[app]
# (str) Title of your application
title = GuessTheLiar

# (str) Package name
package.name = guessliar

# (str) Package domain (needed for android/ios packaging)
package.domain = org.guesstheliar.app

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,ttf,png,jpg,mp3,json,txt

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip

# (str) Icon of the application
icon.filename = icon.png

# (list) Supported orientations
orientation = portrait

# (int) Target Android API
android.api = 30

# (int) Minimum API your APK supports
android.minapi = 21

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Use --private data storage (True) or public storage (False)
android.private_storage = True

# (str) Android SDK/NDK paths
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/27.0.12077973

# (bool) Skip SDK/NDK updates (we preinstalled them)
android.skip_update = True

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (str) Format used to package the app for debug
android.debug_artifact = apk

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
