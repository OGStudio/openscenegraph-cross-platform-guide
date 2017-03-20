Table of contents
=================

* [Overview](#overview)
* [Video](#video)
* [Steps](#steps)
  * [1.3.1. Find MSYS2](#step-find-msys2)
  * [1.3.2. Download MSYS2](#step-download-msys2)
  * [1.3.3. Install MSYS2](#step-install-msys2)
  * [1.3.4. Update MSYS2 core packages](#step-update-msys2-core)
  * [1.3.5. Update MSYS2 system packages](#step-update-msys2-system)
  * [1.3.6. Find MinGW-w64 CMake](#step-find-cmake)
  * [1.3.7. Install build tools](#step-install-build-tools)


<a name="overview"/>

Overview
========

This tutorial is part of [OpenSceneGraph cross-platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we install OpenSceneGraph under Windows and take a look
at the cube with **osgviewer** tool.

<a name="video"/>

Video
=====

[YouTube](https://todo) | [Download](readme/video.mp4)

Video depicts OpenSceneGraph installation under 64-bit Windows 7.

<a name="steps"/>

Steps
=====

<a name="step-find-msys2"/>

1.3.1. Find MSYS2
-------------------------------------

  ![Screenshot](readme/1.3.1.find_msys2.png)

  [MSYS2](http://msys2.org) is a software distro and building platform
  for Windows.

  We use MSYS2 to build and install OpenSceneGraph, because it provides
  Unix-like environment with everything that is necessary to
  build Windows applications: Git, CMake, GCC and a lot more.

<a name="step-download-msys2"/>

1.3.2. Download MSYS2
-------------------------------------

  ![Screenshot](readme/1.3.2.download_msys2.png)

  Choose package suitable for your version of Windows.
  In case of 64-bit Windows, it's MSYS2 *x86_64*.

<a name="step-install-msys2"/>

1.3.3. Install MSYS2
-------------------------------------

  ![Screenshot](readme/1.3.3.install_msys2.png)

  Run the downloaded package.

<a name="step-update-msys2-core"/>

1.3.4. Update MSYS2 core packages
---------------------------------

  ![Screenshot](readme/1.3.4.update_msys2_core.png)

  Run the following command in MSYS2:

  `pacman -Syu`

  Once finished, close MSYS2.

<a name="step-update-msys2-system"/>

1.3.5. Update MSYS2 system packages
-----------------------------------

  ![Screenshot](readme/1.3.5.update_msys2_system.png)

  Reopen MSYS2 and run the following command:

  `pacman -Su`

  Now, MSYS2 is ready for us.

<a name="step-find-cmake"/>

1.3.6. Find MinGW-w64 CMake
-----------------------------------

  ![Screenshot](readme/1.3.6.find_cmake.png)

  In order to build Windows applications, we need to use MinGW-w64 tools.
  [MinGW-w64](http://http://mingw-w64.org) is an advancement of the original
  [MinGW](http://mingw.org) project, created to support the GCC compiler on
  Windows.

  To find relevant CMake package, run the following command:

  `pacman -Ss mingw-w64 | grep cmake`

<a name="install-cmake-tools"/>

1.3.7. Install build tools
--------------------------

  ![Screenshot](readme/1.3.7.install_build_tools.png)

  To install CMake, Make, and GCC, run the following command:

  `pacman -S mingw-w64-i686-cmake mingw-w64-i686-make mingw-w64-i686-gcc`

  We use 32-bit versions, because we want to build 32-bit OpenSceneGraph,
  which would work on both 32- and 64-bit Windows.

