### Day 4 ###
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
		print ('testing',line)

		
		#for index in range(0,len(line)):
		index = -1 
		tmp=0
		while index < len(line):
			index += 1 # FIRST THING lest we have an infinite loop
			#print ("")
			sigLength = 4
			char = line[index]
			dupIndex = line.find(char, max(0,index - sigLength - 1), index)
			
			#print ('char', line[index], 'range', list(range(max(0, index - sigLength),index)))
			#print ('ind', index, 'dupind', dupIndex)
			print (" index ", index, line,"dupindex", dupIndex)

			if dupIndex < 0:
				if index > sigLength:
					print("*****",line, index)
					break
				#else:
				#	print ("dupindex <0 but index is", index)
			else:
				index += dupIndex +1 # bc we're increasing by 1 first thing in the loop
				print ("index now", index, 'next will be', index+1)
				print ("")
			
		tmp += 1
		if tmp >= 2:
			break