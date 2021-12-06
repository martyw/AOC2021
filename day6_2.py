#!/usr/bin/env python3
from optparse import OptionParser
from collections import Counter

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
			c = Counter(data)
			generation = { k: v for k, v in c.items() }
			for part in parts:
				for i in range(part):
					print(i, generation)
					new_generation = {}
					for age in generation.keys():
						if age == 0:
							print("add new {}".format(0))
							new_generation[6] = generation[0]
							new_generation[8] = generation[0]
						else:
							print("add a {}:{}".format(age-1, generation[age]))
							new_generation[age-1] = generation[age]
					generation = new_generation
				print(generation)
			print(sum(generation.values()))
						
	except FileNotFoundError as e:
		print(e)
