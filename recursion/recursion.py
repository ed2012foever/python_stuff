#!/usr/bin/python

def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:])

K = [1]

total = mysum(K)

print(total)

