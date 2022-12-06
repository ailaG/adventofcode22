### Day 6 ###
from sys import argv

# Read file
fileName = argv[1]

lineNum = -1

with open(fileName, 'r') as file:
	while True:
		lineNum += 1
		debug = False #(lineNum == 0)

		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		print ('testing',line)

		sigLength = 4

		charIndex = 0 # bc we'll increase it first thing
		minResultIndex = sigLength - 1
		while charIndex < len(line):
			charIndex += 1 # keep in top of loop!! to avoid an infinite loop
			char = line[charIndex]
			start = max(0,charIndex - sigLength + 1)
			end = charIndex
			findInd = line.rfind(char, start, end)

			if debug:
				print ("")
				print ('ind', charIndex, 'char', char, 'findInd', findInd, 'from', start,'to',end)
				print ('MRI', minResultIndex)

			if findInd < 0:
				if debug:
					print ('not in range')
				if charIndex > minResultIndex:
					print ('RESULT', minResultIndex + 1)
					break
				else:
					if (debug):
						print ("Too early. end is", end, "Same MRI", minResultIndex)
					
			else:
				minResultIndex = findInd + sigLength
				if debug:
					print ("FOUND. New minResultIndex: ", minResultIndex)
		