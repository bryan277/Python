#Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4/3)*(3.14)*(rad**3)


print(vol(2))

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check (num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

ran_check(5,2,7)
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def ran_bool(num, low, high):
    return num in range(low,high)

print(ran_bool(3,1,10))
#True
