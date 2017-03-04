
# TODO: everything
class Game:
    def __init__(self, total, fast_size):
        for cylinder in cylinders:
            if cylinder.getTemperature()>self.maxTemp:
                self.maxTemp=cylinder.getTemperature()
                pass
            pass
        for cylinder in cylinders:
            if cylinder.getTemperature()<self.minTemp:
                self.minTemp=cylinder.getTemperature()
                pass
            pass
        """total: total number of cylinders
           fast_size: size of fast portion"""
        pass

    def swap(self, i, j):
        """swapping rectangle i with rectangle j"""
        pass

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