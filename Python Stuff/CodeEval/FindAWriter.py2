import sys
import re
def FindWriter(line):
	if(line):
		array=line.split("|")
		namesoup = array[0].strip()
		indices = array[1].strip()
		return "".join([ namesoup[int(x)-1] for x in indices.split(" ")])
	return ""
try:
	f=open(sys.argv[1],'r')
	for line in f:
		if line.strip():
			print FindWriter(line.strip())
except Exception as e:
	print e.message
	sys.exit(1)
sys.exit(0)