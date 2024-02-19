class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.z = (self.x ** 2 + self.y ** 2) ** .5
	
	def __eq__(self, other):
		if (self.x == other.x and self.y == other.y):
                        return True
		else:
			return self.z == other.z

	def __lt__(self, other):
		return self.z < other.z

	def __gt__(self, other):
                return self.z > other.z

	def dist_from_origin(self):
		return self.z

	def __str__(self):
		s = 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
		return s

if __name__== '__main__':
	p1 = Point(3, 4)
	p2 = Point(3, 4)
	p3 = Point(5, 12)
	p4 = Point(4, 3)
	s1 = 'Point(3, 4)'
	s2 = 'test'
	d1 = 5.0

	assert p1 == p2
	assert not p1 == p3
	assert p1 == p4
	assert not p3 == p1
	assert p1 < p3
	assert not p1 < p2
	assert p3 > p1
	assert not p1 > p2
	assert p1.dist_from_origin() == 5.0
	assert not p1.dist_from_origin() == 6.0
	assert s1 == str(p1)
	assert not s2 == str(p1)
