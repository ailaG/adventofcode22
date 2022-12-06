### Day 4 ###
from sys import argv

# Read file
fileName = argv[1]

lineNum = -1

with open(fileName, 'r') as file:
	while True:
		lineNum += 1
		debug = (lineNum == 0)

		raw = file.readline()
		if not raw:
			break
		line = raw.strip()
		print ('testing',line)

		sigLength = 4

		charIndex = 0 # bc we'll increase it first thing
		while charIndex < len(line):
			charIndex += 1 # keep in top of loop!! to avoid an infinite loop
			char = line[charIndex]

			# prevGroup= line[max(0, charIndex - sigLength +1) : charIndex]
			# if debug:
			# 	print(charIndex,"searching",char,"in",prevGroup)

			# findInd = prevGroup.rfind(char)
			start = max(0,charIndex - sigLength + 1)
			end = charIndex
			findInd = line.find(char, start, end)

			if debug:
				print ('ind', charIndex, 'char', char, 'findInd', findInd, 'from', start,'to',end)

			if findInd < 0:
				if debug:
					print ('not in range')
				if end >= sigLength:
					print ('RESULT',charIndex + 1) # +1 because they're counting from 1
					break
				else:
					if (debug):
						print ("Too early. end is", end)
					
			else:
				#charIndex = (max(0, charIndex - sigLength + 1)) + findInd - 1
				#charIndex += sigLength + findInd 
				charIndex = max(charIndex, findInd + sigLength - 1) # should be findInd but just in case, no infinite loops!
				if debug:
					print ("FOUND. charIndex: ", charIndex)
		