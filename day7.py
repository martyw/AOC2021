#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def distance_func_part1(dist):
	return dist

def distance_func_part2(dist):
	return (dist*(dist + 1)) // 2

def solve_puzzle(data, distance_func):		
	fuel_needed = {}
	for position_x in range(min(data), max(data)):
		fuel_needed[position_x] = sum([distance_func(abs(position_x - position_y)) for position_y in data])
	return min(fuel_needed.values())									
								
if not options.filename:
    parser.error("Filename not given")
else:
	try:
		start_time = time()
		with open(options.filename, 'r') as f:
			data = [int(i.strip()) for i in f.readline().split(',')]
			print(solve_puzzle(data, distance_func_part1))
			print(solve_puzzle(data, distance_func_part2))
		print("*** Run time: {} ms".format((time() - start_time) * 1000))
	except FileNotFoundError as e:
		print(e)
