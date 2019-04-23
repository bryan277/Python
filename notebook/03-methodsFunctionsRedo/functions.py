def say_hello():
    print('hello')

say_hello()
#hello

def greeting(name):
    print('Hello %s' %(name))

greeting('Jose')
#Hello Jose

def add_num(num1, num2):
    return num1 + num2

add_num(4,5)
#9

result = add_num(4,5)
print(result)
#9

print(add_num('one', 'two'))
#onetwo

def is_prime(num):

    for n in range(2,num):
        if num % n == 0:
            print(num, 'is not prime')
            break
        else:
            print(num, 'is prime!')

is_prime(16)
#16 is not prime
is_prime(17)
#17 is prime!
