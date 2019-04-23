#Map function
def square(num):
    return num**2

# my_nums = [1,2,3,4,5]
# print(map(square,my_nums))
# #<map object at 0x10c1d5f98>

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

# 1
# 4
# 9
# 16
# 25

print(list(map(square,my_nums)))
#[1, 4, 9, 16, 25]

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve' , 'Sally']

print(list(map(splicer,names)))
#['EVEN', 'E', 'S']

#Filter function
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    print(n)

# def square(num):
#     result = num ** 2
#     return print(result)

#same as
square = lambda num: num ** 2

print(square(3))
#9

print(list(map(lambda num:num**2, mynums)))
#[1, 4, 9, 16, 25, 36]

print(list(filter(lambda num:num%2 == 0,mynums)))
#[2, 4, 6]

print(list(map(lambda name:name[0],names)))
#['A', 'E', 'S']

print(list(map(lambda x:x[::-1],names)))
