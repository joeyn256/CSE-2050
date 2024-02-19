# command type() returns the type of the object
# yield returns commands
# for vectors you can define them using tuples so
u = (3, 4)
v = (3, 6)
def add(a, b):
	return (a[0] + b[0], a[1] + b[1])
def subtract(a,b):
	return (a[0] - b[0], a[1] - b[1])
def dot(a, b):
	return (a[0] * b[0] + a[1] * b[1])
def norm(a):
	return (a[0] * a[0] + a[1] * a[1]) ** .5
def isvertical(a):
	return a[0] == 0
print(add(u,v))

#suppose we want to make sure that the inputs to these functions really are tuples that contain two numbers

class Vector:
	def __init__(self, x, y):#checks input, you can access the attributes and methods of the class with self init function is the intializer the two underscore are called magic methods or dundr methods
		self.x = x
		self.y = y
	def norm(self_):
		return (self.x ** 2 + self.y ** 2) ** .5
u = Vector(3,4)
print(u.norm())
print(Vector(5,12).norm())
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def norm(self):
		return (self.x ** 2 + self.y ** 2) ** .5
	
	def __add__(self, other):
		newx = self.x + other.x
		newy = self.y + other.y
		return VEctor(newx, newy)
u = Vector(3,4)
v = Vector(3,6)
print (u + v)
# returns __main__.Vector object at 0x10db7bcd0
# can add a str method to read vectors say def __str__(self):
# return "(%f, %f)" %(self.x, self.y)
#anything with an underscore is considered private in python but you can read it (even though you shouldn't just because python doesn't differentiate between public and private
# inheritance class Triangle then could be class Triangle(Polygon)
#use DRY dont repeat yourself you dont want to have a bug then make a superclass with that bug and have two bugs; put code in a supercode
#Python lets us have a class that stores anything
