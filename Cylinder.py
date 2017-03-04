class Placement():
	FAST = 1 
	SLOW = 2 
	NONE = 2 

class Cylinder:
	def __init__(self, temperature, placement = Placement.NONE):
		self.temperature = temperature
		self.placement = placement
		self.bucket = -1

	def getTemperature(self):
		return self.temperature

	def setTemperature(self, temperature):
		self.temperature = temperature

	# Takes in number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red
	def setColorBucket(self, bucket):
		self.bucket = bucket

	# Returns number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red
	def getColorBucket(self):
		return self.bucket

	def getPlacement(self):
		return self.placement

	def setPlacement(self, placement):
		self.placement = placement

if __name__ == "__main__":
	cyl1 = Cylinder(30)
	print "Temperature: " + str(cyl1.getTemperature())
	print "Placement: " + str(cyl1.getPlacement())

	cyl1.setPlacement(Placement.FAST)
	cyl1.setColorBucket(9)

	print "Placement: " + str(cyl1.getPlacement())
	print "Color Bucket: " + str(cyl1.getColorBucket())
