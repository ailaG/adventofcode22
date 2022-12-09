### Day 9 ###
from sys import argv

def sign(n): #helper
	if n==0:
		return 0
	else:
		return int(n/abs(n))

state = { 	
	# Up, right = positive. Down, left = negative. Like a standard x-y graph. Per AoC's examples.
	'positions': [ [0,0] for i in range(10) ],
	'tailFootprints' : set()
}

def moveHead(direction):
	match direction:
		case "U":
			state['positions'][0][1] += 1
		case "D":
			state['positions'][0][1] -= 1
		case "R":
			state['positions'][0][0] += 1
		case "L":
			state['positions'][0][0] -= 1
		case _:
			raise Exception('Bad direction received', direction)

def moveKnot(n): # n>0
	prev = state['positions'][n-1]
	curr = state['positions'][n]
	deltas = [ prev[0] - curr[0], prev[1] - curr[1] ]
	moveBoth = abs(deltas[0]) + abs(deltas[1]) > 2 # H is 2+ steps away w/o diagonals
	for axisIndex in [0,1]:
		if moveBoth or abs(deltas[axisIndex]) > 1: # too far left/right
			state['positions'][n][axisIndex] += sign(deltas[axisIndex])

def recordTail():
	state['tailFootprints'].add(str(state['positions'][-1]))


fileName = argv[1]
with open(fileName, 'r') as file:

	while True:
		raw = file.readline()
		if not raw:
			break
		(direction, steps) = raw.strip().split(" ")

		for step in range(int(steps)):
			moveHead(direction=direction)
			for knotInd in range(1, len(state['positions'])):
				moveKnot(knotInd)
			recordTail()

print (len(state['tailFootprints']))