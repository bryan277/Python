my_list = [1,2,3]
print(my_list[0])
#1
print(my_list[1:])
#[2,3]
print(my_list[:3])
#['one','two','three']
print(my_list + ['new item'])
#[1, 2, 3, 'new item']
print(my_list)
#[1,2,3]
my_list = my_list + ['add new item permanently']
print(my_list)
#[1, 2, 3, 'add new item permanently']
print(my_list*2)
#[1, 2, 3, 'add new item permanently', 1, 2, 3, 'add new item permanently']
list1 = [1,2,3]
list1.append('append me!')
print(list1)
#[1, 2, 3, 'append me!']
list1.pop(0)
print(list1)
#[2, 3, 'append me!']
popped_item = list1.pop()
print(popped_item)
#'append me!'
print(list1)
#[2,3]

new_list = ['a','e','x','b','c']
new_list.reverse()
print(new_list)
#['c', 'b', 'x', 'e', 'a']
new_list.sort()
print(new_list)
#['a', 'b', 'c', 'e', 'x']
list3
