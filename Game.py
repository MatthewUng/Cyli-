
# TODO: everything
class Game:
    cylinders = []

    """total: total number of cylinders 
    fast_size: size of fast portion"""
    def __init__(self, total, fast_size):
        self.maxTemp = 0
        self.minTemp = 0

        __setMinMaxTemps() 
        pass

    # Private methods for internal use
    def __setMinMaxTemps(self):
     '''   for cylinder in cylinders:
            if cylinder.getTemperature()>self.maxTemp:
                self.maxTemp=cylinder.getTemperature()
                pass
            pass
        for cylinder in cylinders:
            if cylinder.getTemperature()<self.minTemp:
                self.minTemp=cylinder.getTemperature()
                pass
            pass'''
        pass

    def __initRandomCylinders(self):
        pass

    # Public Methods
    def swap(self, i, j):
        """swapping rectangle i with rectangle j"""
        pass

    def change_color(self, i, color):
        """color is... something"""

    def get_states(self, i):
        """returns: array of numbers"""
        pass

    def get_fast_states(self):
        """returns: array of numbers"""
        pass

    def get_slow_states(self):
        """returns: array of numbers"""
        pass

    def fitness(self):
        """returns number 0.0 - 1.0"""
        pass
    def bucket(self,cylinder):
        bucket=math.floor((cylinder.getTemperature()-minTemp)/(maxTemp-minTemp))
        pass
    def updateMax(self,cylinder):
        if cylinder.getTemperature()>self.maxTemp:
                self.maxTemp=cylinder.getTemperature()
                pass
        pass
    def updateMin(self,cylinder):
        if cylinder.getTemperature()<self.minTemp:
                self.minTemp=cylinder.getTemperature()
                pass
        pass