#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def neighbours(point):
	x = point[0]
	y = point[1]
	
	res = [(x, y) for (x, y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= x < dim_x and 0 <= y < dim_y]
	
	return res

def part1(data):
	risk_level = []
	for i in range(dim_x):
		for j in range(dim_y):
			bigger = 0
			hood = neighbours((i,j))
			for n in hood:
				if data[i][j] < data[n[0]][n[1]]:
					bigger += 1

			if bigger == len(hood):
				risk_level.append(data[i][j] + 1)

	return sum(risk_level)
							
def basin(point, current_basin):
	"""recurse through neighbours and add them to current basin if qualify and if they are not already in another one"""
	x = point[0]
	y = point[1]
	for n in neighbours((point[0], point[1])):
		neighbour_x = n[0]
		neighbour_y = n[1]
		if not basin_points[neighbour_x][neighbour_y] and data[neighbour_x][neighbour_y] != 9:
			basin_points[neighbour_x][neighbour_y] = True
			current_basin = basin((neighbour_x, neighbour_y), current_basin + [(neighbour_x, neighbour_y)])
	
	return current_basin

def part2(data):
	for i in range(dim_x):
		for j in range(dim_y):
			if not basin_points[i][j] and data[i][j] != 9:
				basin_points[i][j] = True
				basins.append(basin((i, j), [(i,j)]))
	# multiply length of three biggest basins
	res = 1
	for x in sorted([len(b) for b in basins])[-3:]:
		res = res * x

	return res
				
										
if not options.filename:
	parser.error("Filename not given")
else:
	try:
		start_time = time()
		with open(options.filename, 'r') as f:
			data = [[int(j) for j in list(i.strip())] for i in f.read().splitlines()]
			dim_x = len(data)
			dim_y = len(data[0])

			print(part1(data))
			# keep track which points are in a basin
			basin_points = [[False] * dim_y for i in range(dim_x)]
			# the resulting list of basins
			basins = []
			print(part2(data))					
		print("*** Run time: {} ms".format(int((time() - start_time) * 1000)))
	except FileNotFoundError as e:
		print(e)
