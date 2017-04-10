
/*
This file is part of OpenSceneGraph cross-platform guide:
  https://github.com/OGStudio/openscenegraph-cross-platform-guide

Copyright (C) 2017 Opensource Game Studio

This software is provided 'as-is', without any express or implied
warranty.  In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
*/

#ifndef OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_RENDERING_H
#define OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_RENDERING_H

#include <osg/Camera>
#include <osg/GraphicsContext>

// Create graphics context that specifies render window configuration.
osg::GraphicsContext *createGraphicsContext(
    const std::string &title,
    int x,
    int y,
    int width,
    int height)
{
    // Traits is a struct to combine necessary parameters.
    osg::GraphicsContext::Traits *traits =
        new osg::GraphicsContext::Traits;
    // Geometry.
    traits->x                = x;
    traits->y                = y;
    traits->width            = width;
    traits->height           = height;
    // Title.
    traits->windowName       = title;
    // Window borders.
    traits->windowDecoration = true;
    // Double buffer.
    traits->doubleBuffer     = true;
    // Create GC.
    return osg::GraphicsContext::createGraphicsContext(traits);
}

// Configure camera with common defaults.
void setupCamera(
    osg::Camera *cam,
    osg::GraphicsContext *gc,
    double fovy,
    int width,
    int height)
{
    // Provide GC.
    cam->setGraphicsContext(gc);
    // Viewport must have the same size.
    cam->setViewport(new osg::Viewport(0, 0, width, height));
    // Clear depth and color buffers each frame.
    cam->setClearMask(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);
    // Aspect ratio.
    float aspect = static_cast<float>(width) / static_cast<float>(height);
    // Configure projection.
    cam->setProjectionMatrixAsPerspective(30, aspect, 1, 1000);
}

#endif // OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_RENDERING_H

