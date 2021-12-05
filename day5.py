#!/usr/bin/env python3
from optparse import OptionParser
from enum import Enum, IntEnum, auto

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

class KindOfLine(Enum):
	HORIZONTAL = auto()
	VERTICAL = auto()
	DIAGONAL = auto()

class Orientation(IntEnum):
	UP = 1
	DOWN = -1
	UNDECIDED = 0
		
class Point:
	def __init__(self, point):
		self._x = point[0]
		self._y = point[1]
	
	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y
		
	def __repr__(self):
		return "(x: {}, y: {})".format(self._x, self._y)
	
class Line:
	def __init__(self, coordinates):
		coordinates = coordinates.split('->')
		coordinates = [[int(y) for y in x.strip().split(',')] for x in coordinates]
		
		self.startpoint = Point(coordinates[0])
		self.endpoint = Point(coordinates[1])
	
	def kind(self):
		if self.startpoint.x == self.endpoint.x:
			return KindOfLine.VERTICAL
		elif self.startpoint.y == self.endpoint.y:
			return KindOfLine.HORIZONTAL
		else:
			return KindOfLine.DIAGONAL
			
	def orientation(self):
		if self.kind() == KindOfLine.HORIZONTAL:
			return Orientation.UP if self.startpoint.x < self.endpoint.x else Orientation.DOWN
		elif self.kind() == KindOfLine.VERTICAL:
			return Orientation.UP if self.startpoint.y < self.endpoint.y else Orientation.DOWN
		else:
			return Orientation.UNDECIDED
	
	def x_orientation(self):
		if self.startpoint.x > self.endpoint.x:
			return Orientation.DOWN
		else:
			return Orientation.UP

	def y_orientation(self):
		if self.startpoint.y > self.endpoint.y:
			return Orientation.DOWN
		else:
			return Orientation.UP

	def max_coordinate_value(self):
		return max(self.startpoint.x, self.startpoint.y, self.endpoint.x, self.endpoint.y)

	def covered_points_part1(self):
		if self.kind() == KindOfLine.HORIZONTAL:
			res = [Point((x, self.startpoint.y)) for x in range(self.startpoint.x, self.endpoint.x, self.orientation())]
			res.append(self.endpoint)
		elif self.kind() == KindOfLine.VERTICAL:
			res = [Point((self.startpoint.x, y)) for y in range(self.startpoint.y, self.endpoint.y, self.orientation())]
			res.append(self.endpoint)
		else:
			res = []
			
		return res

	def compare(self, x1, x2):
		if self.x_orientation() == Orientation.UP:
			return x1 <= x2
		else:
			return x1 >= x2
		

	def covered_points_part2(self):
		if self.kind() == KindOfLine.HORIZONTAL:
			res = [Point((x, self.startpoint.y)) for x in range(self.startpoint.x, self.endpoint.x, self.orientation())]
			res.append(self.endpoint)
		elif self.kind() == KindOfLine.VERTICAL:
			res = [Point((self.startpoint.x, y)) for y in range(self.startpoint.y, self.endpoint.y, self.orientation())]
			res.append(self.endpoint)
		else:
			res = []			
			x = self.startpoint.x
			y = self.startpoint.y
			while self.compare(x, self.endpoint.x):
				res.append(Point([x, y]))
				x = x + self.x_orientation()
				y = y + self.y_orientation()
		return res

if not options.filename:
    parser.error('Filename not given')
else:
	try:
		with open(options.filename, 'r') as f:
			lines_of_vents = [ Line(x) for x in f.read().splitlines()]
			size = max([l.max_coordinate_value() for l in lines_of_vents]) + 1
			# part 1
			vent_plot = [[0] * size for i in range(size)]
			for line in lines_of_vents:
				for point in line.covered_points_part1():
					vent_plot[point.y][point.x] += 1
			danger = 0
			for line in vent_plot:
				danger += len([x for x in line if x > 1])
			print(danger)
			
			# part 2
			vent_plot = [[0] * size for i in range(size)]
			for line in lines_of_vents:
				for point in line.covered_points_part2():
					vent_plot[point.y][point.x] += 1
			danger = 0
			for line in vent_plot:
				danger += len([x for x in line if x > 1])
			print(danger)						
	except FileNotFoundError as e:
		print(e)
