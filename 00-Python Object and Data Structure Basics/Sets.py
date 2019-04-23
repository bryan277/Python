myset = set()
myset.add(1)
print(myset)
# {1}
myset.add(2)
print(myset)
# {1, 2}
myset.add(2)
print(myset)
# {1, 2} i doesnt change because it is set and it only accepts unique values

mylist = [3,3,3,3,5,5,2,2,2]
setting = set(mylist)
print(setting)
# {2, 3, 5}

d = 'Mississippi'
print(set(d))
# {'p', 'M', 's', 'i'}
