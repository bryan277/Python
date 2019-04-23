t = (1,2,3)
print(len(t))
# 3

t = ('one', 2)
print(t)
# ('one', 2)

print(t[0])
# 'one'

print(t[-1])
# 2

# Basic Tuple Methods
print(t.index('one'))
# 0
print(t.count('one'))
# 1    Use .count to count the number of times a value appears

t[0] = 'change
print(t[0])
# Traceback (most recent call last):
#   File "Tuples.py", line 21, in <module>
#     t[0] = 'change'
# TypeError: 'tuple' object does not support item assignment

print(t.append('nope'))
#  File "Tuples.py", line 21
#     t[0] = 'change
#                  ^
# SyntaxError: EOL while scanning string literal
