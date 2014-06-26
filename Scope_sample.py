#!/usr/bin/python

X = 99

def func(Y):
	global Z
	Z = X + Y

func(2)
print(Z)

