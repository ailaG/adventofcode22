### Day 5 ###
from sys import argv
from readInput import readInput

# Read file
fileName = argv[1]
(stacks, moves) = readInput(fileName)

# Simulate

for move in moves:
	for counter in range(int(move['amount'])-1, -1, -1):
		item = stacks[move['from']].pop(counter)
		stacks[move['to']].insert(0, item)


# Print result
keys = list(stacks.keys())
keys.sort()
print(''.join([stacks[key][0] for key in keys]))
