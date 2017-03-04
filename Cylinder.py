from enum import enum

class Placement(Enum):
	FAST = auto()
	SLOW = auto()
	NONE = auto()

class Cylinder:
	def __init__(self, temperature, placement = Placement.NONE):
		self.temperature = temperature
		self.placement = placement
		self.bucket = 0

	def getTemperature(self):
		return self.temperature

	def setTemperature(self, temperature):
		self.temperature = temperature

	'''Takes in number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red'''
	def setColorBucket(self, bucket):
		self.bucket = bucket

	'''Returns number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red'''
    def getColorBucket(self, bucket):
    	return self.bucket

	def getPlacement(self):
		return self.placement

	def setPlacement(self, placement):
		self.placement = placement

