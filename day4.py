#!/usr/bin/env python3
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

BOARD_SIZE = 5

def column(matrix, i):
    return [row[i] for row in matrix]

def bingo(matrix):
	res = False
	for row in matrix:
		status = [elt[1] for elt in row]
		if status.count(True) == BOARD_SIZE:
			res = True
			break
	if not res:
		for i in range(BOARD_SIZE):
			status = [elt[1] for elt in column(matrix, i)]
			if status.count(True) == BOARD_SIZE:
				res = True
				break

	return res

def update_board(drawn_number, matrix):
	for row in matrix:
		for elt in row:
			if elt[0] == drawn_number:
				elt[1] = True

def draw_part1(drawings, boards):
	is_bingo = False
	while drawings:
		for board in boards:
			update_board(drawings[0], board)
			if bingo(board):
				is_bingo = True
				break
		if is_bingo:
			break
		drawings.pop(0)
	return (drawings[0], board) if is_bingo else (None, None)


def calculate_score(board):
	notchecked_sum = 0
	for row in board:
		for elt in row:
			if not elt[1]:
				notchecked_sum += elt[0]
	return notchecked_sum

def draw_part2(drawings, boards):
	status_list = [False] * len(boards)
	last_bingo = len(status_list) - status_list.count(True)
	while drawings:
		for i in range(len(boards)):
			update_board(drawings[0], boards[i])
			if not status_list[i] and bingo(boards[i]):
				status_list[i] = True
				last_bingo = len(status_list) - status_list.count(True)
				if last_bingo == 0:
					break
		if last_bingo == 0:
			break
				
		drawings.pop(0)
	return (drawings[0], boards[i]) if last_bingo == 0 else (None, None)

if not options.filename:
    parser.error('Filename not given')
else:
	try:
		start_time = int(round(time() * 1000))
		with open(options.filename, 'r') as f:
			drawings = [int(x) for x in f.readline().split(',')]
			_ = f.readline()
			# filter empty lines
			lines = list(filter(None, f.read().splitlines())) 
			# list them in lists of five strings
			boards_collection = [lines[x:x+BOARD_SIZE] for x in range(0, len(lines), BOARD_SIZE)]
			# split each row in individual numbers
			boards_collection = [[row.split() for row in rows] for rows in boards_collection]
			# convert to [integer, draw status]
			boards_collection = [[[[int(x), False] for x in row] for row in matrix] for matrix in boards_collection]
			# play part 1 & part 2 bingos
			draw_functions = (draw_part1, draw_part2)
			for func in draw_functions:
				lucky_draw, lucky_board = func(drawings, boards_collection)
				if lucky_board:
					score = calculate_score(lucky_board)
					print(lucky_draw, score, lucky_draw * score)
			print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
	except FileNotFoundError as e:
		print(e)
