for num in range(3,10):
    print(num)
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for number in range(0,10,2):
    print(number)
# 2
# 4
# 6
# 8

print(list(range(0,11,2)))
# [0,2,4,6,8,10]

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e


count_index = 0

for let in 'abcde':
    print('At index {} the letter is {}'.format(count_index, let))
    count_index += 10
# At index 0 the letter is a
# At index 10 the letter is b
# At index 20 the letter is c
# At index 30 the letter is d
# At index 40 the letter is e

indexCount = 0
word = 'abcde'
for letter in word:
    print(word[indexCount])
    indexCount += 1

word = 'abcde'

for item in enumerate(word):
    print(item)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)
#(1, 'a')
#(2, 'b')
#(3, 'c')

print(list(zip(mylist1, mylist2)))
#[(1, 'a'), (2, 'b'), (3, 'c')]

print('x' in [1,2,3])
#False

print('x' in ['x', 'y', 'z'])
#True

print('mykey' in {'mykey': 345})
#True

d = {'mykey': 345}
print(345 in d.values())
#True
print(345 in d.keys())
#False
print('mykey' in d.keys())
#True

mylist = [10, 20, 30, 40, 100]
print(min(mylist))
# 10
print(max(mylist))
#100

from random import shuffle
mylist3 = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist3)
print(mylist3)
#[9, 6, 8, 2, 7, 5, 1, 10, 3, 4]
from random import randint
print(randint(0,100))
#69
myrandom = randint(0,100)
print(myrandom)
#71

result = input('What is your name? ')
print(result + " is the best")
print(type(result))
