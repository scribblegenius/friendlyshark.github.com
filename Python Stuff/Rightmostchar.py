import sys
try:
	f=open(sys.argv[1],'r')
	for line in f:
		array=line.split(",")
		printminusone=True
		Sentence=array[0].strip()
		Char=array[1].strip()
		for index,x in enumerate(reversed(Sentence)):
			if x==Char:
				print len(Sentence)-index-1
				printminusone=False
				break
		if printminusone:
			print -1
except:
	sys.exit(1)
sys.exit(0)