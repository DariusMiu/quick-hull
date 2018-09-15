class Point:
	def __init__(self, X, Y, color):
		self.X = X
		self.Y = Y
		self.color = color
	#
	def getArray(self):
		return [self.X, self.Y]
	#
	def __str__(self):
		return "{X:" + str(self.X) + " Y:" + str(self.Y) + "}"
#