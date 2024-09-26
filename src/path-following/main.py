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
simTime = 60
timestep = 0.1
number_points = len(np.arange(0, simTime+timestep, timestep))
pathObj.buildHorizontalLine(x0=0, x1=50, y0=0, nr_points=number_points)


logging.info(f"Simulation Time: simTime={simTime}.")
logging.info(f"Timestep: timestep={timestep}.")
logging.info(f"Building StraightLine with {number_points} points.")




#%%

from envMap import envMap

#Create the environment map object
env_map = envMap()

#Draw the eight shape path
env_map.drawShape(pathObj, blockPlot=False, maximized=False)




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
from utils.trajectoryFunctions import *
import traceback

#T = 100 #Simulation time
#timestep = 0.1 #Timestep


#T = len(pathObj.trajectoryPointsX)



#Initialize the car object
car = carModel(x0 = 0, y0 = 0.1, v0 = 1.0,
               radius1  = 10,
               radius2 = 10)
car.Kp = 0.6
car.Ki = 0.11
car.Kd = 0.7





arrayIndex = 0
#for t in range(0, T, timestep): #start/stop/step
t = 0
while t <= simTime:
    #getStateOfCar() / localizar
    #compute dist_arco or dist_reta ang obtain cross track error
    try:
        x0 = car.x
        y0 = car.y
        x1 = pathObj.trajectoryPointsX[arrayIndex]
        y1 = pathObj.trajectoryPointsY[arrayIndex]
        
        d = computeEuclidianDistance(x0,y0,x1,y1)
        if (y1 < car.y):
            d = d*(-1)
        else:
            pass
        #end-if-else
        logging.info(f"Distance = {d}")
        
        car.PID(error = d, dt = timestep, curvature=0)
        car.update(dt = timestep)
        
        
        env_map.add_data_to_plot(car.xArray, car.yArray, pause_time=0.025)
        
        t += timestep
        arrayIndex += 1
        time.sleep(0.025)
        
    except KeyboardInterrupt:
        break
    except:
        logging.info(traceback.format_exc())
    #end-try-except
#end-for