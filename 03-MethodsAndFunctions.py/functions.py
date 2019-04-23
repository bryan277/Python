print('test')

def name_function():
    '''
    DOCSTRING: Information about the name_function
    INPUT: name_function
    OUTPUT: Hello ...
    '''
    print('Hello')

help(name_function)
# name_function()
#     DOCSTRING: Information about the name_function
#     INPUT: name_function
#     OUTPUT: Hello ...

def say_hello(name):
    print('hello ' + name)

say_hello('Hans')
#hello Hans

def hello(name='Bryan'):
    print('hello '+ name)

hello()
#hello Bryan
hello('Hans')
#hello Hans


def hi(name = 'Hans'):
    return 'hello ' + name

result = say_hello('Jose')
result
# 'hello Jose'

def add(r1, r2):
    return r1 + r2

result = add(20,30)
print(result)
# 50

# Find out if the word "dog" is in a string?

def dog_check(mystring):
    return 'dog' in mystring.lower()
    # if 'dog' in mystring.lower():
    #     return True
    # else:
    #     return False

print(dog_check('My dog ran away'))
# True
print(dog_check('My cat ran away'))
# False
print(dog_check('My Dog ran away'))
# True because of mystring.lower()

def pig_latin(word):

    first_letter = word[0]

    #check if vowel
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


print(myfunc('Hello','Goodbye',False))
#Goodbye

def myfunc(a,b):
    return a*b

def is_greater(c,d):
    if c > d:
        return True
    else:
        return False

print(is_greater(10,12))
#False
