### Day 7 ###
from sys import argv

debug = False

tree = {} 

doneExecuting = False

class Node:
	def __init__(self, isDir=None, path=None, size=None):
		self.childrenPaths = set()
		self.isDir = isDir # None / bool. None = unknown as of yet.
		self.path = path
		self.size = size
	
	def getChildren(self):
		return [tree[path] for path in list(self.childrenPaths)]
	
	def getSize(self):
		if self.getType() == 'file':
			return self.size
		else:
			return sum(
				list(map(
					lambda child: child.getSize(),
					self.getChildren()
				))
			)
	
	def getType(self):
		if (self.isDir == None):
			raise Error('No info yet on whether', self.path, ' is a dir or file')
		if (self.isDir):
			return 'dir'
		else:
			return 'file'


# Read file
fileName = argv[1]
with open(fileName, 'r') as file:
	terminalOutput = file.readlines() # There, I got lazy

root = Node(isDir=True, path='/')
tree ['/'] = root

currPath = root.path
line = terminalOutput.pop(0).strip() # i wouldn't normally do this but this is scripting
try:
	while line:
		if debug:
			print ("Running: ", line)
		if line[0:2] != '$ ': # Unhandled output
			raise Error('unhandled output', line)
		
		command = line[2:].split(' ')
		match command[0]: # what
			case 'cd':
				prevPath = currPath
				# update currPath
				match command[1]: # cd where
					case '/':
						currPath = '/'
					case '..':
						lastSlashIndex = currPath.rfind('/')
						currPath = prevPath[0:lastSlashIndex]
					case _:
						currPath = prevPath + '/' + command[1]
				# is this a new path?
				if currPath not in tree.keys():
					newNode = Node(isDir=None, path=currPath)
					tree[prevPath].isDir = True
					tree[prevPath].childrenPaths.add(currPath)
					tree[currPath] = newNode
				line = terminalOutput.pop(0).strip()

			case 'ls':
				# run through the output until you get a command
				line = terminalOutput.pop(0).strip()
				if debug:
					print ('lsing: ',line)
				while line[:2] != '$ ':
					currRes = line.split(' ')
					newPath = currPath + '/' + currRes[1]
					tree[currPath].childrenPaths.add(newPath)

					if newPath not in tree:
						if (debug):
							print ('found new path', newPath)
						tree[newPath] = Node(isDir=(currRes[0] == 'dir'), path=newPath)
						if currRes[0] != 'dir':
							tree[newPath].size = int(currRes[0])
					line = terminalOutput.pop(0).strip()
			case _:
				raise Error('Bad command', command)
except IndexError:
	pass

doneExecuting = True

smallFilesSizes = 0
for path in tree.keys():
	currNode = tree[path]
	if not currNode.isDir:
		continue
	size = currNode.getSize()
	if size <= 100000:
		if (debug):
			print ("path",path,'size',size)
		smallFilesSizes += size


if (debug):
	print ("RESULT")
print (smallFilesSizes)

#part 1: 95437 


