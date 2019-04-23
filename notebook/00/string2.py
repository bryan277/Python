print('hello')

print(len('Hello World'))
#11
s = 'hello world'
print(len(s))
#11
print(s[0])
#'h'
print(s[1])
#'e'
print(s[1:])
#ello world
print(s[:3])
#'Hel'
print(s[:])
#'hello world'
print(s[-1])
#'d'
print(s[:-1])
#'hello worl'
print(s[::1])
#'hello world'
print(s[::2])
#'hlowrd'
print(s[::-1])
#''dlroW olleH'
print(s + ' concatenate me!')
#hello world concatenate me!
s = s + ' concatenate me!'
print(s)
letter = 'z'
print(letter*10)
#'zzzzzzzzzz'
print(s.upper())
#HELLO WORLD CONCATENATE ME!
print(s.lower())
#hello world concatenate me!
print(s.split())
#['hello', 'world', 'concatenate', 'me!']
print(s.split('w'))
#['hello ', 'orld concatenate me!']
