Table of contents
=================

* [Overview](#overview)
* [Video](#video)
* [Steps](#steps)
  * [1.10.1. Find Emscripten site](#step-find-emscripten)
  * [1.10.2. Download Emscripten portable SDK archive](#step-dl-emscripten)
  * [1.10.3. Extract Emscripten portable SDK](#step-extract-emscripten)
  * [1.10.4. Install Emscripten portable SDK](#step-install-emscripten)


  * [1.10.3. Create build directory](#step-build-dir)


  * [1.5.3. Configure the build](#step-cfg)
  * [1.5.4. Build application](#step-build)
  * [1.5.5. Run application](#step-run)



  * [1.9.2. Launch CMake](#step-open-cmake)
  * [1.9.3. Specify build and source directories](#step-dirs)
  * [1.9.4. Configure osgNativeLib and OSG](#step-cfg)
  * [1.9.5. Generate Xcode project file](#step-generate)
  * [1.9.6. Build osgNativeLib and OSG](#step-build)
  * [1.9.7. Start a new Xcode project](#step-xcode)
  * [1.9.8. Select Single View Application](#step-single-view)
  * [1.9.9. Select Objective-C language](#step-objc)
  * [1.9.10. Finish project creation](#step-proj)
  * [1.9.11. Copy combined library](#step-copy-lib)
  * [1.9.12. Copy view controller and model](#step-copy)
  * [1.9.13. Add copied files to the project](#step-add)
  * [1.9.14. Select RenderVC as the main interface](#step-main)
  * [1.9.15. Reference osgNativeLib headers](#step-headers)
  * [1.9.16. Run the project](#step-run)

<a name="overview"/>

Overview
========

This tutorial is part of [OpenSceneGraph cross-platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we build and run
[sample OpenSceneGraph application](http://github.com/OGStudio/openscenegraph-cross-platform-guide-application)
under Linux for Web. The application displays provided model with simple GLSL shaders.

**Note**: this tutorial requires
* OpenSceneGraph model (see [1.1. Create a cube](../1.1.CreateCube))
* CMake and git installations (see [1.2. Install OpenSceneGraph under Linux](../1.2.InstallUnderLinux))
* OpenSceneGraph sources (see [1.2. Install OpenSceneGraph under Linux](../1.2.InstallUnderLinux))
* sample OpenSceneGraph application sources (see [1.5. Build and run sample OpenSceneGraph application under Linux](../1.5.SampleUnderLinux))

<a name="video"/>

Video
=====

[YouTube](todo) | [Download](readme/video.mp4)

Video depicts running and building sample OpenSceneGraph application
under Xubuntu 16.04 with Emscripten 1.37.9 for Web.

<a name="steps"/>

Steps
=====

**Note**: steps below use frames from the video as screenshots.
Watch the video to see all details.

<a name="step-find-emscripten"/>

1.10.1. Find Emscripten site
----------------------------

  ![Screenshot](readme/f?.png)

  Find main Emscripten site.
  
  We need Emscripten portable SDK, because Xubuntu 16.04
  ships an outdated version.

<a name="step-dl-emscripten"/>

1.10.2. Download Emscripten portable SDK archive
------------------------------------------------

  ![Screenshot](readme/f?.png)

  Download the latest
  [Emscripten portable SDK archive](http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html).

<a name="step-extract-emscripten"/>

1.10.3. Extract Emscripten portable SDK
---------------------------------------

  ![Screenshot](readme/f?.png)

  Unpack Emscripten portable SDK to your home directory.

<a name="step-install-emscripten"/>

1.10.4. Install Emscripten portable SDK
---------------------------------------

  ![Screenshot](readme/f?.png)

  Install Emscripten portable SDK by running the following commands:

  `cd ~/emsdk-portable`

  `./emsdk update`

  `./emsdk install latest`

  `./emsdk activate latest`

  `source ./emsdk_env.sh`

  **Note**: the above commands come from the
  [official Emscripten installation instructions](http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html).










  Create build directory for iOS simulator build of osgNativeLib,
  a native C++ library to be used in Objective-C.

  osgNativeLib also builds OpenSceneGraph inside
  `/path/to/openscenegraph-cross-platform-guide-application/../OpenSceneGraph/build/Simulator`.

  **Note**: iOS simulator build only works under iOS simulator. If you need
  to build for a real device, you need to build osgNativeLib
  with `BUILD_SIMULATOR=NO` in a separate directory. In such a case
  OpenSceneGraph is built inside
  `/path/to/openscenegraph-cross-platform-guide-application/../OpenSceneGraph/build/Device`.

<a name="step-open-cmake"/>

1.9.2. Launch CMake
-------------------

  ![Screenshot](readme/f033.png)

  Open CMake

<a name="step-dirs"/>

1.9.3. Specify build and source directories
-------------------------------------------

  ![Screenshot](readme/f068.png)

  Specify build and source directories.

<a name="step-cfg"/>

1.9.4. Configure osgNativeLib and OSG
-------------------------------------

  ![Screenshot](readme/f083.png)

  Press `Configure`. Select `Xcode` generator when prompted.

<a name="step-generate"/>

1.9.5. Generate Xcode project file
-----------------------------------

  ![Screenshot](readme/f145.png)

  Press `Generate` to generate Xcode specific project file.

<a name="step-build"/>

1.9.6. Build osgNativeLib and OSG
---------------------------------

  ![Screenshot](readme/f180.png)

  Build osgNativeLib and OpenSceneGraph with the following commands:

  `cd /path/to/build/dir`

  `xcodebuild -IDEBuildOperationMaxNumberOfConcurrentCompileTasks=8 -configuration Release`

  At the end the build process combines osgNativeLib and several OpenSceneGraph
  libraries into single `libosglib.a` library. This is done for convenience.

<a name="step-xcode"/>

1.9.7. Start a new Xcode project
--------------------------------

  ![Screenshot](readme/f233.png)

  Start a new Xcode project.

<a name="step-single-view"/>

1.9.8. Select Single View Application
--------------------------------

  ![Screenshot](readme/f250.png)

  Select Single View Application.

<a name="step-objc"/>

1.9.9. Select Objective-C language
----------------------------------

  ![Screenshot](readme/f280.png)

  Select Objective-C language and provide application specific
  information like title, organization, etc.

<a name="step-proj"/>

1.9.10. Finish project creation
-------------------------------

  ![Screenshot](readme/f299.png)

  Select project directory and finish project creation.

<a name="step-copy-lib"/>

1.9.11. Copy combined library
-----------------------------

  ![Screenshot](readme/f330.png)

  Copy combined library into project directory with the following command:

  `cp /path/to/build/dir/libosglib.a /path/to/xcode/project/subdir/`

<a name="step-copy"/>

1.9.12. Copy view controller and model
--------------------------------------

  ![Screenshot](readme/f365.png)

  Copy view controller and model with the following command:

  `cp -R /path/to/openscenegraph-cross-platform-guide-application/ios/project/* /path/to/xcode/project/subdir`
  
  Sample OpenSceneGraph application's *ios/project* directory contains
  a box model and `RenderVC`. `RenderVC` is a view controller that renders
  the model with osgNativeLib.

<a name="step-add"/>

1.9.13. Add copied files to the project
---------------------------------------

  ![Screenshot](readme/f382.png)

  For Xcode to see the files, they should be added to the project.

<a name="step-main"/>

1.9.14. Select RenderVC as the main interface
---------------------------------------------

  ![Screenshot](readme/f396.png)

  Go to `General` project page and select `RenderVC.storyboard` as
  the main interface.

<a name="step-headers"/>

1.9.15. Reference osgNativeLib headers
--------------------------------------

  ![Screenshot](readme/f456.png)

  Since we have not added osgNativeLib headers to the project, we should
  reference them to be able to call osgNativeLib functions.

  Go to project's `Build Settings`, find `Header Search Paths` section,
  then add the following search paths:

  `/path/to/openscenegraph-cross-platform-guide-application/ios/src`

  `/path/to/openscenegraph-cross-platform-guide-application/ios/src-gen`

<a name="step-run"/>

1.9.16. Run the project
-----------------------

  ![Screenshot](readme/f527.png)

  Select iPhone simulator and run the project.
  You should see red cube displayed.

