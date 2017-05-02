Table of contents
=================

* [Overview](#overview)
* [Video](#video)
* [Steps](#steps)
  * [1.8.1. Download Android Studio](#step-dl-as)
  * [1.8.2. Install 32-bit libraries](#step-32-libs)
  * [1.8.3. Unpack Android Studio](#step-unpack-as)
  * [1.8.4. Run Android Studio](#step-run-as)
  * [1.8.5. Complete Android Studio installation](#step-install-as)
  * [1.8.6. Wait for components to download](#step-wait-as)
  * [1.8.7. Run SDK Manager](#step-run-sdk)
  * [1.8.8. Select CMake, LLDB, NDK components](#step-select-ndk)
  * [1.8.9. Accept license](#step-license)
  * [1.8.10. Wait for CMake, LLDB, NDK to download](#step-wait-ndk)

<a name="overview"/>

Overview
========

This tutorial is part of [OpenSceneGraph cross-platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we build and run
[sample OpenSceneGraph application](http://github.com/OGStudio/openscenegraph-cross-platform-guide-application)
under Android. The application displays provided model with simple GLSL shaders.

**Note**: this tutorial requires
* OpenSceneGraph model (see [1.1. Create a cube](../1.1.CreateCube))

<a name="video"/>

Video
=====

[YouTube](todo) | [Download](readme/video.mp4)

Video depicts running and building sample OpenSceneGraph application
with Android Studio 2.3.1 under Xubuntu 16.04.

<a name="steps"/>

Steps
=====

**Note**: steps below use frames from the video as screenshots.
Watch the video to see all details.

<a name="step-dl-as"/>

1.8.1. Download Android Studio
------------------------------

  ![Screenshot](readme/f041.png)

  Download the latest version of Android Studio.
  It contains all the tools you need to develop for Android.

<a name="step-32-libs"/>

1.8.2. Install 32-bit libraries
-------------------------------

  ![Screenshot](readme/f101.png)

  According to [Android Studio installation instructions](https://developer.android.com/studio/install.html)
  64-bit Ubuntu needs several 32-bit libraries to make Android Studio work.

  Install necessary 32-bit libraries with the following command:

  `sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386`

<a name="step-unpack-as"/>

1.8.3. Unpack Android Studio
----------------------------

  ![Screenshot](readme/f165.png)

  Extract Android Studio archive into your home directory.

<a name="step-cfg-as"/>

1.8.4. Run Android Studio
-------------------------------

  ![Screenshot](readme/f191.png)

  Run Android Studio with the following command:

  `cd ~`

  `./android-studio/bin/studio.sh`

<a name="step-install-as"/>

1.8.5. Complete Android Studio installation
-------------------------------------------

  ![Screenshot](readme/f216.png)

  Select standard installation options.

<a name="step-wait-as"/>

1.8.6. Wait for components to download
--------------------------------------

  ![Screenshot](readme/f244.png)

  Wait for standard components to download.

<a name="step-run-sdk"/>

1.8.7. Run SDK Manager
----------------------

  ![Screenshot](readme/f274.png)

  Run SDK manager to install components that are required to build C++.

<a name="step-install-ndk"/>

1.8.8. Select CMake, LLDB, NDK components
-----------------------------------------

  ![Screenshot](readme/f292.png)

  We need CMake, LLDB, and NDK components to build C++ for Android.

  Select them in *SDK Tools* tab of *SDK Manager*.

<a name="step-license"/>

1.8.9. Accept license
---------------------

  ![Screenshot](readme/f302.png)

  To install CMake, LLDB, and NDK, we need to accept the license.

<a name="step-wait-ndk"/>

1.8.10. Wait for CMake, LLDB, NDK to download
---------------------------------------------

  ![Screenshot](readme/f325.png)

  Wait for additional components to download.

