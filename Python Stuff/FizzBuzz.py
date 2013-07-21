import sys
try:
	f = open(sys.argv[1],'r')
	for line in f:
		N = int(line.split(" ")[2])+1
		A = int(line.split(" ")[0])
		B = int(line.split(" ")[1])
		for x in range(1,N):
		    if x % (A*B) == 0:
		    	print "FB",
		    elif x % A ==0:
		    	print "F",
		    elif x % B==0:
		    	print "B",
		    else:
		    	print x,
		print "\r"
except:
	sys.exit(1)
sys.exit(0)