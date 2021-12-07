#!/usr/bin/env python3
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def distance_func_part1(dist):
	return dist

def distance_func_part2(dist):
	return (dist*(dist + 1)) // 2

def solve_puzzle(data, distance_func):		
	fuel_at_position = {}
	for position_x in range(max(data) + 1):
			fuel_needed = 0
			for position_y in data:
				dist = abs(position_x - position_y)
				fuel_needed += distance_func(dist)
			fuel_at_position[position_x] = fuel_needed
	return min(fuel_at_position.values())									
								
if not options.filename:
    parser.error("Filename not given")
else:
	try:
		with open(options.filename, 'r') as f:
			data = [int(i.strip()) for i in f.readline().split(',')]
			print(solve_puzzle(data, distance_func_part1))
			print(solve_puzzle(data, distance_func_part2))
	except FileNotFoundError as e:
		print(e)
