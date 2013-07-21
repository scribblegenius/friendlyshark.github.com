import sys
try:
	f=open(sys.argv[1],'r')
	for line in f:
		print int(line.strip(),16)
except:
	sys.exit(1)
sys.exit(0)