lst = [1,2,3]

print(lst.count(2))
#1

#Objects
#In python, everything is an object. Remember from provious lectures we can use type() to check the type of object something is:
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


class Dog:
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print(sam.breed)
#Lab
print(frank.breed)
#Huskie

class Dog:

    #Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog('Lab', 'Sam')

print(sam.name)
#Sam
print(sam.breed)
#Lab
print(sam.species)
#mammal

class Circle:
    pi = 3.14

    #Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    #Method for resetting radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    #Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()

print('Radius is: ', c.radius)
#Radius is: 1
print('Area is: ', c.area)
#Area is: 3.14p
print('Circumference is: ', c.getCircumference())
#Circumference is: 6.28

c.setRadius(2)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())
# Radius is:  2
# Area is:  12.56
# Circumference is:  12.56

#Inheritance
class Animal:
    def __init__(self):
        print("Animal created")

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
#Animal created
#Dog created
a = Animal()
#Animal created

d.whoAmI()
#Dog
a.whoAmI()
#Animal
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
        return self.name + ' says Woof!'

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
# Niko says Woof!
# Felix says Meow!

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

class Animal:
    def __init__(self, name):  #Constructor of the class
        self.name = name

    def speak(self):           #Abstract method, defined by convention only
        raise NotImpltementedError("Subclass must implement abstract method")

class Dog(Animal):

    def speak(self):
        return self.name+' says Woof!'

class Cat(Animal):

    def speak(self):
        return self.name+ ' says Meow!'

fido = Dog('Fido')
isis = Cat('Isis')
animal = Animal('Animal')

print(fido.speak())
print(isis.speak())
# Fido says Woof!
# Isis says Meow!

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def  __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destoryed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Mehtods
print(book)
print(len(book))
del book
# A book is created
# Title: Python Rocks!, author: Jose Portilla, pages: 159
# 159
# A book is destoryed
