### Day 8 ###
from sys import argv

# Read file
fileName = argv[1]
with open(fileName, 'r') as file:
	grid_raw = file.readlines()

# "grid" is a 2d list
grid = tuple(map(lambda line: tuple(line.strip()), grid_raw))

def checkViewingDistance(line, maxHeight):
	for index in range(len(line)-1):
		height = int( line[index] )
		if height >= maxHeight:
			return index + 1
	return len(line)

gridTransposed = tuple(zip(*grid))
def checkScenicScore(rowInd, colInd):
	treeHeight = int(grid[rowInd][colInd])
	row = grid[rowInd]
	# col = tuple(\
	# 	map(\
	# 		lambda row:row[colInd]\
	# 	, grid)
	# )
	col = gridTransposed[colInd]

	def rev(myList): # helper
		return list(reversed(myList))
	up = rev(col[:rowInd])
	down = col[rowInd+1:]
	left = rev(row[:colInd])
	right = row[colInd+1:]
	return \
		checkViewingDistance(left, treeHeight) * \
		checkViewingDistance(right, treeHeight) * \
		checkViewingDistance(up, treeHeight) * \
		checkViewingDistance(down, treeHeight) 



# for input-example
print ("test 1, is this 4?", checkScenicScore(1,2))
print ("test 2, is this 8?", checkScenicScore(3,2))


highestScore = -1
for rowInd in range(1,len(grid)-1):
	for colInd in range(1,len(grid[rowInd])-1):
		score = checkScenicScore(rowInd, colInd)
		if score == 0:
			print (rowInd,",",colInd)
			
		highestScore = max(score, highestScore)
print ("Result:", highestScore)