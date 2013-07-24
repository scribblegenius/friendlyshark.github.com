import sys
try:
		f=open(sys.argv[1],'r')
		for line in f:
			numbers=line.split(",")
			B=bin(int(numbers[0]))[2::]
			index1=(int(numbers[1]))
			index2=(int(numbers[2]))
			print str((B[index1]==B[index2])).lower()
except:
	sys.exit(1)
sys.exit(0)
