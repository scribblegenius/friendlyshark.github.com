import sys
import math
from math import sqrt
def palindrome(word):
	return word==word[::-1]# compare word to its reverse
Limit=1000
if(Limit==2):
	print Limit
	sys.exit(0)
if(Limit<2):
	sys.exit(1)#error
N=Limit+1
primes = [True] * N
# Cross out the evens
i=3
while(i<N):
	if i%2 == 0:
		primes[i]=False;
	i=i+1
i = 3
while(i<math.sqrt(N)):
	j=i
	multiple=i
	while(multiple+j<N):
		multiple=multiple+j
		primes[multiple]=False
	i=i+1
for index,x in reversed(list(enumerate(primes))):
	if palindrome(str(index)) and x==True:
		print index
		break
sys.exit(0)
	