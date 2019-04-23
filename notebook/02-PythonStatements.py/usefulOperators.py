print(list(range(0,11)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10,20)))
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(0,11,2)))
#[0, 2, 4, 6, 8, 10]
print(list(range(0,101,10)))
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

for i, letter in enumerate('abcde'):
    print('At index {} the letter is {}'.format(i,letter))
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

print(list(enumerate('abcde')))
#[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

print(zip(mylist1,mylist2))
#<zip object at 0x101a0f248>

print(list(zip(mylist1,mylist2)))
#[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item1, item2 in zip(mylist1, mylist2):
    print('For this tuple, first item was {} and second item was {}'.format(item1, item2))
# For this tuple, first item was 1 and second item was a
# For this tuple, first item was 2 and second item was b
# For this tuple, first item was 3 and second item was c
# For this tuple, first item was 4 and second item was d
# For this tuple, first item was 5 and second item was e

print('x' in ['x','y','z'])
#true
print('x' in [1,2,3])
#False

mylist = [10,20,30,40, 100]
print(min(mylist))
#10
print(max(mylist))
#100

from random import shuffle
shuffle(mylist)
print(mylist)
#[100, 10, 30, 20, 40]

from random import randint
print(randint(0,100))
#31

print(randint(0,100))
#99

print(input('Enter Something into this box: '))
