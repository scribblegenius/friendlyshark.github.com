import sys
def printspace(num):
	spaces = ' ' * (4-num)
	return spaces
try:
	for i in range(1,13):
		flag=True
		for j in range(1,13):
			product=str(i*j)
			length = len(product)
			if flag==True:
				print printspace(length+2) + product,
				flag=False
			else:
				print printspace(length) + product,
		print "\r"
except:
	sys.exit(1)
sys.exit(0)