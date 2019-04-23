st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)

# start
# s
# sentence

#Use range() to print all the even numbers from 0 to 10.
print(list(range(0,11)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
lst = [x for x in range(1,50,3)]
print(lst)
#[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49]

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word + ' is even')

# word is even
# in is even
# this is even
# sentence is even
# that is even
# an is even
# even is even
# number is even
# of is even

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
numList = range(0,101)

for num in numList:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in letter.split()])

# for letter in st.split():
#     print(letter[0])
