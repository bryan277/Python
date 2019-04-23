t = (1,2,3)
mylist = [1,2,3]
print(type(t))
# <class 'tuple'>
print(type(mylist))
# <class 'list'>
print(len(t))
# 3
print(t)
# (1,2,3)
print(t[0])
# 1
print(t[-1])
# 2
t = ('a', 'a', 'b', 'a')
print(t.count('a'))
# 3
print(t.index('a'))
# 0
print(t.index('b'))
# 2

mylist[0] = 'NEW'
print(mylist)
# ['NEW', 2, 3]
t[0] = 'NEW'
# # Traceback (most recent call last):
#   File "Tuples.py", line 26, in <module>
#     t[0] = 'NEW'
# TypeError: 'tuple' object does not support item assignment
