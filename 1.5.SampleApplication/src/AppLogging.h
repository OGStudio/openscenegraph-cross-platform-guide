
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

#ifndef OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_LOGGING_H
#define OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_LOGGING_H

#include "Logger.h"

// This class manages application logging.
class AppLogging
{
    public:
        AppLogging()
        {
            // Create custom logger.
            logger = new Logger;
            // Provide the logger to OpenSceneGraph.
            osg::setNotifyHandler(logger);
            // Make sure all notifications are logged.
            osg::setNotifyLevel(osg::DEBUG_FP);
        }
        ~AppLogging()
        {
            // Remove the logger from OpenSceneGraph.
            // This also destroys the logger.
            osg::setNotifyHandler(0);
        }

    private:
        Logger *logger;
};

#endif // OPENSCENEGRAPH_CROSS_PLATFORM_GUIDE_APP_LOGGING_H

