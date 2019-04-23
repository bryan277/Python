my_dict = {'key1': 'value1',
           'key2': 'value2',
           'key3': 'value3'}

print(my_dict['key2'])
# value2
my_dict = {'key1':123, 'key2':[12,23,33],'key3':['item0','item2', 'item3']}

print(my_dict['key3'])
# ['item0', 'item2', 'item3']
print(my_dict['key3'][0])
# item0
print(my_dict['key3'][0].upper())
# ITEM0
print(my_dict['key1'])
# 123
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])
# 0

my_dict['key1'] -= 123
my_dict['key1']

print(my_dict['key1'])
# -123

d = {}

d['animal'] = 'Dog'
d['answer'] = 42
print(d)

#Nesting with dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1'])
# {'nestkey': {'subnestkey': 'value'}}
print(d['key1']['nestkey'])
# {'subnestkey': 'value'}
print(d['key1']['nestkey']['subnestkey'])
# value

# A few Dictionary Methods
d = {'key1':1, 'key2':2,'key3': 3}
print(d.keys())
# dict_keys(['key1', 'key2', 'key3'])
print(d.values())
# dict_values([1,2,3])
print(d.items())
# dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
