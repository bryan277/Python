def biggest_number(*args):
    print (max(args))
    return max(args)

def smallest_number(*args):
    print (min(args))
    return min(args)

def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
# 10
# -10
# 10

maximum = max(1,2,3,4)

print(maximum)
#4

minimum = min(1,2,3,4)

print(minimum)
#1

absolute = abs(-42)

print(absolute)
#42

print(type(42))
# <class 'int'>
print(type(4.2))
print(type('string'))
# <class 'float'>
# <class 'str'>


def shut_down(s):
    if s == "yes":
        return print("Shutting down")
    elif s == "no":
        return print("Shutdown aborted")
    else:
        return print("Sorry")

shut_down("yes")
#Shutting down
shut_down("no")
# "Shutdown aborted"
shut_down("")
# Sorry

def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return print(abs(num))
    else:
        return print("Nope")

distance_from_zero(2)
#2
distance_from_zero(-10)
#10
distance_from_zero(-2.2)
#2.2
