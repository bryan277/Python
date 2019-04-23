print('hi')

# print('I'm going on a run')
# use double quates to fix this

print('hello \n world')
print(len('hi'))
#2
print(len('three'))
#5


# indexing
mystring = "Hello WOrld"
print(mystring)
#Hello WOrld
print(mystring[0])
#H
print(mystring[8])
#r
print(mystring[-1])
#l

mystring = 'abcdefhijk'
print(mystring[2:])
#cdefhijk
print(mystring[:3])
#abc
print(mystring[3:6])
#def
print(mystring[1:3])
#bc
print(mystring[::])
#abcdefhijk
print(mystring[::2])
#acehj
print(mystring[2:7:2])
#ceh
print(mystring[::-1])
#kjihfedcba
print(mystring[::-2])
#kifdb

#Immutability
name = "Sam"
last_letters = name[1:]
print(last_letters)
# am
print('P' + last_letters)
# Pam
# String coca
x = 'P' + last_letters
print(x)
# Pam

letter = 'z'
print(letter * 10)
# zzzzzzzzzz

x = 'Hello World'
y = x.upper()
print(y)
# HELLO WORLD

lowerLetter = 'HELLO WORLD'
a = lowerLetter.lower()
print(a)
# hello world

split = 'Hello world'
b = split.split()
print(b)
# ['Hello' , 'world']

abc  = 'Hi this is a string'
cba = abc.split()
i = abc.split('i')
print(cba)
#['Hi', 'this', 'is', 'a', 'string']
print(i)
#['H', ' th' ,'s ', 's a str', 'ng']
