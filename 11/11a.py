### Day 11 ###
# NOTE!!  I'm assuming that the input file has a num of lines divisible by 7
# I had to add 1-2 blank lines to my inputs.
# Could I test it? Get around it? Yes. Did I want to? No. Now go away, nitpicker :)

from sys import argv
from readInputA import readInput
fileName = argv[1]

monkeys = {}
doneReading = False

class Monkey: # Wrong, these monkeys have no class.
	def __init__(self, id, items=[], operation=lambda x:x, testCond=None, monkeyIfTrue=None, monkeyIfFalse=None):
		self.activity = 0
		self.id = id
		self.items = items
		self.operation = operation
		self.howToTest = (testCond, monkeyIfTrue, monkeyIfFalse)

	def causeChaos(self):
		while len(self.items) > 0:
			self.inspectNextItem()
			self.processNextItem()

	def inspectNextItem(self):
		item = self.items.pop(0)
		# Worry level rises!
		item = self.operation.__call__(item)
		# Phew, didn't damage it.
		item = int(item / 3)
		# put back
		self.items.insert(0,item)

	def processNextItem(self):
		(test, monkeyIfTrue, monkeyIfFalse) = self.howToTest
		self.activity += 1
		item = self.items[0]
		if test.__call__(item):
			self.yeet(item, monkeyIfTrue)
		else:
			self.yeet(item, monkeyIfFalse)
	
	def yeet(self, item, toMonkeyId):
		global monkeys
		if not doneReading:
			raise Exception('Yeeted before all monkeys are present')
		self.items.remove(item) # Assumes exists
		monkeys[toMonkeyId].items.append(item)

def getMonkeyBusiness(monkeys):
	res = 0
	items = list(map(
		lambda monkey: monkey.activity,
		monkeys.values()
	))
	items.sort()
	return items[-2] * items[-1]


### ACTIONS ###

# Read
for monkeyRaw in readInput(fileName):
	monkeys[monkeyRaw['id']] = Monkey(\
		id=monkeyRaw['id'], \
		items=monkeyRaw['items'], \
		operation=monkeyRaw['operation'], \
		testCond=monkeyRaw['test'], 
		monkeyIfTrue=monkeyRaw['ifTrueMonkeyId'], 
		monkeyIfFalse=monkeyRaw['ifFalseMonkeyId']\
	)
doneReading = True

# Do
for round in range(20):
	for monkey in monkeys.values():
		monkey.causeChaos()

# 10605 for the example input
print (getMonkeyBusiness(monkeys))