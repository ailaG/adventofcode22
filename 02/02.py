### Day 2 ###
from sys import argv

# Read file
fileName = argv[1]
plan = [] # Made of steps. A step is a tuple of: what the other player got, what I'm playing
with open(fileName, 'r') as file:
	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip().split(' ')
		if len(line) != 2:
			raise Error('Error in line', line)
		plan.append((line[0], line[1]))

# Calculate score
def scoreStep(step):
	scoresDict = {
		"A" : 1,
		"B" : 2,
		"C" : 3
	}
	resultsDict = {
		"X" : 'lose',
		"Y" : 'draw',
		"Z" : 'win'
	}
	resultsScoring = {
		"X" : 0,
		"Y" : 3,
		"Z" : 6
	}

	winPermutation = ("A","C","B") # A beats C, C beats B...

	opponentMove = step[0]
	myMoveScore = None
	result = step[1]
	match resultsDict[result]:
		case 'lose':
			myMoveScore = ((scoresDict[opponentMove] -1) -1 ) % 3 + 1 # their score index, minus 1 bc mine is 1 lower, all that %3, then it starts at 1 again
		case 'draw':
			myMoveScore = scoresDict[opponentMove]
		case 'win':
			myMoveScore = ((scoresDict[opponentMove] -1) +1 ) % 3 + 1 # see 'lose' for details
	return resultsScoring[result] + myMoveScore

score = 0;
for step in plan:
	print(scoreStep(step))
	score += scoreStep(step)
# Being philosophical here in case someone's reading. I could've used map as I have earlier.
# 	BUT the nature of a game is taking turns. Hence the iterative code here, because code == story

print(score)

