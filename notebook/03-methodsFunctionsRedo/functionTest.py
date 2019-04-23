#Function Practice Exercises

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

    return print(result)

lesser_of_two_evens(2,4)
#2
lesser_of_two_evens(2,5)
#5

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    #['hans','hempton']
    first = wordlist[0]
    print(first)
    #hans
    second = wordlist[1]
    print(second)
    #hempton
    print(first[0], second[0])
    # h h

    return print(first[0] == second[0])

animal_crackers('Hans hempton')
#True
