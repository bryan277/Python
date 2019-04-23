#base class
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print('I am a dog!')

    def eat(self):
        print("I am a dog and I'm eating")

    def bark(self):
        print("Woof woof!")




myanimal = Animal()
print(myanimal)
#ANIMAL CREATED
myanimal.eat()
#I am eating
myanimal.who_am_i()
#I am an animal

mydog = Dog()
print(mydog)
#ANIMAL CREATED
#Dog Created

mydog.eat()
#I am eating
mydog.who_am_i()
#I am dog

mydog.bark()
#Woof woof!

#Polymorphism
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
#niko says woof!
print(felix.speak())
#felix says meow!

for pet in [niko, felix]:

    print(type(pet))
    print(pet.speak())

#<class '__main__.Dog'>
#niko says woof!
#<class '__main__.Cat'>
#felix says meow!

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
#niko says woof!
pet_speak(felix)
#felix says meow!

class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImpltementedError("Subclass must implement this abstract method")


myanimal = Animal('fred')

myanimal.speak()
