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
----------------------

  ![Screenshot](readme/1.2.1.find.png)

  To install Blender on Debian based distributions, run the following command:

  `sudo apt install blender`

  If you're on macOS or Windows, you can get Blender from its homepage: http://blender.org

1.1.2. Create a deformed cube
-----------------------------

  ![Screenshot](readme/1.1.2.create_deformed_cube.png)

  We create the deformed cube so that it's easy to know which side we're looking
  at when we see it rendered later.

1.1.3. Triangulate the cube: CRITICAL for mobile/web
----------------------------------------------------

  ![Screenshot](readme/1.1.3.triangulate.png)

  Both mobile and web platforms use OpenGL ES to perform 3D rendering,
  which is different from OpenGL used on desktops. One specific aspect
  is that mobile and web only render triangles, not quads.

  By default, Blender uses quads. That's why we manually triangulate
  our model to make sure it can be displayed on all platforms.

1.1.4. UV unwrap the cube for later texturing
---------------------------------------------

  ![Screenshot](readme/1.1.4.uv_unwrap.png)

  This is necessary for correct texturing and calculating visual effects
  in shaders later.

1.1.5. Save the model
---------------------

  ![Screenshot](readme/1.1.5.save.png)

  Save the model for later reference.

1.1.6. Install Blender-to-OpenSceneGraph exporter
-------------------------------------------------

  ![Screenshot](readme/1.1.6.install_exporter.png)

  Install exporter to produce OpenSceneGraph models from within Blender.

1.1.7. Export Blender model to OpenSceneGraph format
----------------------------------------------------

  ![Screenshot](readme/1.1.7.export.png)

  Export the model to OpenSceneGraph format.

1.1.8. Take a look at 'box.osgt' file
-------------------------------------

  ![Screenshot](readme/1.1.8.box_osgt.png)

  Exported OpenSceneGraph format (`*.osgt`) is a text file.

  There also exist binary (`*.osg`, `*.osgb`) and xml (`*.osgx`) formats.
  You might want to use them to speed up loading times.

Resources
=========

* [Blender file](result/box.blend)
* [OpenSceneGraph file](result/box.osgt)

video 10:85 install_under_linux.mp4
text 5 1.2.2. Install git to get OpenSceneGraph
video 85:108 install_under_linux.mp4
text 5 1.2.3. Get latest OpenSceneGraph
video 108:118 install_under_linux.mp4
video 140:150 install_under_linux.mp4
text 5 1.2.4. Create build directory
video 170:184 install_under_linux.mp4
text 5 1.2.5. Try to configure OpenSceneGraph with CMake
video 184:194 install_under_linux.mp4
text 5 1.2.6. Install CMake to configure OpenSceneGraph
video 194:214 install_under_linux.mp4
text 5 1.2.6. Try to configure OpenSceneGraph once again
video 218:230 install_under_linux.mp4
text 5 1.2.7. Observe configuration errors
video 230:237 install_under_linux.mp4
video 247:257 install_under_linux.mp4
text 5 1.2.8. Install missing OpenGL libraries
video 260:315 install_under_linux.mp4
text 5 1.2.9. Configure OpenSceneGraph
video 315:323 install_under_linux.mp4
text 5 1.2.10. Observe found OpenGL library location
video 323:338 install_under_linux.mp4
text 5 1.2.11. Build OpenSceneGraph
video 344:371 install_under_linux.mp4
video 406:416 install_under_linux.mp4
video 436:446 install_under_linux.mp4
video 458:468 install_under_linux.mp4
video 566:570 install_under_linux.mp4
video 660:664 install_under_linux.mp4
video 791:795 install_under_linux.mp4
video 911:915 install_under_linux.mp4
video 1055:1090 install_under_linux.mp4
text 5 1.2.12. Install OpenSceneGraph
video 1090:1102 install_under_linux.mp4
text 5 1.2.13. Try to check 'box.osgt' with 'osgviewer'
video 1104:1116 install_under_linux.mp4
text 5 1.2.14. Locate OpenSceneGraph libraries
video 1124:1135 install_under_linux.mp4
text 5 1.2.15. Tell dynamic linker where to find OpenSceneGraph libraries
video 1135:1177 install_under_linux.mp4
text 5 1.2.16. Check 'box.osgt' with 'osgviewer'
