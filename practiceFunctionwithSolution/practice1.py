#1. Write a Python function to find the Max of three numbers. Go to the editor
#mysolution
threeNumber = [1,2,3]

def maxNumber(x,y,z):
    return max(x,y,z)

print(maxNumber(5,3,2))
#5

#theirsolution
def max_of_two(x,y):
    if x > y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

print(max_of_three(3,6,-5))
#6

#2. Write a Python function to sum all the numbers in a list
numList = (8,2,3,0,7)

def sumAllNumbers(num):
    total = 0
    for x in num:
        total += x
    return total


print(sumAllNumbers(numList))
#20

#other solution
def Sum():
    a = [8,2,3,0,7]
    print(sum(a))

Sum()
#20

#3. Write a Python function to multiply all the numbers in a list. Go to the editor
numList1 = [8, 2, 3, -1, 7]

def multiplyAllNumbers(num):
    total = 1
    for x in num:
        total *= x
    return total

print(multiplyAllNumbers(numList1))
#-336

#other solution

#4. Write a Python program to reverse a string.
sampleString = '1234abcd'

def reverse(string):
    return print(string[::-1])

reverse(sampleString)
#dcba4321

#other mysolution
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index -1 ]
        index = index -1
    return rstr1
print(string_reverse(sampleString))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. Go to the editor

#6. Write a Python function to check whether a number is in a given range
def test_range(n):
    if n in range(3,9):
        print(" %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")
test_range(5)
# 5 is in the range

#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor

sampleString1 = 'The quick Brow Fox'

def lowerUpper(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])

lowerUpper('The quick Brow Fox')
# No. of Upper case characters :  3
# No. of Lower case Characters :  12

#other mysolution

#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def sortNumber(num):
#     uniqueList = []
#     for sort in num:
#         if sort not in uniqueList:
#             uniqueList.append(sort)
#     return uniqueList
#
# print(sortNumber([1,2,3,3,3,3,4,5]))

#
# def unique_List(l):
#   x = []
#   for a in l:
#         if a not in x:
#             x.append(a)
#         return x
#
# print(unique_List([1,2,3,3,3,3,4,5]))

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))
