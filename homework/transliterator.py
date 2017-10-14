import sys

vocab =  sys.stdin.readlines()

table = {}

fd = open("symbols2.txt")
for line in fd.readlines():
	line = line.strip("\n")
	line = line.split("\t")
	inn = line[0]
	out = line[1]
	table[inn] = out
	
for a in vocab:
	a=a.strip()
	if a.count("\t") == 0:
		print(a)
		continue
	line=a.split("\t")
	form=line[1]
	for x in table:
		form = form.replace(x, table[x])
	line[9] = form
	print("\t".join(line))