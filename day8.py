#!/usr/bin/env python3
from optparse import OptionParser
from time import time
from collections import Counter
from itertools import permutations
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

class SevenSegmentDisplay:
	def __init__(self):	
		self.segments = {}
		self.segments[0] = set(['a', 'b', 'c', 'e', 'f', 'g'])
		self.segments[1] = set(['c', 'f'])
		self.segments[2] = set(['a', 'c', 'd', 'e', 'g'])
		self.segments[3] = set(['a', 'c', 'd', 'f', 'g'])
		self.segments[4] = set(['b', 'c', 'd', 'f'])
		self.segments[5] = set(['a', 'b', 'd', 'f', 'g'])
		self.segments[6] = set(['a', 'b', 'd', 'e', 'f', 'g'])
		self.segments[7] = set(['a', 'c', 'f'])
		self.segments[8] = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
		self.segments[9] = set(['a', 'b', 'c', 'd', 'f', 'g'])

	def get_unique_digits_on_length(self):
		lengths = {k: len(v) for k, v in self.segments.items()}
		cntr = Counter(lengths.values())
		unique_nr_digits = { i for i in cntr if cntr[i] == 1}
		unique_digits_on_length = {k:v for k, v in lengths.items() if v in unique_nr_digits}
		
		return unique_digits_on_length
		
	def updated_ssd(self, mapping):
		mapped_segments = {}
		for i in range(10):
			mapped_segments[i] = {mapping[j] for j in self.segments[i]}
		return mapped_segments

	def scrambled_mapping(self, scrambled_key):
		res = ""		
		for perm in permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
			mapping = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'], perm))
			mapped_ssd = test_ssd.updated_ssd(mapping)
			mapped = [False] * 10
			for nr in scrambled_key.split():
				for i in range(10):
					if set(nr) == mapped_ssd[i]:
						mapped[i] = True
			if mapped.count(True) == len(mapped):
				res = mapped_ssd
				break
		return res
		
	def scrambled_value(self, scrambled_entry):
		scrambled_entry = scrambled_entry.split('|')
		mapping = self.scrambled_mapping(scrambled_entry[0].strip())
		scrambled_output = [ set(x) for x in scrambled_entry[1].strip().split() ]
		x = ""
		for i in scrambled_output:
			x += str(list(mapping.keys())[list(mapping.values()).index(i)])
		return x
		
test_ssd = SevenSegmentDisplay()
assert test_ssd.get_unique_digits_on_length() == {1: 2, 4: 4, 7: 3, 8: 7 }
assert "5353" == test_ssd.scrambled_value("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")

if not options.filename:
	parser.error("Filename not given")
else:
	try:
		start_time = time()
		ssd = SevenSegmentDisplay()
		unique_lenghths = ssd.get_unique_digits_on_length()
		with open(options.filename, 'r') as f:
			# part1
			count = 0
			file_content = f.read().splitlines()
			for line in [l.split("|")[1].strip() for l in file_content]:
				for pattern in line.split():
					if len(pattern) in unique_lenghths.values():
						count += 1
			print(count)
			
			# part 2
			print(sum([int(ssd.scrambled_value(line)) for line in file_content]))
		print("*** Run time: {} ms".format(int((time() - start_time) * 1000)))
	except FileNotFoundError as e:
		print(e)
