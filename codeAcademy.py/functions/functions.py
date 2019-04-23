

def tax(bill):
    """Adds 8% tax to a restaurant
    bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

print(tax(2.00));
# With tax: 2.160000
# 2.16

def tip(bill):
    """Adds 15% tip to a restaurant
    bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
# With tax: 108.000000
# With tip: 124.200000

def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." %(n, squared))
    return result

square(10)
#10 squared is 100.

def power(base, exponent):
    result = base ** exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))


power(37, 4)
# 37 to the power of 4 is 1874161.

def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7

print(fun_two(5))
#32

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2


print(deserves_another(3))
#6

def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING""
    else
        return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


def cube(number):
    return number * number * number

print(cube(2))

def by_three(number):
    if number % 3 == 0:
        print (cube(number))
    else:
        print (False)

print(by_three(3))
#27
print(by_three(4))
#False
print(by_three(6))
#216
