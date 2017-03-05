from Cylinder import *
from random import random, sample

class Game:
    # Maximum random temperature to initialize the cylinders to
    TEMP_MAX = 1000

    # total: Total number of cylinders 
    # fastSize: Number of cylinders that can go in fast storage
    def __init__(self, total, fastSize):
        self.total = total
        self.fastSize = fastSize

        # Date for the current frame
        self.date = ""

        # List of cylinders
        self.cylinders = []

        # List of fast cylinders
        self.fastCylinders = []

        # Initialize Game with cylinders with random temperatures and locations
        self.__initRandomCylinders()

        # Set min and max temperatures
        self.maxTemp = 0
        self.minTemp = 0

        self.updateColors() 

        # Have the temperatures changed since the last updateColors call
        self.haveTempsChanged = False

    # Private methods for internal use

    # Updates max and min temperatures in the cylinders array
    def __updateMinMaxTemps(self):
        self.minTemp = self.maxTemp = self.cylinders[0].getTemperature()

        for cylinder in self.cylinders:
            temperature = cylinder.getTemperature()

            if temperature > self.maxTemp: 
                self.maxTemp = temperature
            elif temperature < self.minTemp:
                self.minTemp = temperature

    # Initializes the game with cylinders with ranodm temperatures and locations
    def __initRandomCylinders(self):
        # Initialize Cylinder objects
        for i in xrange(self.total):
            randTemp = random() * self.TEMP_MAX
            newCylinder = Cylinder(randTemp, Placement.SLOW)

            self.cylinders.append(newCylinder)

        # Pick random cylinders to be placed in fast storage
        moveToFast = sample(xrange(self.total), self.fastSize)

        for i in moveToFast:
            self.cylinders[i].setPlacement(Placement.FAST)
            self.fastCylinders.append(i)
            
    # Returns a number from {1,...,10} representing the color based on the temperature
    def __computeColorBucket(self, cylinder):
        # Get relative position of temperature in terms of range [0, 1]
        pos = float(cylinder.getTemperature() - self.minTemp) / (self.maxTemp - self.minTemp)

        return int(pos * 10) # Shift to range [0, 10]

    # Public Methods

    # Updates the color values of the cylinders
    def updateColors(self):
        self.__updateMinMaxTemps()

        for cylinder in self.cylinders:
            cylinder.setColorBucket(self.__computeColorBucket(cylinder))

    # Sets the date string
    def setDate(self, date):
        self.date = date

    # Gets the date string
    def getDate(self):
        return self.date

    # Swaps the placements of the cylinders in slow/fast storage
    # i.e. If the cylinder at cylinder1Index is fast and that at cylinder2Index
    # is slow, then cylinder1Index will be slow and cylinder2Index will be fast
    def swap(self, cyl1Index, cyl2Index):
        cyl1Plce = self.cylinders[cyl1Index].getPlacement()
        cyl2Plce = self.cylinders[cyl2Index].getPlacement()

        # Update fast cylinders list if 
        if cyl1Plce == Placement.SLOW and cyl2Plce == Placement.FAST:
            self.fastCylinders.remove(cyl2Index)
            self.fastCylinders.append(cyl1Index)
        elif cyl1Plce == Placement.FAST and cyl2Plce == Placement.SLOW:
            self.fastCylinders.remove(cyl1Index)
            self.fastCylinders.append(cyl2Index)

        self.cylinders[cyl1Index].setPlacement(cyl2Plce)
        self.cylinders[cyl2Index].setPlacement(cyl1Plce)

    # Sets the temperature of a cylinder at the given index
    def setTemperatureAt(self, index, temperature):
        self.cylinders[index].setTemperature(temperature)
        self.haveTempsChanged = True


    # Gets the color bucket of the cylinder at the given index
    def getColorAt(self, index):
        if self.haveTempsChanged:
            self.updateColors()
            self.haveTempsChanged = False

        return self.cylinders[index].getColorBucket()

    # Returns a list of all the cylinders
    def getCylinders(self):
        return self.cylinders;

    # Returns a list of the indices of the fast cylinders
    def getFastCylinderIndices(self):
        return self.fastCylinders

    # Returns a list of the indices of the slow cylinders
    def getSlowCylinderIndices(self):
        return [index for index in range(self.total) if index not in self.fastCylinders]

# Testing main method
if __name__ == "__main__":
    game = Game(10, 3)

    for cylinder in game.getCylinders():
        print str(cylinder)

    print "MaxTemp: " + str(game.maxTemp)
    print "MinTemp: " + str(game.minTemp)

    print "Fast cylinders: " + str(game.getFastCylinderIndices())
    print "Slow cylinders: " + str(game.getSlowCylinderIndices())

    print "\nSWAPPING PLACEMENTS OF INDICES 0 AND 1\n"
    game.swap(0, 1)

    for cylinder in game.getCylinders():
        print str(cylinder)

    print "Fast cylinders: " + str(game.getFastCylinderIndices())
    print "Slow cylinders: " + str(game.getSlowCylinderIndices())

    print "\nSetting cylinder at index 0's temperature to 9999"
    game.setTemperatureAt(0, 9999)

    print str(game.getCylinders()[0])

    print "Getting color of cylinder at index 0"
    print game.getColorAt(0)

    print str(game.getCylinders()[0])