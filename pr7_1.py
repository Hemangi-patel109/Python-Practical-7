# Write a python program to read the text file using read (), readlines() and readline() methods.

fo = open('foo.txt','r')
print("Using read():",fo.read())
fo.close()
fo = open('foo.txt','r')
print("Using readlines():",fo.readlines())
fo.close()
fo = open('foo.txt','r')
print("Using readline():",fo.readline())
fo.close()
