import sys
def isHappy(number):
	dict={}
	while str(number) not in dict.keys():
		dict[str(number)]=1
		total=0
		for digit in str(number):
			total = total + int(digit)*int(digit)
		if total == 1:
			return True
		number = total
	return False
try:
	f=open(sys.argv[1],'r')
	for line in f:
		if line:
			if isHappy(int(line.strip())):
				print 1
			else:
				print 0
except Exception as e:
	print e.message
	sys.exit(1)
sys.exit(0)