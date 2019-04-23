my_list = [1,2,3]
print(len(my_list))
# 3

my_list = ['one', 'two', 'three', 4.5]
print(my_list[0])
# one
print(my_list[1:])
# ['two', 'three', 4.5]
print(my_list[:3])
# ['one', 'two', 'three']

print(my_list + ['new item'])
# ['one', 'two', 'three', 4.5, 'new item']
print(my_list)
# ['one', 'two', 'three', 4.5]
# This doesn't acutally change the original list!
my_list = my_list + ['add new item permanently']
#You would have reassign the list to make the change permanent
print(my_list)
# ['one', 'two', 'three', 4.5, 'add new item permanently']
print(my_list * 2)
# ['one', 'two', 'three', 4.5, 'add new item permanently', 'one', 'two', 'three', 4.5, 'add new item permanently']

#Indexing and Slicing
list1 = [1,2,3]

list1.append('append me')
print(list1)
#[1, 2, 3, 'append me']
list1.pop(0)
print(list1)
#[2, 3, 'append me']
popped_item = list1.pop()
print(popped_item)
# append me
print(list1)
# [2,3]

new_list = ['a', 'e', 'x', 'b', 'c']
new_list.reverse()
print(new_list)
# ['c', 'b', 'x', 'e', 'a']
new_list.sort()
print(new_list)
# ['a', 'b', 'c', 'e', 'x']

#Nesting List
list2 = [1,2,3]
list3 = [4,5,6]
list4 = [7,8,9]

matrix = [list2, list3, list4]
print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
# [1,2,3]
print(matrix[0][0])
# 1
print(matrix[0][1])
# 2

first_col = [row[0] for row in matrix]
print(first_col)
#[1, 4, 7]
