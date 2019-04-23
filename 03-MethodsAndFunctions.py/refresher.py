def name_function():
    '''
    Information
    '''
    print('hello')

def say_hello(name):
    print('hello ' + name)

say_hello('Hans')

def hello(name='Bryan'):
    print('hello ' + name)

hello()
#hello Bryan
hello('Hans')

def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check('My dog ran away'))
#True
print(dog_check('My cat ran away'))
#False
print(dog_check('My Dog ran away'))
#True because of mystring.lower()

def pig_latin(word):

    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

print(pig_latin('apple'))
#appleay

def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y

print(myfunc('Hello', say_hello('Bryan'), False))



def ran_check(num, low, high):
    if num in range(low, high):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')

ran_check(5,2,7)


name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy'

    def hello():
        name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()

greet()

x = 50

def func(x):

    print(f'X is {x}')

    x= 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x

print(x)
#50

x = func(x)
#X IS 50


def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    #['crazy' 'Kangaroo']
    first = wordlist[0]
    second = wordlist[1]
    print(first)
    #crazy
    print(second)
    #Kangaroo
    print(first[0])
    #c
    print(second[0])
    #k
    return first[0] == second[0]

print(animal_crackers('Crazy Kangaroo'))
#False

#Cleaner method
# def animal_crackers(text):
#     wordlist = text.lower().split()
#
#     return wordlist[0][0] == wordlist[1][0]
