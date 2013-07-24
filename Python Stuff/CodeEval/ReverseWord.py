import sys
def reverseline(line):
	revline= reversed(list(line.split(" ")))
	revvedline=""
	for x in revline:
		revvedline=revvedline+" "+x.strip()
	return revvedline.strip()
try:
	f=open(sys.argv[1],'r')
	for line in f:
		print reverseline(line)
except:
	sys.exit(1)
sys.exit(0)
	