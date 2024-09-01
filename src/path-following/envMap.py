import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from config import readConfig
from trajectory2D import trajectory2D




class envMap():
    def __init__(self) -> None:
        self.config = readConfig(moduleName="environmentMap")
        
    #end-def
    
    
    def drawEightShape(self, pathObject):        
        if (isinstance(pathObject, trajectory2D) is False): 
            raise Exception(f"{pathObject} is not a trajectory2D object.")
        #end-if-else
        
        
        #Get Plot Config from file
        config = readConfig(moduleName = "plots_1")
        
        
        #Matlab implementation:
        # plot(Xarc1,Yarc1,'-k', Xarc2,Yarc2,'-k', ...
        #     X_reta1,Y_reta1,'-k', X_reta2,Y_reta2,'-k')
                
        Xdata = [pathObject.eightShapePathLines["X_line1"],
                 pathObject.eightShapePathLines["X_line2"],
                 pathObject.eightShapePathSegments['Xarc1'],
                 pathObject.eightShapePathSegments['Xarc2']]
        
        Ydata = [pathObject.eightShapePathLines["Y_line1"],
                 pathObject.eightShapePathLines["Y_line2"],
                 pathObject.eightShapePathSegments['Yarc1'],
                 pathObject.eightShapePathSegments['Yarc2']]
        
        print(config["color"])
        
        plotRows, plotColumns = 1, 2
        self.fig1, (self.ax1, self.ax2) = plt.subplots(nrows=plotRows, ncols=plotColumns,
                                                       gridspec_kw={'width_ratios':[2,1]})
        for X, Y in zip(Xdata, Ydata):
            self.ax1.plot(X, Y,
                          color=config["color"],
                          ls=config["lineStyle"],
                          linewidth=config["lineWidth"])
        #end-for
        
        self.ax1.grid()
        self.ax2.grid()
        
        plt.savefig("")
        plt.show()
    #end-def
    
    
    
    def showTestPlot(self):
        X = np.linspace(0, 2*np.pi, 100)
        Y = np.cos(X)
        
        fig, ax = plt.subplots()
        ax.plot(X,Y, color='blue')
        
        plt.savefig("test_figure.pdf")
        plt.show()
    #end-def
    
#end-class

if __name__ == "__main__":
    pass
#end-if-else