#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def solver(data, distance_func):		
	return min([sum([distance_func(x, y) for y in data]) for x in range(min(data), max(data) + 1)])									
								
if not options.filename:
    parser.error("Filename not given")
else:
	try:
		start_time = time()
		with open(options.filename, 'r') as f:
			data = [int(i.strip()) for i in f.readline().split(',')]
			print(solver(data, lambda x, y: abs(x - y)))
			print(solver(data, lambda x, y: abs(x - y)*(abs(x - y) + 1)) // 2)
		print("*** Run time: {} ms".format((time() - start_time) * 1000))
	except FileNotFoundError as e:
		print(e)
