Table of contents
=================

* [Overview](#overview)
* [Video](#video)
* [Steps](#steps)
  * [1.9.1. Create build directory](#step-build-dir)
  * [1.9.2. Launch CMake](#step-open-cmake)
  * [1.9.3. Specify build and source directories](#step-dirs)
  * [1.9.4. Add iOS specific variables](#step-vars)
  * [1.9.5. Configure OpenSceneGraph](#step-cfg)
  * [1.9.6. Generate Xcode project file](#step-generate)
  * [1.9.7. Build OpenSceneGraph](#step-build-osg)


* Create build directory
  for osgNativeLib
* Launch CMake
* Specify build and source directories
  by default it configures for iOS simulator
* Configure osgNativeLib
* Generate Xcode project file
* Build osgNativeLib
  it also builds OpenSceneGraph, actual osgNativeLib
  packages static libs into single osglib


<a name="overview"/>

Overview
========

This tutorial is part of [OpenSceneGraph cross-platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we build and run
[sample OpenSceneGraph application](http://github.com/OGStudio/openscenegraph-cross-platform-guide-application)
under iOS. The application displays provided model with simple GLSL shaders.

**Note**: this tutorial requires
* OpenSceneGraph model (see [1.1. Create a cube](../1.1.CreateCube))
* Xcode and CMake installations (see [1.4. Install OpenSceneGraph under macOS](../1.4.InstallUnderMacOS))
* OpenSceneGraph sources (see [1.4. Install OpenSceneGraph under macOS](../1.4.InstallUnderMacOS))
* sample OpenSceneGraph application sources (see [1.7. Build and run sample OpenSceneGraph application under macOS](../1.7.SampleUnderMacOS))

<a name="video"/>

Video
=====

[YouTube](todo) | [Download](readme/video.mp4)

Video depicts running and building sample OpenSceneGraph application
for iOS simulator with iOS 10.

<a name="steps"/>

Steps
=====

**Note**: steps below use frames from the video as screenshots.
Watch the video to see all details.

<a name="step-build-dir"/>

1.9.1. Create build directory
-----------------------------

  ![Screenshot](readme/f???.png)

  Create build directory for iOS simulator build of OpenSceneGraph.  

  iOS simulator build only works under iOS simulator. If you need
  to build for a real device, you need an additional build of
  OpenSceneGraph in a separate directory.

<a name="step-open-cmake"/>

1.9.2. Launch CMake
-------------------

  ![Screenshot](readme/f???.png)

  Open CMake

<a name="step-dirs"/>

1.9.3. Specify build and source directories
-------------------------------------------

  ![Screenshot](readme/f???.png)

  Specify build and source directories.

<a name="step-vars"/>

1.9.4. Add iOS specific variables
---------------------------------

  ![Screenshot](readme/f???.png)

  Add the following variables **before** pressing `Configure`:
  - `BUILD_OSG_APPLICATIONS=OFF` makes sure we don't build applications
  - `CMAKE_OSX_SYSROOT=/path/to/iOS/SDK` specifies path to SDK (simulator or real device)
  - `DYNAMIC_OPENSCENEGRAPH=OFF` makes sure we build OpenSceneGraph statically
  - `DYNAMIC_OPENTHREADS=OFF` makes sure we build OpenThreads statically
  - `OPENGL_PROFILE=GLES2` specifies GLES2 OpenGL profile
  - `OSG_WINDOWING_SYSTEM=IOS` specifies iOS windowing system
  - `OSG_BUILD_PLATFORM_IPHONE_SIMULATOR=ON` is only necessary if you build for simulator

  **Note**: you **must** specify these variables **before** pressing `Configure`,
  otherwise you won't be able to build OpenSceneGraph.

<a name="step-cfg"/>

1.9.5. Configure OpenSceneGraph
-------------------------------

  ![Screenshot](readme/f???.png)

  Press `Configure`. Select `Xcode` generator when prompted.

<a name="step-generate"/>

1.9.6. Generate Xcode project file
-----------------------------------

  ![Screenshot](readme/???.png)

  Press `Generate` to generate Xcode specific project file.

<a name="step-build-osg"/>

1.9.7. Build OpenSceneGraph
---------------------------

  ![Screenshot](readme/???.png)

  Build OpenSceneGraph with the following command:

  `xcodebuild -IDEBuildOperationMaxNumberOfConcurrentCompileTasks=6 -configuration Release`

