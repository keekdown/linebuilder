import numpy as np
def fact(n):
	if n == 0:
		return 1
	else:
		return fact(n-1)*n

def B(t,P):
	fromN_on_I = (lambda n,i:(fact(n)/(fact(i)*fact(n-i))))
	return np.sum(P[i]*(fact2(len(P)-1,i)*(t**i)*((1-t)**(len(P)-i - 1))) for i in range(len(P)))

def fact2(n,i):
	if i == 0:
		return 1
	if n-i + 1 == n+1:
		return n
	if n == i:
		return 1
	else:
		up=np.multiply.accumulate(np.arange(n-i + 1,n+1))[-1]
		#print(up)
		down=fact(i)
		return up/down
fromN_on_I = (lambda n,i:(fact(n)/(fact(i)*fact(n-i))))
#print(fact2(1000,5))
#print(fromN_on_I(1000,5))