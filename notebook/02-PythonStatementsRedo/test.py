st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)
# start
# s
# sentence

print(list(range(0,10)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = [x for x in range(0,51) if x % 3 == 0]
print(x)
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word+"<-- has an even length!")
# word<-- has an even length!
# in<-- has an even length!
# this<-- has an even length!
# sentence<-- has an even length!
# that<-- has an even length!
# an<-- has an even length!
# even<-- has an even length!
# number<-- has an even length!
# of<-- has an even length!

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
