def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05


print(myfunc(40,60,100))
#10
print(myfunc(40,60))
#5

def myfunc(*args):
    return sum(args) * 0.05

myfunc(40,60,100,1,34)
#11.75

def myfunc(*args):
    print(args)

myfunc(40,60,100,1,34)
#(40, 60, 100, 1, 34)


def myfunc(*args):
    for item in args:
        print(item)

myfunc(40,60,100,1,34)
# 40
# 60
# 100
# 1
# 34

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
#{'fruit': 'apple', 'veggie': 'lettuce'}
myfunc(fruit='apple', veggie='lettuce')
#My fruit of choice is apple


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')
# (10, 20, 30)
# {'fruit': 'orage', 'food': 'eggs', 'animal': 'dog'}
# I would like 10 eggs

def myfunc(*arg):
    lst = [] # creating a list to store further values
    for i in arg:
        if i % 2 == 0:
            lst.append(i) # appending the even value

    return lst # returning the list with all elements

myfunc(4,5,6,7,8)
