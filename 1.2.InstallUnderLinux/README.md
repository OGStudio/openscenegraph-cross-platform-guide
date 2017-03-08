1.2. Install OpenSceneGraph under Linux
=======================================

This tutorial is part of [OpenSceneGraph cross platform guide](http://github.com/OGStudio/openscenegraph-cross-platform-guide).

In this tutorial we install OpenSceneGraph under Linux and take a look
at the cube with standard **osgviewer** tool.

Video
=====

[YouTube](https://youtu.be/4w0tAicl_70) | [Download](readme/video.mp4)

Video depicts OpenSceneGraph installation under Xubuntu 16.04.

Steps
=====

1.2.1. Find OpenSceneGraph repository
-------------------------------------

  ![Screenshot](readme/1.2.1.find.png)

  Find OpenSceneGraph repository at the website.

1.2.2. Install git to get OpenSceneGraph
----------------------------------------

  ![Screenshot](readme/1.2.2.install_git.png)

  Since [OpenSceneGraph is hosted at GitHub](https://github.com/openscenegraph/OpenSceneGraph),
  we need to install git.

  To install git on Debian based distributions, run the following command:

  `sudo apt install git`

1.2.3. Get latest OpenSceneGraph
--------------------------------

  ![Screenshot](readme/1.2.3.get_osg.png)

  Get the latest copy of OpenSceneGraph with the following command:

  `git clone https://github.com/openscenegraph/OpenSceneGraph.git`

1.2.4. Create build directory
-----------------------------

  ![Screenshot](readme/1.2.4.build_dir.png)
  
  OpenSceneGraph uses CMake build system, which supports out-of-source builds.
  We create a build directory to keep generated (built) content separate
  from the original source.


1.2.5. Try to configure OpenSceneGraph with CMake
-------------------------------------------------

  ![Screenshot](readme/1.2.5.try_cfg.png)

  Before we can build OpenSceneGraph, we need to configure the build.

  However, CMake is not yet installed.

1.2.6. Install CMake to configure OpenSceneGraph
-------------------------------------------------

  ![Screenshot](readme/1.2.6.install_cmake.png)

  To install CMake on Debian based distributions, run the following command:

  `sudo apt install cmake`

1.2.7. Try to configure OpenSceneGraph once again
-------------------------------------------------

  ![Screenshot](readme/1.2.7.cfg.png)

  Configure OpenSceneGraph build with the following commands:
 
  `cd /path/to/build/dir`

   `cmake /path/to/source/dir`

  We use default configuration without specifying anything.

1.2.8. Observe configuration errors
-------------------------------------

  ![Screenshot](readme/1.2.8.cfg_errors.png)

  As you see, configuration process could not resolve `OPENGL_INCLUDE_DIR`
  variable. This means CMake could not find OpenGL libraries.

1.2.9. Install missing OpenGL libraries
---------------------------------------

  ![Screenshot](readme/1.2.9.install_gl.png)

  The easiest way to install OpenGL libraries is to install GLUT development package,
  which will bring OpenGL libraries in as a dependency.

  To install GLUT development package on Debian based distributions,
  run the following command:

  `sudo apt install freeglut3-dev`

1.2.10. Configure OpenSceneGraph
--------------------------------

  ![Screenshot](readme/1.2.10.cfg_osg.png)

  Configure OpenSceneGraph once again. There are no OpenGL errors anymore.

1.2.11. Observe found OpenGL library location
---------------------------------------------

  ![Screenshot](readme/1.2.11.gl_path.png)

  As you see, configuration process has successfully found OpenGL libraries.

1.2.12. Build OpenSceneGraph
----------------------------

  ![Screenshot](readme/1.2.12.build.png)

  We are finally ready to build OpenSceneGraph with the following command:

  `make -j10`

  We use `-j10` to run 10 parallel jobs. This makes building faster.

1.2.13. Install OpenSceneGraph
------------------------------

  ![Screenshot](readme/1.2.13.install.png)

  Install OpenSceneGraph with the following command:

  `sudo make install`

1.2.14. Try to check 'box.osgt' with 'osgviewer'
------------------------------------------------

  ![Screenshot](readme/1.2.14.try_check.png)
  
  Try to take a look at the cube with standard **osgviewer** tool.
  It cannot find OpenSceneGraph libraries.

1.2.15. Locate OpenSceneGraph libraries
---------------------------------------

  ![Screenshot](readme/1.2.15.locate.png)

  By default, OpenSceneGraph is installed into `/usr/local/lib64` on 64-bit
  Linux distributions. This location is not a standard library path.

1.2.16. Tell dynamic linker where to find OpenSceneGraph libraries
------------------------------------------------------------------

  ![Screenshot](readme/1.2.16.linker.png)

  Specify `/usr/local/lib64` inside `/etc/ld.so.conf` to make sure
  dynamic linker is aware of the directory with OpenSceneGraph libraries.

  Then refresh the linker cache with the following command:

  `sudo ldconfig`

1.2.17. Check 'box.osgt' with 'osgviewer'
-------------------------------------

  ![Screenshot](readme/1.2.17.viewer.png)

  Finally, take a look at the cube with standard **osgviewer** tool:

  `osgviewer /path/to/box.osgt`

