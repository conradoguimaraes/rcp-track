# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 23:24:40 2024

@author: Conrado
"""

#%%
#Required Imports
import os
import time
import logging
import numpy as np
import traceback

from config import readConfig
from trajectory2D import trajectory2D
from envMap import envMap
from carModel import carModel


import utils.trajectoryFunctions as tf
from utils.logInit import initLogger



#%%
#Initialize the Logger
initLogger()



#%%
#Required Simulation inputs: 
config = readConfig(moduleName=__file__)

#simTime = 60
#timestep = 0.1
logging.info(f"Reading config '{__file__}'")
simTime = config["simTime"]
timestep = config["timestep"]

logging.info(f"simTime = {simTime}")
logging.info(f"timestep = {timestep}")


#%%
#Initialize the Path/Trajectory Object

#Init the Path Object with the desired trajectory config/parameters
#logger.info(f"Creating a path object with trajectory config '{desiredTrajectory}' ...")
pathObj = trajectory2D(trajectoryName = "trajectory_eightshape_v1")

#Build the Path segments
pathObj.eightShape(delta = np.pi/8)

#Fix the straight lines:
pathObj.fixEightShapeLineVectors()

#Build the trajectory
pathObj.buildEightShapeTrajectory()


#Horizontal:
# forcing an horizontal line (for tests)

number_points = len(np.arange(0, simTime+timestep, timestep))

line_x0, line_y0 = 0, 0
line_x1, line_y1 = 50, 2
pathObj.buildStraightLine(x0=line_x0, y0=line_y0, x1=line_x1, y1=line_y1, nr_points=number_points)

logging.info(f"Simulation Time: simTime={simTime}.")
logging.info(f"Timestep: timestep={timestep}.")
logging.info(f"Building StraightLine with {number_points} points.")




#%%
#Initialize the car object
car = carModel(x0 = 0, y0 = 0.1, v0 = 1.0,
               radius1  = 10,
               radius2 = 10)
car.Kp = 0.6
car.Ki = 0.11
car.Kd = 0.7



#%%
#Create the environment map object
env_map = envMap()

#Draw the eight shape path
title = f"simTime={simTime} | Kp={car.Kp} | Kp={car.Ki} | Kp={car.Kd}"
env_map.drawShape(pathObj, titleStr=title, blockPlot=False, maximized=True)








#%%
#Run the simulation:

arrayIndex = 0 #integer index counter to iterate along XY point arrays
t = 0.0 #float step counter (tk = t(k-1) + h, etc) (ex with h=0.1: t=[0.0, 0.1, 0.2, ...])

while t <= simTime:
    #getStateOfCar() / localizar
    #compute dist_arco or dist_reta ang obtain cross track error
    try:
        x0 = car.x
        y0 = car.y
        x1 = pathObj.trajectoryPointsX[arrayIndex]
        y1 = pathObj.trajectoryPointsY[arrayIndex]
        
        d, lambda1, lambda2, theta, Q = tf.distance2line(line_x0, line_y0,
                                                         line_x1, line_y1,
                                                         car.x, car.y)
        
        logging.info(f"Distance = {d}")
        logging.info(f"lambda-1 = {lambda1} | lambda-2 = {lambda2}")
        logging.info(f"Theta = {theta}")
        logging.info(f"Nearest Point on Track Q={Q}")
        
        if(lambda2 <= 0): d = d*(-1);
        curvature_value = 0
        
        #Compute PID
        car.PID(error = d, dt = timestep, curvature = curvature_value)
        
        #Update Car Kinematics
        car.update(dt = timestep)
        
        #Update Loop variables
        t += timestep
        arrayIndex += 1
        
        #Plot new Car position
        env_map.add_data_to_plot(car.xArray, car.yArray,
                                 pause_time = 0.025,
                                 plot_Suffix_title = " t = " + "{:.2f}".format(t))
        
        
        time.sleep(0.025)
        
    except KeyboardInterrupt:
        break
    except:
        logging.info(traceback.format_exc())
    #end-try-except
#end-for

logging.info("Saving plot snapshot ...")
env_map.savePlot(figureName="myresult.png")

input("________end of program________>")