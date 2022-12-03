### Day 3 ###
from sys import argv

# Read file
fileName = argv[1]
bags = []
with open(fileName, 'r') as file:
	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		bagSize = int(len(line) / 2)
		bags.append( (
			line[:bagSize],
			line[bagSize:]
		) )

# Define priorities
def getPriority(item):
	# item is a letter
	itemOrd = ord(item)
	# Really rudimentary because WHY NOT
	if itemOrd >= 97: #lowercase
		return itemOrd - 97 + 1 # ord('a') == 97
	else:
		return itemOrd - 65 + 26 + 1 # ord('A') == 65

prioritiesSum = 0
for bag in bags:
	itemsInCommon = set(bag[0]) & set(bag[1]) # "cheating" does feel good
	item = itemsInCommon.pop()
	priority = getPriority(item)
	prioritiesSum += priority

print (prioritiesSum)