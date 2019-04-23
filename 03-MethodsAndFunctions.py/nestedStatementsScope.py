x = 25

def printer():
    x = 50
    return x

print(x)
#25
print(printer())
#50


# LEGB RULE:
# Local - Names assigned in any way within a function(def or lambda) and not declared global in that function
# lambda num:num**2

#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    #ENClOSING
    name = 'Sammy'

    def hello():
        #LOCAL
        name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()

greet()
# Hello IM A LOCAL
# name = 'Sammy' was commented out it would be Hello THIS IS A GLOBAL STRING

x = 50

def func(x):

    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X T0 {x}')
    return x

print(x)
#50

x = func(x)
#X IS 50
#I JUST LOCALLY CHANGED GLOBAL X TO NEW VALUE

print(x)
#NEW VALUE



#func(x)
#X is 50
# I JUST LOCALLY changed X T0 200
