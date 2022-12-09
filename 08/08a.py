### Day 8 ###
from sys import argv

# Read file
fileName = argv[1]

with open(fileName, 'r') as file:
	grid_raw = file.readlines()

# "grid" is a 2d list
grid = tuple(map(lambda line: tuple(line.strip()), grid_raw))

# We'll walk the trees from every direction. Every tree that's higher than the previously highest on that trip is visible.
# Note that we shouldn't count the same tree twice! So we'll do a set.

visibleTrees = set() # Strings. A tree in point (i,j) will be "i,j".

# But how do we do a single check?
def checkLineOfTrees(line): # front to back
	line = list(line)
	tallestSoFar = -1
	result = []
	for index in range(len(line)):
		height = int( line[index] )
		if height > tallestSoFar:
			result.append(index)
			tallestSoFar = height
	return result


# East and west
for rowIndex in range(len(grid)):
	currLine = grid[rowIndex]
	for colIndex in checkLineOfTrees(currLine):
		visibleTrees.add(f'{rowIndex},{colIndex}')
	for reversedIndex in checkLineOfTrees(reversed(currLine)):
		colIndex = len(currLine) - reversedIndex - 1
		visibleTrees.add(f'{rowIndex},{colIndex}')

# North and south
for colIndex in range(len(grid[0])):
	currLine = list(map(lambda row:row[colIndex], grid)) # not scalable but I DONT CARE
	for rowIndex in checkLineOfTrees(currLine):
		visibleTrees.add(f'{rowIndex},{colIndex}')
	for reversedIndex in checkLineOfTrees(reversed(currLine)):
		rowIndex = len(currLine) - reversedIndex - 1
		visibleTrees.add(f'{rowIndex},{colIndex}')

print (len(visibleTrees))

