from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

if not options.filename:
    parser.error('Filename not given')
else:
	try:
		with open(options.filename, 'r') as f:
			#part 1			
			data = [line.split() for line in f.read().splitlines()]
			data = [(k, int(v)) for k, v in data]
			horizontal = 0
			depth = 0
			for k, v in data:
				if k == 'down':
					depth += v
				elif k == 'up':
					depth -= v
				elif k == 'forward':
					horizontal += v
				else:
					raise ValueError
			print(horizontal * depth)
			
			# part 2
			horizontal = 0
			depth = 0
			aim = 0
			for k, v in data:
				if k == 'down':
					aim += v
				elif k == 'up':
					aim -= v
				elif k == 'forward':
					horizontal += v
					depth += aim * v
				else:
					raise ValueError
			print(horizontal * depth)
			
	except FileNotFoundError as e:
		print(e)
