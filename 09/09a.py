### Day 9 ###
from sys import argv

def sign(n): #helper
	if n==0:
		return 0
	else:
		return int(n/abs(n))

state = {
	# Up, right = positive. Down, left = negative. Like a standard x-y graph. Per AoC's examples.
	'headPosition' : [0,0], # I wish I could use tuples
	'tailPosition' : [0,0],

	'tailFootprints' : set()
}

def moveHead(direction):
	match direction:
		case "U":
			state['headPosition'][1] += 1
		case "D":
			state['headPosition'][1] -= 1
		case "R":
			state['headPosition'][0] += 1
		case "L":
			state['headPosition'][0] -= 1
		case _:
			raise Exception('Bad direction received', direction)

def moveTail():
	head = state['headPosition']
	tail = state['tailPosition']
	deltas = [ head[0] - tail[0], head[1] - tail[1] ]
	moveBoth = abs(deltas[0]) + abs(deltas[1]) > 2 # H is 2+ steps away w/o diagonals
	for axisIndex in [0,1]:
		if moveBoth or abs(deltas[axisIndex]) > 1: # too far left/right
			state['tailPosition'][axisIndex] += sign(deltas[axisIndex])

def recordTail():
	state['tailFootprints'].add(str(state['tailPosition']))


fileName = argv[1]
with open(fileName, 'r') as file:

	while True:
		raw = file.readline()
		if not raw:
			break
		(direction, steps) = raw.strip().split(" ")
		
		for step in range(int(steps)):
			moveHead(direction=direction)
			moveTail()
			recordTail()

print (len(state['tailFootprints']))