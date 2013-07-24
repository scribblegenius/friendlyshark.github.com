import sys
def SumOfDigits(num):
	N=int(num)
	sum=0
	while(N!=0):
		sum=sum + (N%10)
		N=N%10	
	return sum
	try:
		f=open(argv[1],'r')
		for n in f:
			print n
			print SumOfDigits(n.strip())
	except:
		sys.exit(1)
sys.exit(0)