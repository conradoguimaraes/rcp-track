from config import readConfig

class carModel:
    def __init__(self, kinematicModelNr: int= 1, carModelConfig: str = "carModel_1") -> None:
        config = readConfig(moduleName = carModelConfig)
        
        #Desired Kinematic Model
        self.kinematicModel = kinematicModelNr
        
        #vehicle position
        self.x = config["x0"]
        self.y = config["y0"]
        
        #vehicle velocity
        self.v = config["v"]
        
        #Set the start heading angle
        self.theta = config["theta0"]
        
        #Radius:
        self.R1 = config["radiusR1"]
        self.R2 = config["radiusR2"]
        self.CarR = max(self.R1,self.R2)/2
       
        #Curvature (value, max and min values for saturation)
        self.c_max = 1/self.CarR
        self.c = self.c_max;
        self.c_min = -(self.c_max);
        
        
        #cross-track error
        self.d = config["startCrossTrackError"]
        
        return
    #end-def
    
    def update(self):
        #If R1 and R2 were changed, compute again the Radius and Curvature
        self.CarR = max(self.R1,self.R2)/2
        
        self.c_max = 1/self.CarR
        self.c = self.c_max;
        self.c_min = -(self.c_max);
    #end-def
        

#end-class


if __name__ == "__main__":
    pass
#end-if-else
    