import sys
try:
	f=open(sys.argv[1],'r')
	for line in f:
		print line.lower()
except:
	sys.exit(1)
sys.exit(0)