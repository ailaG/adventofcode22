import re

def decipherMonkeyInput(lines):
	# Input is not well documented! 
	regexes = {\
		'id': 'Monkey (?P<id>[0-9]+)',
		'items': 'Starting items: (?P<itemsStr>.+)$',
		'operation': 'Operation: new = (?P<func>.+)$',
		'testDivisor': 'Test: divisible by (?P<divisor>\d+)$',
		'if': 'If (?P<calcRes>\w+): throw to monkey (?P<monkeyId>\w+)$'

	}
	# line 1: ID
	id = re.match(regexes['id'], lines[0]).group('id')
	
	# line 2: items
	itemsStrs = re.match(regexes['items'], lines[1]).group('itemsStr').split(', ')
	items = [int(item) for item in itemsStrs]

	# line 3: operation to estimate worry level from item ID
	worryFuncRaw = re.match(regexes['operation'], lines[2]).group('func')
	operation = lambda old: eval(worryFuncRaw)
	
	# line 4: Test, divisibility	
	testDivisor = re.match(regexes['testDivisor'], lines[3]).group('divisor')
	test = lambda level: level % int(testDivisor) == 0

	# line 5: If true
	ifTrueMonkeyId = re.match(regexes['if'], lines[4]).group('monkeyId')

	# line 6: If false
	ifFalseMonkeyId = re.match(regexes['if'], lines[5]).group('monkeyId')
	return { # I miss JS now
		'id': id,
		'items': items,
		'operation': operation,
		'test': test, 
		'ifTrueMonkeyId': ifTrueMonkeyId, 
		'ifFalseMonkeyId': ifFalseMonkeyId
	}

def readInput(fileName):
	monkeysRaw = []
	with open(fileName, 'r') as file:
		lineCount = -1
		rawMonkeyInput = []
		while True:
			raw = file.readline()
			lineCount+= 1
			if not raw:
				break
			line = raw.strip()
			rawMonkeyInput.append(line)
			if lineCount % 7 == 6:
			#if len(line) == 0:
				monkeysRaw.append(decipherMonkeyInput(rawMonkeyInput))
				rawMonkeyInput = []
	return monkeysRaw

