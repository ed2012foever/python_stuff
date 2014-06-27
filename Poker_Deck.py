#!/usr/bin/python

value = range(13)
suit = ['clubs', 'diamonds', 'hearts', 'spades']

L = []

for i in suit:
	for k in value:
		card = (k, i)
		L.append(card)

for i in L:
	print(i)
