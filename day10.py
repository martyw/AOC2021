#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def parse_chunk(chunk, token_pairs):
	open_tokens = []
	for ch in chunk:
		if ch in token_pairs.keys():
			open_tokens.append(ch)
		elif not open_tokens:
			return ch
		elif token_pairs[open_tokens[-1]] == ch:
			open_tokens.pop()
		else:
			return ch
	
	return [token_pairs[ch] for ch in reversed(open_tokens)]

def part1(data):
	token_pairs = { '(': ')', '[': ']', '{':'}', '<': '>'}
	score_map = {')': 3, ']': 57, '}': 1197, '>': 25137 }

	ret = [ parse_chunk(line, token_pairs) for line in data ]
	ret = [ score_map[i] for i in ret if type(i) is str ]
	
	return sum(ret)

def calculate_completion_score(li, score_map):
	score = 0
	for ch in li:
		score *= 5
		score += score_map[ch]
	return score

def part2(data):
	token_pairs = { '(': ')', '[': ']', '{':'}', '<': '>'}
	completion_score = {')': 1, ']': 2, '}': 3, '>': 4 }
	
	not_corrupted_lines = [ line for line in data if type(parse_chunk(line, token_pairs)) is list ]
	completion_lists = [parse_chunk(chunk, token_pairs) for chunk in not_corrupted_lines]
	completion_scores = [calculate_completion_score(li, completion_score) for li in completion_lists]
	
	return sorted(completion_scores)[len(completion_scores) // 2]
										
if not options.filename:
	parser.error("Filename not given")
else:
	try:
		start_time = time()
		with open(options.filename, 'r') as f:
			data = [i.strip() for i in f.read().splitlines()]
			print(part1(data))
			print(part2(data))					
		print("*** Run time: {} ms".format(int((time() - start_time) * 1000)))
	except FileNotFoundError as e:
		print(e)
