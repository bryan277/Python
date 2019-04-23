mylist = ['one', 'two', 'three']
print(mylist[0])
# 'one'
print(mylist[1:])
# ['two', 'three']
another_list = ['four', 'five']
print(mylist + another_list)
# ['one', 'two', 'three', 'four', 'five']
new_list = mylist + another_list
print(new_list)
# ['one', 'two', 'three', 'four', 'five']
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
new_list.append('seven')
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']
popped_item = new_list.pop()
print(popped_item)
# seven
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
new_list.pop(0)
print(new_list)
# ['two', 'three', 'four', 'five', 'six']
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)
# ['a', 'b', 'c', 'e', 'x']
num_list.sort()
print(num_list)
# [1, 3, 4, 8]

num_list.reverse()
print(num_list)
# [8, 4, 3, 1]
