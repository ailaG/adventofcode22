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
		bags.append(line) # !!

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

for groupLead in range(0,len(bags),3):
	itemsInCommon = set(bags[groupLead]) & set(bags[groupLead+1]) & set(bags[groupLead+2])
	item = itemsInCommon.pop()
	priority = getPriority(item)
	prioritiesSum += priority

print (prioritiesSum)