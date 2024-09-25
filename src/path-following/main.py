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
    format='[%(asctime)s][%(levelname)s][%(threadName)s][%(module)s][%(funcName)s][line %(lineno)d] %(message)s',
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


#_:_:_:_:_:_:_:_ forcing an horizontal line (for tests)
pathObj.buildHorizontalLine(x0=0, x1=50, y0=0, nr_points=10000)


#%%

from envMap import envMap

#Create the environment map object
env_map = envMap()

#Draw the eight shape path
env_map.drawShape(pathObj, blockPlot=False)




"""
# Now, you can add random XY points in the future like this:
import numpy as np

# Simulate adding new data over time
for i in range(50):
    # Generate new random XY points
    new_Xdata = np.random.rand(10)
    new_Ydata = np.random.rand(10)

    # Add the new data to the plot in real-time
    env_map.add_data_to_plot(new_Xdata, new_Ydata, pause_time=0.1)

    # Simulate a delay for data generation (optional)
    time.sleep(0.5)
#end-for
"""

#%%
import time
from carModel import carModel


T = 100 #Simulation time
timestep = 0.1 #Timestep


T = len(pathObj.trajectoryPointsX)
timestep = 1


#Initialize the car object
car = carModel(x0 = 0, y0 = 2, v0 = 1.0,
               radius1  = 4,
               radius2 = 4)
car.Kp = 0.1
car.Ki = 0
car.Kd = 0.2


def computeEuclidianDistance(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5
#end-def

for t in range(0, T, timestep): #start/stop/step
    #getStateOfCar() / localizar
    #compute dist_arco or dist_reta ang obtain cross track error
    
    x0 = car.x
    y0 = car.y
    x1 = pathObj.trajectoryPointsX[t]
    y1 = pathObj.trajectoryPointsX[t]
    
    d = computeEuclidianDistance(x0,y0,x1,y1)
    
    car.PID(error = d, dt = timestep)
    car.update(dt = timestep)
    
    
    env_map.add_data_to_plot(car.xArray, car.yArray, pause_time=0.1)
    time.sleep(0.1)
    pass
#end-for