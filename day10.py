#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def parse_chunk(chunk):
	token_pairs = { '(': ')', '[': ']', '{':'}', '<': '>'}
	open_tokens_stack = []
	for ch in chunk:
		if ch in token_pairs.keys():
			open_tokens_stack.append(ch)
		elif ch in token_pairs.values():
			if ch != token_pairs[open_tokens_stack.pop()]:
				return ch
		else:
			raise ValueError("Unexpected token found: {}".format(ch))

	return [token_pairs[ch] for ch in reversed(open_tokens_stack)] # the remainder

def part1(data):
	score_map = {')': 3, ']': 57, '}': 1197, '>': 25137 }

	ret = [ parse_chunk(line) for line in data ]
	ret = [ score_map[i] for i in ret if type(i) is str ]
	
	return sum(ret)

def calculate_completion_score(li):
	completion_score = {')': 1, ']': 2, '}': 3, '>': 4 }
	score = 0
	
	for ch in li:
		score = 5 * score + completion_score[ch]
	return score

def part2(data):
	not_corrupted_lines = [ line for line in data if type(parse_chunk(line)) is list ]
	completion_lists = [parse_chunk(chunk) for chunk in not_corrupted_lines]
	completion_scores = [calculate_completion_score(li) for li in completion_lists]
	
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

