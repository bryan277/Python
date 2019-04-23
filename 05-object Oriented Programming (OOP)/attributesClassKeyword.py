mylist = [1,2,3]

myset = set()

print(type(myset))



class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS

    species = 'mammal'

    def __init__(self, breed, name):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name



    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print("woof! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog('Huskie', 'Sammy')

print(type(my_dog))
#<class '__main__.Dog'>

print(my_dog.breed)
#Huskie

print(my_dog.name)
#Sammy

print(my_dog.bark)
#<bound method Dog.bark of <__main__.Dog object at 0x11048c1d0>>

print(my_dog.bark(10))
#woof!

print(my_dog.species)

#questions to ask code immersive
#appartment
#job placement
#finicial aid
#break in between terms?
#how many month in each terms


class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius =1 ):

        self.radius = radius
        self.area = radius*radius*Circle.pi

    #METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)

print(my_circle.get_circumference())
#188.4

print(my_circle.pi)
#3.14

print(my_circle.radius)
#30

print(my_circle.area)
#2826.0
