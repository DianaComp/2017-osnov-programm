import sys

text = sys.stdin.readlines()

for i in range(0, 3):
	line = text[i]
	print("# sent_id = ",i+1,"\n", "#text = ", line)
	token_id = 1
	punctuation = [".", ",", "?", "!", ":", ";"]
	newline1=line.replace("с. ш.","&&&&")
	newline2=newline1.replace("з. д.","////")
	for hats in punctuation:
			newline2 = newline2.replace(hats, " " + hats)
	tokens = newline2.split(" ")
	for token in tokens:
		token=token.replace("&&&&", "с. ш. ")
		token=token.replace("////","з. д. ")
		print("%d\t%s" % (token_id, token))
		token_id = token_id+1