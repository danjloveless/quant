# Mobile App Build Instructions

## Prerequisites

### iOS Development
- macOS with Xcode 14+
- Apple Developer Account
- CocoaPods installed

### Android Development  
- Android Studio
- Android SDK
- Java JDK 11+

## Building the iOS App

1. **Setup Xcode Project**
   ```bash
   cd mobile/ios
   # Create new Xcode project with the provided files
   # Select "App" template
   # Product Name: QUANTFIN
   # Organization Identifier: com.quantfinsociety
   # Interface: SwiftUI
   # Language: Swift
   ```

2. **Add Files**
   - Replace ContentView.swift with QUANTFINApp.swift
   - Update Info.plist with provided configuration

3. **Configure Signing**
   - Select your development team
   - Enable automatic signing

4. **Build and Run**
   - Select target device
   - Press Cmd+R to build and run

5. **Deploy to App Store**
   - Archive the app (Product → Archive)
   - Upload to App Store Connect

## Building the Android App

1. **Import Project**
   ```bash
   cd mobile/android
   # Open in Android Studio
   # File → New → Import Project
   ```

2. **Configure Project**
   - Copy MainActivity.java to src/main/java/com/quantfinsociety/research/
   - Update AndroidManifest.xml
   - Update build.gradle

3. **Add App Icons**
   - Copy icon-192.png to res/mipmap-xxxhdpi/ic_launcher.png
   - Generate other sizes using Android Studio

4. **Build APK**
   ```bash
   ./gradlew assembleRelease
   ```

5. **Deploy to Google Play**
   - Generate signed APK/AAB
   - Upload to Google Play Console

## Progressive Web App (PWA)

The easiest way to get the mobile experience:

1. **iOS Installation**
   - Open Safari
   - Go to https://quantfinexeter.replit.app
   - Tap Share → Add to Home Screen

2. **Android Installation**
   - Open Chrome
   - Go to https://quantfinexeter.replit.app
   - Tap menu → Add to Home screen

## Testing

### iOS Simulator
```bash
xcrun simctl install booted path/to/app.app
xcrun simctl launch booted com.quantfinsociety.research
```

### Android Emulator
```bash
adb install app-release.apk
adb shell am start -n com.quantfinsociety.research/.MainActivity
```

## Distribution

### iOS
- TestFlight for beta testing
- App Store for production

### Android
- Google Play Beta for testing
- Google Play Store for production

### PWA
- Already live at https://quantfinexeter.replit.app
- No app store submission needed