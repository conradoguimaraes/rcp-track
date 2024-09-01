from config import readConfig
import numpy as np

class trajectory2D():
    def __init__(self, trajectoryName: str = "") -> None:
        """_summary_

        Args:
            trajectoryName (str): Defaults to "".
                Desired trajectoryName (must be defined in the config.yml file)

        Raises:
            Exception: when trajectoryName is empty
        
        """
        if (trajectoryName == ""): raise Exception("[ERROR] You must provide the desired trajectory name.")
        
        #Load the desired trajectory Config
        self.config = readConfig(moduleName = trajectoryName)
        
        
        self.myVarsList = {}
        
    #end-def
    
    
    def add2varsList(self, varsList: list=[], fname: str=""):
        self.myVarsList[fname] = []
        for element in varsList: self.myVarsList[fname].append(element)
        return
    #end-def
    
    def displayVarsList(self):
        print(self.myVarsList)
        return
    #end-def
    
    def eightShape(self, delta: float=np.pi/8) -> None:
        """
        Build the eightShape path segments

        Args:
            delta (float): Defaults to pi/8.
                Parameter used to adjust (more smooth/steep) the transition between the straight lines and arcs.
                Is used when the 'eval' function is called.
        """
        self.eightShapePathSegments = {}
        self.eightShapePathJointPoints = {}
        self.eightShapePathLines = {}
        
        
        self.eightShapeParams = {'c1x': self.config["c1x"],
                                 'c1y': self.config["c1y"],
                                 'c2x': self.config["c2x"],
                                 'c2y': self.config["c2y"],
                                 'R1': self.config["R1"],
                                 'R2': self.config["R2"],
                                 'theta1': np.arange(start= eval(self.config["theta1_limInf"]),
                                                     stop = eval(self.config["theta1_limSup"]),
                                                     step = self.config["arrayStep"]),
                                 'theta2': np.arange(start= eval(self.config["theta2_limInf"]),
                                                     stop = eval(self.config["theta2_limSup"]),
                                                     step = self.config["arrayStep"])
                                }
        
        
        #-------------------------------
        #Build the Arc Path Segments
        
        Xarc1 = self.eightShapeParams["c1x"] + self.eightShapeParams["R1"]*np.cos(self.eightShapeParams["theta1"]);
        Yarc1 = self.eightShapeParams["c1y"] + self.eightShapeParams["R1"]*np.sin(self.eightShapeParams["theta1"]);
        
        self.eightShapeArcs['Xarc1'] = Xarc1
        self.eightShapeArcs['Yarc1'] = Yarc1
        
        
        Xarc2 = self.eightShapeParams["c2x"] + self.eightShapeParams["R2"]*np.cos(self.eightShapeParams["theta2"]);
        Yarc2 = self.eightShapeParams["c2y"] + self.eightShapeParams["R2"]*np.sin(self.eightShapeParams["theta2"]);
        
        self.eightShapeArcs['Xarc2'] = Xarc2
        self.eightShapeArcs['Yarc2'] = Yarc2
        
        #Matlab equivalent:
        #Xarc1 = Cx1 + R1*cos(theta1);
        #Yarc1 = Cy1 + R1*sin(theta1);

        #Xarc2 = Cx2 + R2*cos(theta2);
        #Yarc2 = Cy2 + R2*sin(theta2);

        
        #-------------------------------
        #Set the Path Points (where transition between straight lines and arcs occur)
        Dx1 = Xarc1[len(Xarc1)-1]
        Dy1 = Yarc1[len(Yarc1)-1]

        Dx2 = Xarc1[0]
        Dy2 = Yarc1[0]

        Ex1 = Xarc2[0]
        Ey1 = Yarc2[0]

        Ex2 = Xarc2[len(Xarc2)-1];
        Ey2 = Yarc2[len(Yarc2)-1];

        self.eightShapePathJointPoints["Dx1"] = Dx1
        self.eightShapePathJointPoints["Dy1"] = Dy1
        
        self.eightShapePathJointPoints["Dx2"] = Dx2
        self.eightShapePathJointPoints["Dy2"] = Dy2
        
        self.eightShapePathJointPoints["Ex1"] = Ex1
        self.eightShapePathJointPoints["Ey1"] = Ey1
        
        self.eightShapePathJointPoints["Ex2"] = Ex2
        self.eightShapePathJointPoints["Ey2"] = Ey2
        
        #-------------------------------
        #Build the Straight Lines Path Segments
        X_line1= [Dx1, Ex2];
        Y_line1= [Dy1, Ey2];
        
        X_line2= [Dx2, Ex1];
        Y_line2= [Dy2, Ey1];
        
        self.eightShapePathLines["X_line1"] = X_line1
        self.eightShapePathLines["Y_line1"] = Y_line1
        
        self.eightShapePathLines["X_line2"] = X_line2
        self.eightShapePathLines["Y_line2"] = Y_line2
        
        
        #-------------------------------
        usedVarsList = ["eightShapeArcs", 
                        "eightShapePathJointPoints", 
                        "eightShapePathLines", 
                        "eightShapeParams"]
        self.add2varsList(varsList = usedVarsList, fname = "eightShape")
        
        return
    #end-def


    def fixEightShapeLineVectors(self) -> None:
        """
            Fix the straight lines: make arrays with just the starting and ending points.
            Example:
                X_line1= [Dx1, Ex2] is a list with 2 points
                line1Xvector = np.linspace(X_line1[0], X_line1[1], nrPoints) is an array with nrPoints
            
            This is required because the Arcs were initially created with nrPoints. Thus, this makes
            the straight lines have the same nrPoints.
        """
        
        #Matlab implementation:
        # reta1Xvector = linspace(X_reta1(1), X_reta1(2), length(Xarc2)/2);
        # reta1Yvector = linspace(Y_reta1(1), Y_reta1(2), length(Xarc2)/2);

        # reta2Xvector = linspace(X_reta2(1), X_reta2(2), length(Xarc2));
        # reta2Yvector = linspace(Y_reta2(1), Y_reta2(2), length(Xarc2));
        
        self.eightShapePathLineVectors = {}
        
        
        length = round(len(self.eightShapePathSegments['Xarc2']) / 2)
        
        #-------------------------------
        
        X_line1 = self.eightShapePathLines["X_line1"]
        Y_line1 = self.eightShapePathLines["Y_line1"]
        
        X_line2 = self.eightShapePathLines["X_line2"]
        Y_line2 = self.eightShapePathLines["Y_line2"]
        
        #-------------------------------
        
        line1Xvector = np.linspace(X_line1[0], X_line1[1], length)
        line1Yvector = np.linspace(Y_line1[0], Y_line1[1], length)
        
        line2Xvector = np.linspace(X_line2[0], X_line2[1], length)
        line2Yvector = np.linspace(Y_line2[0], Y_line2[1], length)
        
        #-------------------------------
        self.eightShapePathLineVectors["line1Xvector"] = line1Xvector
        self.eightShapePathLineVectors["line1Yvector"] = line1Yvector
        
        self.eightShapePathLineVectors["line2Xvector"] = line2Xvector
        self.eightShapePathLineVectors["line2Yvector"] = line2Yvector
        
        #-------------------------------
        usedVarsList = ["eightShapePathLineVectors"]
        self.add2varsList(varsList = usedVarsList, fname = "fixEightShapeLineVectors")
        
        
        return
    #end-def
    
    
    def buildEightShapeSinglePointsVector(self) -> None:
        """
            Build single Arrays of X and Y points of the Eight Shape trajectory:
            line1 -> Arc2 -> line2, Arc1
        """
        #Matlab implementation:
        #PontosX = [reta1Xvector, flip(Xarc2), flip(reta2Xvector), Xarc1];
        #PontosY = [reta1Yvector, flip(Yarc2), flip(reta2Yvector), Yarc1];
        
        
        self.trajectoryPointsX = np.concatenate((self.eightShapePathLineVectors["line1Xvector"],
                                                 np.flip(self.eightShapeArcs['Xarc2']),
                                                 np.flip(self.eightShapePathLineVectors["line1Xvector"]),
                                                 self.eightShapeArcs['Xarc1']))
        
        self.trajectoryPointsY = np.concatenate((self.eightShapePathLineVectors["line1Yvector"],
                                                 np.flip(self.eightShapeArcs['Yarc2']),
                                                 np.flip(self.eightShapePathLineVectors["line2Yvector"]),
                                                 self.eightShapeArcs['Yarc1']))
        
        #-------------------------------
        usedVarsList = ["trajectoryPointsX", "trajectoryPointsY"]
        self.add2varsList(varsList = usedVarsList, fname = "buildEightShapeSinglePointsVector")
        
        return
    #end-def
#end-class




if __name__ == "__main__":
    #from numpy import pi
    #from trajectory2D import trajectory2D

    #Init the Path Object with the desired trajectory config/parameters
    path = trajectory2D(trajectoryName = "trajectory_eightshape_v1")

    #Build the Path segments
    path.eightShape(delta = np.pi/8)
#end-if-else