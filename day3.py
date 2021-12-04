#!/usr/bin/env python3
from optparse import OptionParser
from enum import Enum, auto

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

class WhatTest(Enum):
	OXYGEN = auto()
	CO2 = auto()

def rank_bits(data):
	bytesize = len(data[0])
	zeros = [0] * bytesize 
	ones = [0] * bytesize
	
	for line in data:
		for i in range(0, bytesize):
			zeros[i] += int(line[i] == '0')
			ones[i] += int(line[i] == '1')
	return zeros, ones

def calculate_greeks(data):
	bytesize = len(data[0])
	zeros, ones = rank_bits(data)
	gamma = [0] * bytesize
	epsilon = [0] * bytesize
	for i in range(0, bytesize):
		gamma[i] = str(1) if ones[i] >= zeros[i] else str(0)
		epsilon[i] = str(0) if ones[i] >= zeros[i] else str(1)
	return gamma, epsilon

def get_rating(data, test_type):
	bytesize = len(data[0])
	test_data = data
	test_gamma_on = '1' if test_type == WhatTest.OXYGEN else '0' 

	for j in range(0, bytesize):
		gamma, epsilon = calculate_greeks(test_data)
		if gamma[j] == test_gamma_on:
			test_data = [x for x in test_data if x[j] == '1']
		else:
			test_data = [x for x in test_data if x[j] == '0']
		
		if len(test_data) == 1:
			break
	
	return int(test_data[0],2)

def power_consumption(data):
	gamma, epsilon = calculate_greeks(data)
	return int(''.join(gamma), 2) * int(''.join(epsilon), 2)
	
def oxygen_generator_rating(data):
	return get_rating(data, WhatTest.OXYGEN)

def co2_scrubber_rating(data):
	return get_rating(data, WhatTest.CO2)
	
	
data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
assert power_consumption(data) == 198, "Power consumption test fails"
assert oxygen_generator_rating(data) == 23, "oxygen generator rating test fails"
assert co2_scrubber_rating(data) == 10, "CO2 scrubber rating test fails"

if not options.filename:
    parser.error('Filename not given')
else:
	try:
		with open(options.filename, 'r') as f:
			data = [i for i in f.read().splitlines()]
			print(power_consumption(data))
			print(oxygen_generator_rating(data) * co2_scrubber_rating(data))
	except FileNotFoundError as e:
		print(e)
