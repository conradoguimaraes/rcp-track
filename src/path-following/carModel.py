import math
import numpy as np

import logging
logger = logging.getLogger()


class carModel:

    def __init__(self, x0 = None, y0 = None, \
                v0: float=0.0, theta0: float=0.0,\
                radius1 = 10, radius2 = 10):
        
        logging.info("Initializing the car model ...")
        
        #-----------------------------
        #Check if a initial position has been given:
        if (x0 is None):
            logging.info("x0 cannot be None type.")
            raise Exception("x0 cannot be None type.")
        #end-if-else
        
        if (y0 is None):
            logging.info("y0 cannot be None type.")
            raise Exception("y0 cannot be None type.")
        #end-if-else
        
        if (v0 <= 0):
            logging.info("v0 cannot be equal or smaller than 0.")
            raise Exception("v0 cannot be equal or smaller than 0.")
        #end-if-else
        
        #-----------------------------
        #Set Car initial position
        self.x = x0
        self.y = y0
        
        #-----------------------------
        #Set car initial velocity and steering angle
        self.v = v0
        self.th = theta0
        
        #-----------------------------
        #Car parameters in array format
        self.xArray  = np.array([])
        self.yArray  = np.array([])
        self.thArray = np.array([])
        self.vArray  = np.array([])
        
        #-----------------------------
        #Car curvature Radius:
        self.R1 = radius1
        self.R2 = radius2
        self.CarR = max(self.R1,self.R2)/2
       
        #Curvature (value, max and min values for saturation)
        self.c_max = 1/self.CarR
        self.c = self.c_max;
        self.c_min = -(self.c_max);
        
        
        self.curvature = 0 #given by 1/R1 or 1/R2 according to type of path segment
        #-----------------------------
        #PID:
        #u = (Kp*e) + error_i+(Ki*e*dt) + Kd*(e-e_previous)/dt
        
        self.Kp = 17
        self.Ki = 0.11
        self.Kd = 27.3

        
        self.error = 0
        self.error_abs = 0
        self.error_previous = 0
        
        self.error_p = 0
        self.error_i = 0
        self.error_d = 0
        
        #-----------------------------
        #Metrics
        self.total_error = 0
        self.errorArray = np.array([])
        self.errorArrayAbs = np.array([])
        
        self.control_effort = 0
        self.controlEffort_array = np.array([])
    #end-def
    
    
    
    def update(self, dt=0.01):
        logging.info("Updating Car Model ...")
        logging.info(f"Control value c={self.c}")
        
        if (self.c > self.c_max):
            logging.info(f"Computed control value above threshold c_max={self.c_max}.")
            self.c = self.c_max
        elif (self.c < self.c_min):
            logging.info(f"Computed control value below threshold c_min={self.c_min}.")
            self.c = self.c_min
        else:
            pass
        #end-if-else
        
        #Compute Car Kinematic Model (radians):
        dx  = self.v * math.cos(self.th);
        dy  = self.v * math.sin(self.th);
        dth = self.v * self.c;
        
        
        logging.info(f"Previous Car position: (x={self.x}, y={self.y}).")
 
        logging.info(f"Previous Car velocity: v={self.v}.")
        logging.info(f"Previous Car steering angle: theta={self.th}.")
        
        #Update position XY and steering angle
        self.x  +=  dx * dt;
        self.y  +=  dy * dt;
        self.th += dth * dt;
        
        logging.info(f"New Car position: (x={self.x}, y={self.y})")
        logging.info(f"New Car velocity: v={self.v}.")
        logging.info(f"New Car steering angle: theta={self.th}")
        
        
        #Add to the arrays
        self.xArray  = np.append(self.xArray,   self.x)
        self.yArray  = np.append(self.yArray,   self.y)
        self.thArray = np.append(self.thArray, self.th)
        self.vArray  = np.append(self.vArray,   self.v)
    #end-def
    
    
    def PID(self, error, dt, curvature):
        #error is the crosstrack_error
        logging.info("Running PID ...")
        
        self.error = error
        self.error_abs = abs(error)
        logging.info(f"cross track error = {self.error}")
        
        #Compute Errors:
        self.error_p = error
        self.error_i = self.error_i + (error * dt)
        self.error_d = (error - self.error_previous) / dt
        
        logging.info(f"error_p = {self.error_p}")
        logging.info(f"error_i = {self.error_i}")
        logging.info(f"error_d = {self.error_d}")
        
        #Compute control:
        self.c = (self.Kp*error + self.Ki*self.error_i + self.Kd*self.error_d) + self.curvature;
        logging.info(f"computed control c = {self.c}")
        
        #Save error, and append errors and control effort to arrays:
        self.error_previous = self.error #save current error to be used on next iteration
        
        self.total_error += self.error #total accumulated error
        self.errorArray = np.append(self.errorArray, self.error) #error on each iteration
        self.errorArrayAbs = np.append(self.errorArrayAbs, self.error_abs)
        
        self.controlEffort_array = np.append(self.controlEffort_array, self.c) #control effort on each iteration
                
        logging.info(f"Current Total Sum of cross track error = {self.total_error}")
    #end-def
    
    def computeControlEffort(self) -> float:
        #Control Effort computed as U = (u0)^2 + (u1)^2 + ... + (uk)^2
        logging.info("Computing total control effort 'U = (u0)^2 + (u1)^2 + ... + (uk)^2'")
        
        #Square each element of the array:
        arraySquared = self.controlEffort_array**2
        
        #Sum:
        self.control_effort = np.sum(arraySquared)
        
        logging.info(f"Total control effort U = {self.control_effort}")
        return self.control_effort
    #end-def

#end-class


if __name__ == "__main__":
    print(f"Running {__file__} ...")
    
    car = carModel(x0 = 10, y0 = 20)
#end-if-else
    