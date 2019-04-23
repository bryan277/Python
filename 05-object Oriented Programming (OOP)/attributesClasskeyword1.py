mylist = [1,2,3]
myset = set()

print(type(myset))

print(type(mylist))

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))
#<class '__main__.Sample'>

class Dog():

    def __init__(self, breed, name, spots):

        # Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed='lab', name='Sammy' , spots=False)
print(my_dog)
#<__main__.Dog
print(my_dog.breed)
#Huskie
print(my_dog.name)
#Sammy
print(my_dog.spots)
#False
