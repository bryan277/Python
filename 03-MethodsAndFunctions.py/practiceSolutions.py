#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        #BOTH NUMBERS ARE EVEN!
        if a < b:
            result = a
        else:
            result = b
    else:
        # ONE OR BOTH NUMBERS ARE ODD!
        if a > b:
            result = a
        else:
            result = b

    return result


print(lesser_of_two_evens(2,4))
#2
print(lesser_of_two_evens(7,5))
#7


#Other method max and min

def lesserOfTwoEvens(a,b):
    if a%2 == 0 and b%2 == 0:
        #BOTH NUMBERS ARE EVEN!
        result = min(a,b)
    else:
        result = max(a,b)

    return result

print(lesserOfTwoEvens(2,4))
#2
print(lesserOfTwoEvens(7,5))
#7

#Even more slickier
# def lesserOfTwoEvens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         #BOTH NUMBERS ARE EVEN!
#         return min(a,b)
#     else:
#         return max(a,b)
#
#
# print(lesserOfTwoEvens(2,4))
# #2
# print(lesserOfTwoEvens(7,5))
# #7

def animal_crackers(text):
    wordlist = text.lower().split()
    #you can also use upper case and it would still worked

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

#Same method only cleaner
# def animal_crackers(text):
#     wordlist = text.split()
#
#     return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelheaded Llama'))
#True
print(animal_crackers('Crazy Kangaroo'))
#False
print(animal_crackers('Hans hans'))
#True with lower()
print(animal_crackers('Help me'))
#False

def makes_twenty(n1,n2):

    return (n1 + n2) == 20 or n1==20 or n2==20
    # code above is the same as code below
    # if n1 + n2 == 20:
    #     return True
    # elif n1 == 20:
    #     return True
    # elif n2 == 20:
    #     return True
    # else:
    #     return False

print(makes_twenty(10,10))
#True
print(makes_twenty(20,12))
#True
print(makes_twenty(10,22))
#False

#level 1 problems
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#First method
def old_macdonald(name):

    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

print(old_macdonald('macdonald'))
#MacDonald

def old_macdonald(name):

    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))
#MacDonald

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return print(' '.join(reverse_word_list))

master_yoda('I am home')
#home am I
master_yoda('We are ready')
#ready are We

#join method
mylist = ['a','b','c']
print('--'.join(mylist))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
# abs(num) returns the absolute value of a number

def almost_there(n):

    return print((abs(100-n) <= 10) or (abs(200-n) <= 10))

almost_there(104)
#True
almost_there(150)
#False
almost_there(209)
#True

#Level 2 problems
#FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):

    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True

    return False

print(has_33([1,3,1,3]))
#False
print(has_33([1,3,3]))
#True
print(has_33([3,1,3]))
#False

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶

def paper_doll(text):
    result = ''

    for char in text:
        result += char*3
    return print(result)

paper_doll('Hello')
#HHHeeellllllooo
paper_doll('Mississippi')
#MMMiiissssssiiissssssiiippppppiii


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):

    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return "BUST"

print(blackjack(5,6,7))
#18
print(blackjack(9,9,9))
#BUST
print(blackjack(9,9,11))
#19
