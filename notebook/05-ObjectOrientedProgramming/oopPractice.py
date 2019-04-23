print(type(1))
print(type([]))
print(type(()))
print(type({}))
# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

class Sample:
    pass

x = Sample()

print(type(x))
#<class '__main__.Sample'>

# class Dog:
#
#     species = 'mammal'
#
#     def __init__(self,breed):
#         self.breed = breed
#
#
# sam = Dog(breed='Lab')
# frank = Dog(breed='Huskie')
#
# print(sam.breed)
# #Lab
# print(frank.breed)
#Huskie

class Dog:

    #Class Object Attribute
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab', 'Sam')
print(sam.name)
#Sam
print(sam.species)
#mammal

class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()

print('Radius is: ', c.radius)
#Radius is: 1
print('Radius is: ', c.setRadius)
#Radius is:  <bound method Circle.setRadius of <__main__.Circle object at 0x10f556240>>
print('Area is: ', c.area)
#Area is: 3.14
print('Circumference is: ', c.getCircumference())
#Circumference is:  6.28

c.setRadius(2)

print('Radius is: ',c.radius)
#Radius is: 2
print('Area is: ',c.area)
#Area is: 12.56
print('Circumference is: ', c.getCircumference())
#Circumference is:  12.56

#Inheritance

class Animal:
    def __init__(self):
        print("Animail created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
a = Animal()
# Animail created
# Dog created
d.whoAmI()
#Dog
d.eat()
#Eating
a.eat()
#Eating
d.bark()
#Woof!


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+ ' says Woof!'

class Cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name+ ' says Meow!'

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
#Niko says Woof!
print(felix.speak())
#Felix says Meow!

for pet in [niko, felix]:
    print(pet.speak())
# Niko says Woof!
# Felix says Meow!

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
# Niko says Woof!
# Felix says Meow!
