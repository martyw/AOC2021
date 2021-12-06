#!/usr/bin/env python3
from optparse import OptionParser
from enum import Enum, auto

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()
		
	
if not options.filename:
    parser.error("Filename not given")
else:
	try:
		with open(options.filename, 'r') as f:
			data = [int(i.strip()) for i in f.readline().split(',')]
			parts = (80, 256)
			for part in parts:
				for i in range(part):
					res = []
					for j in data:
						if j == 0:
							res.append(6)
							res.append(8)
						else:
							res.append(j-1)
					data = res
					print(i, len(data))
						
	except FileNotFoundError as e:
		print(e)
