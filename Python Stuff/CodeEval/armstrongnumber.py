import sys
import math
def isArmstrong(number):
	if len(str(number))==1:
		return True
	sum=0
	Len= len(str(number))
	for x in number:
		sum =  sum + math.pow(int(x),Len)
	return int(number) == sum
try:
	f=open(sys.argv[1],'r')
	for line in f:
		print isArmstrong(line.strip())
except:
	sys.exit(1)
sys.exit(0)