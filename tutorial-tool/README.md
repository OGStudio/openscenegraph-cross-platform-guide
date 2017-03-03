Overview
========

**tutorial-tool** automates creation of video tutorials by combining text and video

Here's a preview:

![Preview](example/video.gif)

Dependencies
============

* [Image magick](http://imagemagick.org)
* [MLT](http://mltframework.org)
* [Python](http://python.org)

Example workflow
================
1. Create one or several videos of something you want to teach

   You can do it with software like [OBS Studio](https://obsproject.com).

2. Convert the video with MLT to 25 FPS

   You can do it with the following command:
   > $ melt -verbose -profile atsc_720p_25 **source_video.mp4** -consumer avformat:**destination_video.mp4** vcodec=libx264

   We will use this [sample video](example/install_blender.mp4).

1. Create background image with 1280x720 resolution

   You can do it with software like [GIMP](http://gimp.org).
   
   We will use this [sample image](example/bg.png).

1. Prepare the script to build final video

   We will use this script:
   ```
   background bg.png
   text 5 Let's install Blender
   video 0:6 install_blender.mp4
   text 5 Installing it with apt
   video 6:26 install_blender.mp4
   text 5 We're still installing it
   video 26:56 install_blender.mp4
   text 5 Congratulations! We just finished installng Blender
   ```
   This script contains all supported language constructs:

   * `background [image]`

     Specifies background **image** to use for text

   * `text [seconds] [text]`

     Specifies **text** to render for desired number of **seconds**

   * `video [seconds_start]:[seconds_end] [video_file]`
     
     Specifies **video_file** part that starts at **seconds_start** and ends at **seconds_end**

1. Bake the video

   Since **tutorial-tool** itself only prints BASH commands for you to execute,
   you should run it like this:
   > /path/to/tutorial-tool /path/to/script **| sh**

1. You get the following video as a result in your temporary directory

   Under Linux the final video is in
   > /tmp/tutorial-tool-cache/video.mp4

   Here is how it looks like: [YouTube video](https://youtu.be/ScwXSJpIXpQ)

