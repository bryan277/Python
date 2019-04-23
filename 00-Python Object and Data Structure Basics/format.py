print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED

print('The {} {} {}'.format('fox','brown','quick'))
# The fox brown quick

print('The {2} {1} {0}'.format('fox','brown','quick'))
# The quick brown fox

print('The {0} {0} {0}'.format('fox','brown','quick'))
# The fox fox fox

print('The {q} {b} {q}'.format(f='fox',b='brown',q='quick'))
# The quick brown fox


#Float formatting follows "{value:width.precision f}"
result = 100/777
# print(result)
#0.1287001387001287
print('The result was {r:1.3f}'.format(r = result))
# The result was 0.129
print('The result was {r:1.5f}'.format(r = result))
# The result was 0.12870

name = "Jose"
age = 3
print(f'Hello, his name is {name} and my age is {age} years old')
# Hello, his name is Jose
