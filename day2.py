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
			data = [line.split() for line in f.read().splitlines()]
			data = [(k, int(v)) for k, v in data]
			aim = 0
			horizontal = 0
			depth_part1 = 0
			depth_part2 = 0
			for k, v in data:
				if k == 'down':
					depth_part1 += v
				elif k == 'up':
					depth_part1 -= v
				elif k == 'forward':
					horizontal += v
					depth_part2 += aim * v
				else:
					raise ValueError
				aim = depth_part1
				
			print(horizontal * depth_part1)
			print(horizontal * depth_part2)
			
	except FileNotFoundError as e:
		print(e)
