#!/usr/bin/python

print('Hello World!')

myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')

myfile.close()

myfile = open('myfile.txt')
line1=myfile.readline()
print(line1, end='')
line2=myfile.readline()
print(line2, end='')
line3=myfile.readline()
print(line3, end='')

print('Iterating over file')

for line in open('myfile.txt'):
	print(line, end='')

