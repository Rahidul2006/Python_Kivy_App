# 📱 Build APK Using Google Colab

> 🚀 **Quick Guide:** Build your Kivy/KivyMD app into an Android APK without installing Android SDK locally!

---

## 📋 Prerequisites

- ✅ Google account (for Colab)
- ✅ Your Python project with `main.py`
- ✅ Stable internet connection
- ✅ Android device for testing (optional)

---

## 🔧 Step 1: Set Up Google Colab

1. Visit [Google Colab](https://colab.research.google.com/)
2. Click **"New notebook"** button
3. Rename your notebook to something like `"Build-Kivy-APK"`

---

## 📥 Step 2: Install Required Dependencies

Run these commands in separate cells:

```bash
!pip install buildozer
!pip install cython==0.29.19
```

### Cell 2: Install System Dependencies (SDL2, FFmpeg, etc.)

```bash
!sudo apt-get install -y \
  python3-pip \
  build-essential \
  git \
  python3 \
  python3-dev \
  ffmpeg \
  libsdl2-dev \
  libsdl2-image-dev \
  libsdl2-mixer-dev \
  libsdl2-ttf-dev \
  libportmidi-dev \
  libswscale-dev \
  libavformat-dev \
  libavcodec-dev \
  zlib1g-dev
```

### Cell 3: Install Additional Build Dependencies

```bash
!sudo apt-get install -y \
  build-essential \
  libsqlite3-dev \
  sqlite3 \
  bzip2 \
  libbz2-dev \
  zlib1g-dev \
  libssl-dev \
  openssl \
  libgdbm-dev \
  libgdbm-compat-dev \
  liblzma-dev \
  libreadline-dev \
  libncursesw5-dev \
  libffi-dev \
  uuid-dev
```

---

## 📂 Step 3: Upload Your Project

1. Click the **"Files"** icon on the left sidebar
2. Click **"Upload"** button
3. Select your `main.py` file
4. Wait for upload to complete

---

## ⚙️ Step 4: Initialize Buildozer Configuration

Run this command in a new cell:

```bash
!buildozer init
```

This creates a `buildozer.spec` file in your current directory.

---

## ✏️ Step 5: Configure buildozer.spec

1. Navigate to the **Files** section
2. Find and double-click `buildozer.spec`
3. Find **line 40** (look for the `requirements` line)
4. Add This :

```ini
requirements = kivy==2.3.1,kivymd,pillow
```

**Or for the latest KivyMD 2.0.0:**

```ini
requirements = kivy==2.3.1,https://github.com/kivymd/KivyMD/archive/master.zip,pillow
```

5. **Save** the file (Ctrl+S)

---

## 🏗️ Step 6: Build the APK

Run this command in a new cell (⏳ **This takes 10-20 minutes**):

```bash
!buildozer -v android debug
```

**Output:**
- Buildozer will create the APK and place it in the `bin/` folder
- File name: `app-debug.apk` or similar

---

## 📥 Step 7: Download Your APK

1. Navigate to the **Files** section
2. Go to **bin/** folder
3. Right-click `app-debug.apk`
4. Click **"Download"**

---

## 📱 Step 8: Install on Android Device

1. Transfer `app-debug.apk` to your Android phone
2. Open file manager on phone
3. Tap the APK file
4. Click **"Install"** (may need to enable unknown sources)
5. Launch your app! 🎉

---

## 🐛 Troubleshooting

### Build Fails with "Permission Denied"

**Solution:** Add execute permission:

```bash
!chmod +x /root/.buildozer/android/platform/android-ndk-r25c/ndk-build
```

### "Java not found" Error

**Solution:** Install Java:

```bash
!sudo apt-get install -y default-jdk
```

### Build Takes Too Long

**Solution:** This is normal! ⏳ First builds take 15-20 minutes. Subsequent builds are faster.

### APK Won't Install

**Solution:** Check if:
- ✅ Unknown sources are enabled on phone
- ✅ Android version is 5.0+ (API 21+)
- ✅ Sufficient storage space

---

## 📊 Build Process Overview

| Step | Time | Description |
|------|------|-------------|
| Download NDK | 5 min | First time only |
| Compile Python | 5-10 min | Python interpreter |
| Build APK | 5-10 min | Packaging |
| **Total** | **15-20 min** | First build |

---

## ✨ Tips

- 💾 **Save often:** Keep your `main.py` backed up
- 🔄 **Version control:** Use Git to manage changes
- 📦 **Minimize size:** Remove unnecessary dependencies
- 🎨 **Test locally:** Always run on desktop first
- 🔐 **Sign APK:** For production, add signing certificates

---

## 📚 Additional Resources

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy on Android](https://kivy.org/doc/stable/guide/packaging-android.html)
- [KivyMD GitHub](https://github.com/kivymd/KivyMD)

---

**Last Updated:** January 25, 2026