### Day 3 ###
from sys import argv

# Read file
fileName = argv[1]
groups = [] # pairs
with open(fileName, 'r') as file:
	while True:
		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		elvesRaw = line.split(",")
		group = [] # pair
		for rawElf in elvesRaw:
			elf = rawElf.split('-')
			group.append( [ int(elf[0]) , int(elf[1]) ] )
		groups.append(group)

# Now we have our groups! From now on we assume pairs
bad_pairs_count = 0
# I was considering using Python's range(elf[0],elf[1]+1) but I think this is simpler
for pair in groups:
	startDiff = pair[0][0] - pair[1][0]
	endDiff = pair[0][1] - pair[1][1]
	# if one is contained within the other, one of these will be negative and the other positive. Or zeroes.
	if startDiff * endDiff <= 0:
		bad_pairs_count += 1

print (bad_pairs_count)
