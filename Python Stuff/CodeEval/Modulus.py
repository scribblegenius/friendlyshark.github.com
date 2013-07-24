import sys
def Mod(N,M):
	if N<M:
		return N
	while N-M >= 0:
		N=N-M
	return N
try:
	f=open(sys.argv[1],'r')
	for line in f:
		array=(line.strip()).split(",")
		N=int(array[0])
		M=int(array[1])
		print Mod(N,M)
except:
	sys.exit(1)
sys.exit(0)