#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def neighbours(point, dim_x, dim_y):
	x = point[0]
	y = point[1]
	
	res = [(x, y) for (x, y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= x < dim_x and 0 <= y < dim_y]
	
	return res


def find_low_points(data):
	dim_x = len(data)
	dim_y = len(data[0])

	low_points = []

	for i in range(dim_x):
		for j in range(dim_y):
			bigger = 0
			hood = neighbours((i,j), dim_x, dim_y)
			for n in hood:
				if data[i][j] < data[n[0]][n[1]]:
					bigger += 1

			if bigger == len(hood):
				low_points.append((i, j))
	
	return low_points
	

def part1(data):
	risk_level = [data[i][j] + 1 for i, j in find_low_points(data)]

	return sum(risk_level)
							
def find_basin_size(res, dim_x, dim_y, point, data, points_in_basin):
	x = point[0]
	y = point[1]

	points_in_basin[x][y] = True
	for n in neighbours((point[0], point[1]), dim_x, dim_y):
		neighbour_x = n[0]
		neighbour_y = n[1]
		
		if not points_in_basin[neighbour_x][neighbour_y] and data[x][y] <= data[neighbour_x][neighbour_y] < 9:
			points_in_basin[neighbour_x][neighbour_y] = True
			res += 1
			res = find_basin_size(res, dim_x, dim_y, (neighbour_x,neighbour_y), data, points_in_basin)
	
	return res
	
def part2(data):
	dim_x = len(data)
	dim_y = len(data[0])

	basin_lengths = []
	points_in_basin = [[False] * dim_y for i in range(dim_x)]

	for i, j in find_low_points(data):
		res = 1
		res = find_basin_size(res, dim_x, dim_y, (i,j), data, points_in_basin)
		basin_lengths.append(res)
	
	# multiply length of three biggest basins
	res = 1
	for x in sorted(basin_lengths)[-3:]:
		res = res * x

	return res

if not options.filename:
	parser.error("Filename not given")
else:
	try:
		start_time = time()
		with open(options.filename, 'r') as f:
			data = [[int(j) for j in list(i.strip())] for i in f.read().splitlines()]

			print(part1(data))
			print(part2(data))					
		print("*** Run time: {} ms".format(int((time() - start_time) * 1000)))
	except FileNotFoundError as e:
		print(e)
