st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
# start
# s
# sentence


print(list(range(0,10,2)))
#[0, 2, 4, 6, 8]

print([x for x in range(1,51) if x%3 == 0])
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word + ' has even length')

numList = range(1,101)

for num in numList:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

letter = 'Create a list of the first letter of every word in this string'
print([word[0] for word in letter.split()])
#['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
