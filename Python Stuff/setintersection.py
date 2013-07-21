import sys
import re
def removeduplicates(array):
	dict = {}
	out=""
	for x in array:
		if x in dict:
			out=out+x+","
		else:
			dict[x]=False
	print out[:len(out)-1]
try:
	f=open(sys.argv[1],'r')
	for line in f:
		string=re.split(',|;',line.strip())
		removeduplicates(string)
except:
	sys.exit(1)
sys.exit(0)