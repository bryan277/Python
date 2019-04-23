zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];

if len(zoo_animals) > 3:
    print ("The first animal at the zoo is the " + zoo_animals[0])
    print ("The second animal at the zoo is the " + zoo_animals[1])
    print ("The third animal at the zoo is the " + zoo_animals[2])
    print ("The fourth animal at the zoo is the " + zoo_animals[3])

# The first animal at the zoo is the pangolin
# The second animal at the zoo is the cassowary
# The third animal at the zoo is the sloth
# The fourth animal at the zoo is the tiger

numbers = [5, 6, 7, 8]

print (numbers[0] + numbers[2])
#12

zoo_animals[3] = 'lion'
print(zoo_animals)
# ['pangolin', 'cassowary', 'sloth', 'lion']


letters = ['a', 'b', 'c']
letters.append('d')
print(len(letters))
print(letters)
#4
# ['a', 'b', 'c', 'd']
