"""

I/O parser

"""

f = open('test.txt','r')

parsed = {}

for line in f:
	splitline = line.strip().split(" = ")
	parsed[splitline[0]] = splitline[1]
	
print parsed