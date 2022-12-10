### Day 10 ###
from sys import argv
fileName = argv[1]

# state
cycle = 0 # 0 based now
register = 1

CRT = [ \
	[ '' for col in range(40)] \
	for row in range(6) \
]

def executeCycle(command, value=None):
	global CRT, cycle, register
	# CRT
	CRTRow = int(cycle / 40)
	CRTCol = cycle % 40
	CRTPixel = '#' if abs(register - CRTCol) <= 1 else '.'
	CRT[CRTRow][CRTCol] = CRTPixel

	cycle += 1

	# RUN CMD
	match command:
		case 'addx':
			executeCycle('noop') # takes an extra cycle
			register += int(value)
		case 'noop':
			pass


with open(fileName, 'r') as file:
	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		parts = line.split(" ")
		command = parts[0]
		value = None
		if len(parts) > 1:
			value = parts[1]
		executeCycle(command, value)

for row in CRT:
	print (''.join(row))