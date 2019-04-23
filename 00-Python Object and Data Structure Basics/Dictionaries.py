my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])
# value1
prices_lookup = {'apple': 2.99, 'orange': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])
# 2.99

d = {'k1':['a','b','c'], 'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d['k2'])
#[0,1,2]
print(d['k3']['insideKey'])
#100
print(d['k3'])
# {'insideKey': 100}
print(d['k2'][2])
# 2
mylist=d['k2']
print(mylist)
# [0,1,2]
mylist1=d['k1']
print(mylist1)
# [a,b,c]
letter = mylist1[2]
print(letter)
# c
print(letter.upper())
# C
print(mylist)
print(d['k1'][2].upper())

print(d['k3'])
# {'insideKey': 100}
print(d['k3']['insideKey'])
# 100


d = {'k1': 100, 'k2':200}
d['k3'] = 300
print(d)
# {'k1': 100, 'k2': 200, 'k3': 300}

d['k1'] = 'NEW VALUE'
print(d)
# {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
# dict_keys(['k1', 'k2', 'k3'])
print(d.values())
# dict_values([100, 200, 300])
print(d.items())
# dict_items([('k1', 100), ('k2', 200), ('k3', 300)])
