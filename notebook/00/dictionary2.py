my_dict = {'key1':'value1',
           'key2':'value2'}

print(my_dict['key2'])
#value2
my_dict = {'key1':123, 'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])
#['item0', 'item1', 'item2']
print(my_dict['key3'][0])
#item0
print(my_dict['key3'][0].upper())
#ITEM0
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])
#0
my_dict['key1'] -= 123
print(my_dict['key1'])
#-123

d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print(d)

d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(['key1'])
#{'animal': 'Dog', 'answer': 42}
print(d['key1']['nestkey']['subnestkey'])
#value

d = {'key1':1, 'key2': 2, 'key3': 3}
print(d.keys())
#dict_keys(['key1', 'key2', 'key3'])
print(d.values())
#dict_values([1, 2, 3])
print(d.items())
#dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
