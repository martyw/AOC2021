from optparse import OptionParser
from itertools import islice, tee

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="file with input data", metavar="FILE")
(options, args) = parser.parse_args()

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c
   
if not options.filename:
    parser.error('Filename not given')
else:
	try:
		with open(options.filename, 'r') as f:
			# part 1
			data = [int(i) for i in f.read().splitlines()]
			bigger = [first for first, second in pairwise(data) if second > first] 
			print(len(bigger))
			# part 2			
			triplet_sums = [first + second + third  for first, second, third in triplewise(data)] 
			bigger = [first for first, second in pairwise(triplet_sums) if second > first] 
			print(len(bigger))
	except FileNotFoundError as e:
		print(e)
