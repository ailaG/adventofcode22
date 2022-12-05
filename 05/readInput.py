import re

def readInput(fileName):
	with open(fileName, 'r') as file:
		# Read stacks
		stacks = {}
		while True:
			raw = file.readline()
			if not raw:
				raise Error('No moves?')
			line = raw.rstrip()
			if len(line) == 0:
				break
			if '[' not in line:
				continue
			for charIndex in range(0, len(line), 4):
				stackIndex = str(int(charIndex /  4) + 1)
				if not stackIndex in stacks:
					stacks[stackIndex] = []
				item = line[charIndex+1].strip()
				if item:
					stacks[stackIndex].append(item)

		# Read moves
		moves = []
		while True:
			raw = file.readline()
			if not raw:
				break
			line = raw.strip()
			if len(line) == 0:
				continue
			exp = re.compile("move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)")
			move = exp.match(line).groupdict()
			moves.append(move)
		return (stacks, moves)