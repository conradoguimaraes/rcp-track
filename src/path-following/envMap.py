import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from config import readConfig
from trajectory2D import trajectory2D



import logging
logger = logging.getLogger()

class envMap():
    def __init__(self) -> None:
        self.config = readConfig(moduleName="environmentMap")
        
    #end-def
    
    
    def drawShape(self, pathObject, plot_style_config = "plots_1", blockPlot = False):
        """drawShape given a pathObject with X and Y points

        Args:
            pathObject (_type_): path object, created in trajectory2D
            plot_style_config (str, optional): config name with plot parameters (e.g., color). Defaults to "plots_1".

        Raises:
            Exception: when path object is not a trajectory2D object
        """        
        if (isinstance(pathObject, trajectory2D) is False): 
            raise Exception(f"{pathObject} is not a trajectory2D object.")
        #end-if-else
        
        #-------------------------------
        #Get Plot Config from file
        logging.info("Reading plot_style_config file '{plot_style_config}' ...")
        plotConfig = readConfig(moduleName = plot_style_config)
        
        #-------------------------------
        #Numpy arrays with the data points
        Xdata = pathObject.trajectoryPointsX
        Ydata = pathObject.trajectoryPointsY
        
        logging.info(f"Xdata datatype {type(Xdata)}")
        logging.info(f"Ydata datatype {type(Ydata)}")
        
        
        #-------------------------------
        logging.info("Building subplots ...")
        plotRows, plotColumns = plotConfig["plotRows"], plotConfig["plotColumns"]
        self.fig1, (self.ax1, self.ax2) = plt.subplots(nrows=plotRows, ncols=plotColumns,
                                                       gridspec_kw={'width_ratios':[2,1]})
   
        self.ax1.plot(Xdata, Ydata,
                      color=plotConfig["color"],
                      ls=plotConfig["lineStyle"],
                      linewidth=plotConfig["lineWidth"])
        
        self.ax1.grid()
        self.ax2.grid()
        
        #-------------------------------
        logging.info("Maximizing plot window ...")
        #manager = plt.get_current_fig_manager()
        #manager.full_screen_toggle()
        #manager.window.showMaximized()
        #figHandler = plt.gcf()
        #figHandler.show()
        plt.show(block = blockPlot)
        #-------------------------------
        #logging.info("Saving plot figure ...")
        #self.plt.savefig("drawShape_figure.png")
        #-------------------------------
    #end-def
    
    def add_data_to_plot(self, new_Xdata, new_Ydata, plot_style_config="plots_1", plotPoint = False, pause_time=0.1):
        #Add new data points to the left subplot (self.ax1) in real-time
        if self.ax1 is None: raise Exception("The plot has not been initialized. Call drawShape first.")
        
        # Get Plot Config from file (if needed)
        #logging.info(f"Reading plot_style_config file '{plot_style_config}' ...")
        #plotConfig = readConfig(moduleName=plot_style_config)

        # Plot new data points
        if (plotPoint):
            self.ax1.plot(new_Xdata, new_Ydata,
                        color="red",
                        marker='o',
                        ls='None',  # No line, since it's a single point (or points)
                        linewidth=2)
        else:  
            self.ax1.plot(new_Xdata, new_Ydata,
                          color="red",  # Default color if not specified
                          ls=":",    # Default line style
                          linewidth=2)  # Default line width
        #end-if-else
        
        # Redraw the plot and pause to allow real-time updates
        plt.draw()
        plt.pause(pause_time)  # Pause to update the plot in real-time
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