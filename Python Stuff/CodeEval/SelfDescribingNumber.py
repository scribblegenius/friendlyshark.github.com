import sys
def isSelfDescribing(number):
	dict={}
	#print number
	for index,x in enumerate(number):
		if str(index) not in dict:
			dict[str(index)]=0
		if x in dict:
			dict[x]=int(dict[x])+1
		else:
			dict[x]=1
	#print dict
	for key in dict:
		 if str(dict[key])!=str(number[int(key)]):
		 	return 0
	return 1
try:
	f=open(sys.argv[1],'r')
	for line in f:
		print isSelfDescribing(line.strip())
except:
	sys.exit(1)
sys.exit(0)