# Enumeration class for the storage location of the Cylinders
class Placement():
	FAST = 1 
	SLOW = 2 
	NONE = 2 

# Cylinder class storing data of a cylinder; different from UICylinder handling UI representation
class Cylinder:
	def __init__(self, temperature, placement = Placement.NONE):
		self.temperature = temperature
		self.placement = placement
		self.bucket = -1

	# Gets the current temperature of this Cylinder
	def getTemperature(self):
		return self.temperature

	# Sets the current temperature of this Cylinder
	def setTemperature(self, temperature):
		self.temperature = temperature

	# Takes in number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red
	# Called by Game class
	def setColorBucket(self, bucket):
		self.bucket = bucket

	# Returns number 1 to 10 representing color. 1 is strongest Blue, 10 is strongest Red
	# Called by UICylinder class
	def getColorBucket(self):
		return self.bucket

	# Returns the current storage location of this cylinder
	def getPlacement(self):
		return self.placement

	# Sets the storage location of this cylinder
	def setPlacement(self, placement):
		self.placement = placement

# Tester method
if __name__ == "__main__":
	cyl1 = Cylinder(30)
	print "Temperature: " + str(cyl1.getTemperature())
	print "Placement: " + str(cyl1.getPlacement())

	cyl1.setPlacement(Placement.FAST)
	cyl1.setColorBucket(9)

	print "Placement: " + str(cyl1.getPlacement())
	print "Color Bucket: " + str(cyl1.getColorBucket())
