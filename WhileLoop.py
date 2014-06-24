#!/usr/bin/python

import sys

if sys.version[0] == '2': input = raw_input # 2.X compatible

while True:
	reply = input('Enter text: ')
	if reply == 'stop': 
		break
	try:
		print(float(reply) ** 2)
	except:
		print('Bad!' * 8)
print('Bye')

