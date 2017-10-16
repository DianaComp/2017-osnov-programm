import sys

vocab =  sys.stdin.readlines()

table = {}

fd = open("POS_vocab1.txt")

for b in vocab:
	b = b.strip()
	if b.count("\t") == 0:
		print(b)
		continue
	line = b.split("\t")
	pos = line[1]
	for y in table:
		form = pos.replace(y, table[y])
	line[3] = pos
	print("\t".join(line))