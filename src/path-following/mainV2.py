# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:24:40 2024

@author: Conrado
"""

#%%
import os
import logging

if (os.path.isdir("logs") is False): os.mkdir("logs")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s][%(levelname)s][%(threadName)s][%(module)s][line %(lineno)d] %(message)s',
    handlers=[
        logging.FileHandler("logs/logs.log", mode='w+'),
        logging.StreamHandler()
    ]
)



logger = logging.getLogger()

logger.info("Logger created!")

#%%

import numpy as np
from trajectory2D import trajectory2D

#Init the Path Object with the desired trajectory config/parameters
#logger.info(f"Creating a path object with trajectory config '{desiredTrajectory}' ...")
pathObj = trajectory2D(trajectoryName = "trajectory_eightshape_v1")

#Build the Path segments
pathObj.eightShape(delta = np.pi/8)

#Fix the straight lines:
pathObj.fixEightShapeLineVectors()

#Build the trajectory
pathObj.buildEightShapeTrajectory()


#%%

from envMap import envMap

#Create the environment map object
env_map = envMap()

#Draw the eight shape path
env_map.drawEightShape(pathObj)