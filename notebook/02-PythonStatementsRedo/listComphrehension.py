#ListComprehensions
lst = [x for x in 'word']
print(lst)
#['w', 'o', 'r', 'd']

lst = [x**2 for x in range(0,11)]
print(lst)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)
#[0, 2, 4, 6, 8, 10]
