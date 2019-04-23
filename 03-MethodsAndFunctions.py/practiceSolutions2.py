#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b

    return result


print(lesser_of_two_evens(2,4))
#2
print(lesser_of_two_evens(10,22))
#10
print(lesser_of_two_evens(20,2))
#2
print(lesser_of_two_evens(12,13))
#13

def lesserOfTwoEvens(a,b):
    if a%2 == 0 and b%2 == 0:
        #BOTH NUMBERS ARE EVEN!
        result = min(a,b)
    else:
        result = max(a,b)

    return result

# def lesserOfTwoEvens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else
#         return max(a,b)

# print(lesserOfTwoEvens(2,4))
# #2
# print(lesserOfTwoEvens(7,5))
# #7

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#     wordlist = text.lower().split()
#
#     firstWord = wordlist[0]
#     secondWord = wordlist[1]
#
#     return firstWord[0] == secondWord[0]
#
# print(animal_crackers('Hans hans'))
# #True
# print(animal_crackers('jason born'))
# #False

#Cleaner method
def animal_crackers(text):
    wordlist = text.lower().split()

    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Hans hans'))
# #True
print(animal_crackers('jason born'))
# #False


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False

print(makes_twenty(10,10))
#True
print(makes_twenty(20,12))
#True
print(makes_twenty(10,22))
#False

#shorter way
# def makes_twenty(n1, n2):
#
#     return (n1 + n2) == 20 or n1==20 or n2==20
#
# print(makes_twenty(10,10))
# #True
# print(makes_twenty(20,12))
# #True
# print(makes_twenty(10,22))
# #False

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#('macdonald') --> MacDonald

def old_macdonald(name):

    first_letter = name[0]
    middle = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return print(first_letter.upper() + middle + fourth_letter.upper() + rest)

old_macdonald('macdonald')

# MacDonald

def up_low(s):
    d={"upper":0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case characters : ", d["lower"])

s = 'Hello Mr.Rogers, how are you this fine Tuesday?'
up_low(s)

##Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
        return x

print(unique_list([1,1,1,1,1,2,2,3,3,3,4,5,]))

#Write a Python function to mulitply all the numbers in a list
def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total

sampleList= [1,2,3,-4]
print(multiply(sampleList))
#-24

#Write a Python function that checks whether a passed in string is plaindrome or not
def palindrome(s):
    return print(s == s[::-1])


palindrome('helleh')
#True
palindrome("hallo")
#False
