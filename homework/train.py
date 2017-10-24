import sys

train = sys.stdin.readlines()

hat = ["#P", "count", "tag", "form"]
print('\t'.join(hat))

w = {}
t = {}
count_of_words = {}

total = 0
for line in train:
	if "\t" not in line:
		continue
	row = line.split("\t")
	
	w1 = row[1] #form
	if w1 == "_":
		continue
	if w1 not in w:
		w[w1] = {}

	if w1 not in count_of_words:
		count_of_words[w1] = 0
	count_of_words[w1] = count_of_words[w1] + 1

	w2 = row[3] #tags
	if w2 == "_":
		continue
	if w2 not in t:
		t[w2] = 0
	t[w2] = t[w2] +1

	if w2 not in w[w1]:
		w[w1][w2]=0
	w[w1][w2] = w[w1][w2]+1
	total = total+1 

for w2 in t:
	freq = t[w2]/total
	print("%.2f\t%d\t%s\t%s" % (freq, t[w2], w2, w1))

for w1 in w:
	for w2 in w[w1]:
		freq = w[w1][w2]/count_of_words[w1]
		print("%.2f\t%d\t%s\t%s" % (freq, (w[w1][w2]), w2, w1))