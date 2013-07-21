import sys
import re
def FindBeauty(line):
	beauty=0
	maxval=26
	dict={}
	for letter in line.upper():
		if re.match('[A-Z]',letter):
			if letter in dict:
				dict[letter]+=1
			else:
				dict[letter]=1
	for x in reversed(sorted(dict.values())):
		beauty= beauty + (int(x)*maxval)
		maxval= maxval - 1
	return beauty
try:
	f=open(sys.argv[1],'r')
	for line in f:
		if line:
			print FindBeauty(line)
except Exception as e:
	print e.message
	sys.exit(1)
sys.exit(0) 