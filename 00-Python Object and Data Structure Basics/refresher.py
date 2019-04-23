#dictionary
my_dict = {'key1':'value1', 'key2': 'value2'}
print(my_dict)
#{'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])
#value1
letter = my_dict['key1']
print(letter.upper())
#VALUE1
my_dict['key3'] = 'value3'
print(my_dict)
#{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict['key1'] = 'NEW VALUE'
print(my_dict)
#{'key1': 'NEW VALUE', 'key2': 'value2', 'key3': 'value3'}
print(my_dict.keys())
#dict_keys(['key1', 'key2', 'key3'])
print(my_dict.values())
#dict_values(['NEW VALUE', 'value2', 'value3'])


#format
print('This is a string {}'.format('INSERTED'))
#This is a string INSERTED
print('The {} {} {}'.format('fox', 'brown','quick'))
#The fox bronw quick
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#The quick bronw fox
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
#The fox fox fox
print('The {q} {b} {q}'.format(f='fox', b='brown', q='quick'))
#The quick brown quick


result = 100/777

name = "Jose"
age = 3

print('The result was {r: 1.3f}'.format(r = result))
## The result was 0.129
print('The result was {r:1.5f}'.format(r = result))
#The result was 0.12870
print(f'Hello, his name is {name} and my age is {age} years old')
#Hello, his name is Jose and my age is 3 years old

mylist = ['one', 'two', 'three']
print(mylist[0])
#one
another_list = ['four', 'five']
print(mylist + another_list)
#['one', 'two', 'three', 'four', 'five']
new_list = mylist + another_list
new_list[0] = 'zero'
print(new_list)
#['zero', 'two', 'three', 'four', 'five']
num_list = [4,1,8,3]
print(num_list.sort())
#None
num_list.sort()
print(num_list)
#[1,3,4,8]
num_list.reverse()
print(num_list)
#[8, 4, 3, 1]
