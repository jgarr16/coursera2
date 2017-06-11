# this program reads a file and manipulates the text using RegEx (re)

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('^X\S*: ([0-9.]+)', line)
	if len(x) > 0 and float(x[0]) > 0:
		print float(x[0])