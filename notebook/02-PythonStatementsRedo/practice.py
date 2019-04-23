#if, elif, else
x = False

if x:
    print('x was true!')
else:
    print('I will be printed in any case where x is not true')
#I will be printed in any case where x is not true

loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')
#Welcome to the bank!

person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")
#Welcome Sammy!

person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person == 'George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")
#Welcome George!

#For loops
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print(17 % 5)
#2
print(10 % 3)
#1
print(18 % 7)
#4
print(4 % 2)
#0

for num in list1:
    if num % 2 == 0:
        print(num)
# 2
# 4
# 6
# 8
# 10

for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')
# Odd number
# 2
# Odd number
# 4
# Odd number
# 6
# Odd number
# 8
# Odd number
# 10

for letter in 'This is a string.':
    print(letter)
# T
# h
# i
# s
#
# i
# s
#
# a
#
# s
# t
# r
# i
# n
# g
# .

tup = (1,2,3,4,5)

for t in tup:
    print(t)
# 1
# 2
# 3
# 4
# 5

list2 = [(2,4), (6,8), (10, 12)]

for tup in list2:
    print(tup)
# (2, 4)
# (6, 8)
# (10, 12)

for (t1, t2) in list2:
    print(t1)
# 2
# 6
# 10

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)
# k1
# k2
# k3

print(d.items())
# dict_items([('k1', 1), ('k2', 2), ('k3', 3)])

for k,v in d.items():
    print(k)
    print(v)

# k1
# 1
# k2
# 2
# k3
# 3

print(list(d.keys()))
#['k1', 'k2', 'k3']

print(sorted(d.values()))
# [1, 2, 3]

#Useful operators
print(list(range(0,11)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0,11,2)))
#[0, 2, 4, 6, 8, 10]
print(list(range(0,101,10)))
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

#enumerate
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

print(list(enumerate('abcde')))
#[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

#zip
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

print(list(zip(mylist1,mylist2)))
#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item1, item2 in zip(mylist1, mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1, item2))
# For this tuple, first item was 1 and second item was a
# For this tuple, first item was 2 and second item was b
# For this tuple, first item was 3 and second item was c
# For this tuple, first item was 4 and second item was d
# For this tuple, first item was 5 and second item was e

print('x' in ['x', 'y', 'z'])
#True
print('x' in [1,2,3])
#False

#min and max
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))
# 10
# 100

#random
from random import shuffle
#This shuffles the list 'in-place' meaning it won't return
#anyting, instead it will effect the list passed
shuffle(mylist)
print(mylist)
#[40, 10, 20, 30, 100]

from random import randint
print(randint(0,100))
#37
print(randint(0,100))
#56

#input
input('Enter Something into this box: ')
