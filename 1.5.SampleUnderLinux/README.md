Table of contents
=================

* [Overview](#overview)
* [Video](#video)
* [Steps](#steps)
  * [1.5.1. Get sample application](#step-get)
  * [1.5.2. Create build directory](#step-build-dir)
  * [1.5.3. Configure the build](#step-cfg)
  * [1.5.4. Build application](#step-build)
  * [1.5.5. Run application](#step-run)


<a name="overview"/>

Overview
========

This tutorial is part of [OpenSceneGraph cross-platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we build and run
[sample OpenSceneGraph application](http://github.com/OGStudio/openscenegraph-cross-platform-guide-application)
under Linux. The application displays provided model with simple GLSL shaders.

**Note**: this tutorial requires
* OpenSceneGraph installation (see [1.2. Install OpenSceneGraph under Linux](../1.2.InstallUnderLinux))
* OpenSceneGraph model (see [1.1. Create a cube](../1.1.CreateCube))

<a name="video"/>

Video
=====

[YouTube](https://youtu.be/5wL0H0W2oWQ) | [Download](readme/video.mp4)

Video depicts running and building sample OpenSceneGraph application
under Xubuntu 16.04.

<a name="steps"/>

Steps
=====

**Note**: steps below use frames from the video as screenshots.
Watch the video to see all details.

<a name="step-get"/>

1.5.1. Get sample application
-----------------------------

  ![Screenshot](readme/f027.png)

  Get the latest copy of sample application with the following command:

  `git clone https://github.com/OGStudio/openscenegraph-cross-platform-guide-application.git`

<a name="step-build-dir"/>

1.5.2. Create build directory
-----------------------------

  ![Screenshot](readme/f045.png)

  Create a separate build directory for sample application, just as you did for
  OpenSceneGraph.

<a name="step-cfg"/>

1.5.3. Configure the build
--------------------------

  ![Screenshot](readme/f063.png)

  Configure sample application build with the following commands:
 
  `cd /path/to/build/dir`

  `cmake /path/to/source/dir`

<a name="step-build"/>

1.5.4. Build application
------------------------

  ![Screenshot](readme/f070.png)

  Build sample application with the following commands:

  `cd /path/to/build/dir`

  `make`

<a name="step-run"/>

1.5.5. Run application
----------------------

  ![Screenshot](readme/f101.png)

  Run sample application with the following commands:

  `cd /path/to/build/dir`

  `./sampleApplication /path/to/box.osgt`

