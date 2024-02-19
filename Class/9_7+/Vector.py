import math
class Vector:
	def __init__(self, p1, p2):
		self.x = p1
		self.y = p2
#Vector.__init__(v1, 3, 4)
# v1.__init__(3, 4)
	def magnitude(self):
		return (self.x**2 + self.y**2) ** (1/2)

class PolarVector(Vector): #inherits last class !

	def angle(self):
		return math.atan(self.y/self.x) * 180/math.pi

v1 = Vector(3,4)# calls Vector.__init__() with v1
v2 = Vector(4,5)

assert v1.x == 3# calls Vector.__init() with v1
assert v1.y == 4

assert v1.magnitude() == 5

#dir(list)

p1 = PolarVector(2,2)
assert p1.angle() == 45
