### Day X ###
from sys import argv
fileName = argv[1]

with open(fileName, 'r') as file:
	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip()