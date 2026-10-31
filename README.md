# Cadence – Study & Rest Timer (Android)

The web app lives in `www/index.html`. Capacitor wraps it as an Android app.
GitHub Actions builds the APK for you; the `android/` folder is generated during the build, so it is not stored in the repo.

## Get your APK
1. Create a new GitHub repository and upload everything in this folder (keep the `.github` folder).
2. Open the **Actions** tab. The build runs on every push; you can also run **Build Android APK** manually.
3. When it finishes (about 5–8 minutes), open the run and download **cadence-debug-apk** from *Artifacts*. Unzip it to get `app-debug.apk`.
4. Copy the APK to your phone, open it, and allow “install unknown apps” if asked.

## First launch on the phone
- Allow notifications when asked.
- On Android 12 and later, allow **Alarms & reminders** for Cadence when prompted. Without it, alerts can arrive late with the screen off.
- For the most reliable alerts, set battery usage for Cadence to **Unrestricted**.

## How alerts work
When you press Start, the app schedules the upcoming phase endings as Android notifications (about 20 study/rest cycles ahead), so they fire even if the app is in the background or the screen is locked. Reopening the app refreshes the schedule. Notification sounds follow your phone’s default; custom sounds play only while the app is open.

## Changing things
- App name / id: `capacitor.config.json` (`appName`, `appId`).
- Icon: replace the three PNGs in `assets/` (1024×1024) and push.
- Status bar and camera cutout: the app draws edge to edge; `scripts/patch-android.py` applies the window setting during the build.
- Edit the app: change `www/index.html` and push; a new APK is built.
- Debug APKs are fine for personal use. For Google Play you need a signed release build (AAB), which is a separate step.
