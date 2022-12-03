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
		"C" : 3,
		"X" : 1,
		"Y" : 2,
		"Z" : 3
	}
	resultsDict = {
		"lose" : 0,
		"draw" : 3,
		"win" : 6
	}
	result = None
	match scoresDict[ step[1] ] - scoresDict[ step[0] ]:
		case 0:
			result = 'draw'
		case 1 | -2:
			result = 'win'
		case -1 | 2:
			result = 'lose'
		case _:
			raise Error('Bad result in step', step)
	return resultsDict[result] + scoresDict[ step[1] ]

score = 0;
for step in plan:
	score += scoreStep(step)
# Being philosophical here in case someone's reading. I could've used map as I have earlier.
# 	BUT the nature of a game is taking turns. Hence the iterative code here, because code == story

print(score)

