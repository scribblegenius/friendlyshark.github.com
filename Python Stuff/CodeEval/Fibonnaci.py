import sys
try:
	fibo = {}
	def fib(n):
		if n==0 or n ==1:
			return n
		elif n in fibo:
			return fibo[n]
		else:
			fibo[n]=fib(n-1)+fib(n-2)
			return fibo[n]
	f=open(sys.argv[1],'r')
	for line in f:
		number = int(line.strip())
		if number < 0:
			sys.exit(0)
		print fib(number)
except e:
	sys.exit(1)
sys.exit(0)