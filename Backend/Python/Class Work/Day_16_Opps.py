# OOPs(object oriented programming): It is a ohenomemon of creating objects and running the program using those object.
# it is a paradigm
# Class: blueprint for our object creation
# object: simulating a real life thing in our program. / instance of a class
# we create objects outside the class in python
# eg:it can be a car,a chair
# four pillars of oops:
# Encapsulation: Grabbing of data and functions inside a class.
# abstraction: hiding the unecessary details / functionality from the user,so that he can see only the essential things
# Inheritance:acquring data and functions from the parent class to child class
# polymorphism: same function name but different functionality.
# __init__():it is a default constructor which is called automatically when an object is created
            # it is used to assign values to our object(car1).
            # init stands for initialize.
            # self:it is used to know which object is currently accessing the data and functions inside the class.
            # variable is the reference of data, just like that self is a reference to object 
            # it is used to know which object is working on the data/functions inside a class
# Class variables vs object variables:
# syntax:
""" class classname:
    # class variable
    init function:
        # object variables / instance variables"""


"""class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def enginestart(self):
        print(f'{self.brand} {self.model} the car has started')

    def enginestop(self):
        print(f'{self.brand} {self.model} the car has stopped')


car1=car('Audi','A6')
car1.enginestart()
car1.enginestop()
# print(f'the brand of car is {car1.brand}')
# print(f'the model of car is {car1.model}')

car2=car('Lamborghini','avendator')
car2.enginestart()
car2.enginestop()

# print(f'the brand of car is {car1.brand}')
# print(f'the model of car is {car1.model}')


class movie:
    def __init__(self,movie,timeline):
        self.movie = movie
        self.timeline = timeline

    def movieyear(self):
        print(f'{self.movie} is released in the year {self.timeline}')

    def hitmov(self):
        print(f'{self.movie} is a hit')

mov1=movie('bahubali',2017)
mov1.movieyear()
mov1.hitmov()
mov2=movie('ninnukori',2019)
mov2.hitmov()
mov3=movie('anthariksham',2015)

print(f'the movie name is {mov2.movie} time line is {mov3.timeline}')

"""
class cafe:
    freedish='brownie'
    def __init__(self,book,food,drinks):
        self.book = book
        self.food = food
        self.drinks = drinks
    
    def booktype(self):
        print(f'lets get the genre of the book {self.book} heres your freedish {self.freedish}')

    def foodcusine(self):
        print(f'lets get the genre of the book {self.food}')

    def drinkies(self):
        print(f'lets get the genre of the book {self.drinks}')

carla = cafe('death note','mushroom 65 ',' blueberry mojito')
carla.booktype()

class dog:
    species='mammal' #class variables
    area='hyderabad'
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed   #these are object variables

    def details(self):
        print(f'the {self.name} of breed {self.breed} is {self.species} belongs to {self.area}')
    

dog1=dog('bunty','indie')
dog1.details()

dog2=dog('chimtu','Pomerian')
dog2.details()


class atm:

    # constructor
    def _init_(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input('''
                         Hello, how would you like to proceed?
                         1. Enter 1 to create pin
                         2. Enter 2 to deposit
                         3. Enter 3 to Wwithdraw
                         4. Enter 4 to check balance
                         5. Enter 5 to exit''')
        if user_input=='1':
            print('create pin')
        elif user_input=='1':
            print('create pin')
        elif user_input=='2':
            print('create pin')
        elif user_input=='3':
            print('create in')
        elif user_input=='4':
            print('create pin')