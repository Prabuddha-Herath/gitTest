[app]
# (str) Title of your application
title = Medical Reminder App

# (str) Package name
package.name = medicalreminder

# (str) Package domain (reverse domain notation)
package.domain = org.test

# (str) Source code where main.py is located
source.dir = .

# (str) List of file extensions to include
source.include_exts = py,kv,wav,mp3

# (str) Application version
version = 0.1

# (list) Requirements (Python modules)
requirements = python3,kivy,plyer

# (str) Orientation
orientation = portrait

# (int) Fullscreen mode
fullscreen = 0

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# Android API/NDK/SDK versions
android.api = 33
android.ndk = 25b
android.sdk = 30

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the app (optional)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# (int) Log level (0 = errors only, 2 = info)
log_level = 2

# Warn when running as root
warn_on_root = 1

# (str) Location to store build files (optional)
# build_dir = ./build

# (int) Number of processes for compilation
# android.archs = arm64-v8a, armeabi-v7a
