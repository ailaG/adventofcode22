### Day 10 ###
from sys import argv
fileName = argv[1]

# state
cycle = 1
register = 1
result = 0

def executeCycle(command, value=None):
	global cycle, register, result
	match command:
		case 'addx':
			executeCycle('noop') # takes an extra cycle
			register += int(value)
		case 'noop':
			pass

	cycle += 1

	if (cycle + 20) % 40 == 0:
		result += cycle * register


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

print (result)