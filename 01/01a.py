### Day 1 ###
# Plain and simple and not ideal but y bother
from sys import argv
fileName = argv[1]

elfLog = []

with open(fileName, 'r') as file:
	currElf = []

	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		if len(line) == 0:
			elfLog.append(currElf)
			currElf = []
		else:
			currElf.append(int(line.strip()))

#print(elfLog)

calories = map(sum, elfLog)

print(max(calories))