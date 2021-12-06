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
			for part in parts:
				c = Counter(data)
				this_generation = dict(sorted({k: v for k, v in c.items()}.items()))
				for _ in range(part):
					new_generation = dict()
					for age in this_generation.keys():
						if age == 0:
							new_generation[6] = this_generation[0]
							new_generation[8] = this_generation[0]
						else:
							if age != 7:
								new_generation[age-1] = this_generation[age]
							else:
								try:
									new_generation[6] = this_generation[7] + new_generation[6]
								except KeyError:
									new_generation[6] = this_generation[7]
					this_generation = dict(sorted(new_generation.items()))
				print(sum(this_generation.values()))						
	except FileNotFoundError as e:
		print(e)
