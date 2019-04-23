lst = [x for x in 'word']
print(lst)
#['w', 'o', 'r', 'd']

lst = [x**2 for x in range(0,11)]
print(lst)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst = [x for x in range(11) if x % 2 == 0]
print(lst)
#[0, 2, 4, 6, 8, 10]

celsius = [0, 10, 20.1, 34.5]

fahreheit = [((9/5) * temp +32) for temp in celsius]

print(fahreheit)
#[32.0, 50.0, 68.18, 94.1]

lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)
