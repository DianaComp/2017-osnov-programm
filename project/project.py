import sys

text = sys.stdin.readlines()
text.sort(reverse=True)

fd = open("twit_tok.txt", "w+")
id = 1

a = []
emotions = {}
emotions["emotion"] = "emotions"

for line in text:
	line = line.strip()
	line = line.split("\t")

	twit = line[1]
	emotion = line[2]
	rating = line[3]
	tab = "\t"

	fd.write("&emotion %s \n # %s, id= %d, \n # text = %s \n" % (emotion, emotion, id, twit))
	id = id+1

	column = rating + tab + twit
	a.append(column)

	i = twit
	exclusion = ["0."]
	for exc in exclusion:
		i = i.replace(exc, "&&&")
	punctuation = [".", ",", "?", "!", ":", ";", "(", ")", "/"]
	for hats in punctuation:
		i = i.replace(hats, " " + hats)
	token_id = 1
	tokens = i.split(" ")
	for token in tokens:
		token = token.replace("&&&", "0.")
		fd.write("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_\n" % (token_id, token))
		token_id += 1
	fd.write("\n")

fd.close()

base = open("twit_tok.txt")
tokenised_tagged = open("twits_tagged.txt", "w+")
vocab =  base.readlines()

table = {}

tokt = open("twits_vocabulary.txt")
for line in tokt.readlines():
	line = line.strip("\n")
	if "\t" not in line:
		continue
	if line == "&"
		print(line)
	line = line.split("\t")
	inn = line[0]
	out = line[1]
	table[inn] = out

for b in vocab:
	b = b.strip()
	if b.count("\t") == 0:
		print(b)
		continue
	line = b.split("\t")
	surf = line[1]
	if surf in table:
		line[3] = table[surf]
	tokenised_tagged.write("\t".join(line))

tokenised_tagged.close()

file = open("twits_tagged.txt")
tr = open("twits_train.txt", "w+")

train = file.readlines()

words = {}
tags = {}
count_of_words = {}

total = 0
for line in train:
	if "\t" not in line:
		continue
	row = line.split("\t")
	
	word = row[1]
	if word == "_":
		continue
	if word not in words:
		words[word] = {}

	if word not in count_of_words:
		count_of_words[word] = 0
	count_of_words[word] = count_of_words[word] + 1

	tag = row[3] 
	if tag == "_":
		continue
	if tag not in tags:
		tags[tag] = 0
	tags[tag] = tags[tag] +1

	if tag not in words[word]:
		words[word][tag]=0
	words[word][tag] = words[word][tag]+1
	total = total+1 

for tag in tags:
	freq = tags[tag]/total
	tr.write("%.2f\t%d\t%s\t%s\n" % (freq, tags[tag], tag, "_"))

for word in words:
	for tag in words[word]:
		freq = words[word][tag]/count_of_words[word]
		tr.write("%.2f\t%d\t%s\t%s\n" % (freq, (words[word][tag]), tag, word))

