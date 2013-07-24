import sys
def smallestmultipleofngreaterthanx(x,n):
	multiple=n
	while(multiple<x):
		multiple=multiple+n
	return multiple
try:
	f=open(sys.argv[1],'r')
	for line in f:
		list = line.split(",")
		print smallestmultipleofngreaterthanx((int)(list[0]),(int)(list[1]))
except:
	sys.exit(1)
sys.exit(0)