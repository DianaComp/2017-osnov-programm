import sys

a=sys.stdin.read()

aa=a.replace("с. ш. ","&&&&")
ab=aa.replace("з. д. ","////")
aab=ab.replace(". ",".\n")
aabb=aab.replace("&&&&", "с. ш. ")
abc=aabb.replace("////","з. д. ")
	
print(abc)