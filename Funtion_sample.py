#!/usr/bin/python

print('Hello World')

def times(x, y):
	return x * y

result = times('A', 5)
print(result)

def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res

s1 = 'SPAM'
s2 = 'SCAM'

result = intersect(s1, s2)
print(result)

