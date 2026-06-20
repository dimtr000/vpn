[app]
title = PremiumVPN
package.name = premiumvpn
package.domain = org.cyber.vpn
source.include_exts = py,kv,png
version = 1.0
requirements = python3,kivy,kivymd,plyer,pyjnius

android.permissions = CAMERA, INTERNET, VIBRATE, BIND_VPN_SERVICE, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
