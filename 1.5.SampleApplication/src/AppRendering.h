
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

#ifndef OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_RENDERING_H
#define OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_RENDERING_H

#include "Rendering.h"

#include <osgViewer/Viewer>

// This class manages application rendering.
class AppRendering
{
    public:
        AppRendering()
        {
            // Create OpenSceneGraph viewer.
            mViewer = new osgViewer::Viewer;
            // Use single thread: CRITICAL for web.
            mViewer->setThreadingModel(osgViewer::ViewerBase::SingleThreaded);
            // Setup window size.
            setupWindow(1024, 768);
        }
        ~AppRendering()
        {
            // Tear down the viewer.
            delete mViewer;
        }

        void run()
        {
            // Launch the viewer.
            mViewer->run();
        }

    private:
        void setupWindow(int width, int height)
        {
            osg::GraphicsContext *gc =
                createGraphicsContext("Sample", 100, 100, width, height);
            // Configure viewer's camera with FOVY and window size.
            osg::Camera *cam = mViewer->getCamera();
            setupCamera(cam, gc, 30, width, height);
        }

        osgViewer::Viewer *mViewer;
};

#endif // OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_RENDERING_H

