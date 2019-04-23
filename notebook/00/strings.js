#STRING INDEXING
s = 'Hello World'
print(s)
# Hello World
h = s[0]
print(h)
#H
print(s[1:])
#ello World
print(s[:3])
#Hel
print(s[:])
#Hello World
print(s[-1])
#d
print(s[:-1])
#Hello World
print(s[::1])
#Hello World #Grab everyting, but go in steps size of 1
print(s[::2])
#HloWrd
print(s[::-1])
#dlroW olleH

#STRING PROPERTIES
# s[0] = 'x'
# #Traceback (most recent call last):
#   File "strings.js", line 26, in <module>
#     s[0] = 'x'
# TypeError: 'str' object does not support item assignment
print(s + ' concatenate me!')
# Hello World concatenate me!
s = s + ' concatenate me!'
print(s)
# Hello World concatenate me!

letter = 'z'
print(letter * 10)
# zzzzzzzzzz
print(s.upper())
#HELLO WORLD CONCATENATE ME!
print(s.lower())
#hello world concatenate me!
print(s.split())
#['Hello', 'World', 'concatenate', 'me!']
print(s.split('W'))
#['Hello ', 'orld concatenate me!']
print('Insert another string with curly brackets: {}'.format('The inserted string'))
#Insert another string with curly brackets: The inserted string
