
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

#ifndef OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_H
#define OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_H

#include "AppLogging.h"
#include "AppRendering.h"
#include "Shaders.h"

#include <osgDB/ReadFile>

// This class is the central point of the application.
class App
{
    public:
        App()
        {
            mLogging = new AppLogging;
            mRendering = new AppRendering;
        }
        ~App()
        {
            delete mRendering;
            delete mLogging;
        }

        void loadScene(const std::string &fileName)
        {
            // Load scene.
            osg::Node *scene = osgDB::readNodeFile(fileName);
            if (!scene)
            {
                osg::notify(osg::FATAL) << "Could not load scene";
                return;
            }
            // Load shaders.
            osg::Program *prog = createShaderProgram(shaderVertex, shaderFragment);
            // Apply shaders.
            scene->getOrCreateStateSet()->setAttribute(prog);
            // Set scene.
            mRendering->setScene(scene);
        }
        // Run the application.
        void run() {
            mRendering->run();
        }

    private:
        AppLogging *mLogging;
        AppRendering *mRendering;
};

#endif // OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_H

