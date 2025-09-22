# Abstraction: Hides the unnecessary details and show only the required features to the user.
# Here we use a built in class and a method to implement abstraction in our program.
# we declare a class as abstract by inheriting ABC class into that class
# we wont define a method in abstract class.we just declare it.
# we define the abstract method in the classes where the abstract class is inherited.
# we cannot create an object for an abstract class.
# by declaring a method as abstract,we ensure that method is defined in all the sub classes below it.

from abc import ABC, abstractmethod  #imported ABC and abstract method from abc module   "ABC - Stands for abstract base class"
# thse are used for 

# class vehicle(ABC):  #abstract class declaration
#     @abstractmethod    #inorder to declare a method as abstract method
#     def mileage(self):  #abstract method declaration    # just giving a name is declaring ,defining is giving the functionalty for the function
#         pass
    
#     def name():
#         print('This is for testing')

# # v=vehicle()
# # v.mileage()      # this gives error

# class Tesla(vehicle):   # defined a class tesla and inherited abstract class vehicle
#     def mileage(self):
#         print('Tesla:300 miles per charge')  #gave body for the mileage


# t1=Tesla()
# t1.mileage()

# class bike(vehicle):
#     def mileage(Self):
#         print('This has 150 miles per hour')

# t2=bike()
# t2.mileage()


# class restaurant(ABC):
#     @abstractmethod
#     def biryani(self):
#         pass

# class huga(restaurant):
#     def biryani(self):
#         print('chicken biryani here')

#     def drink(self):
#         print('its a coke')

# s=huga()
# s.drink()
# s.biryani()


class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    # @abstractmethod
    # def perimeter(self):
    #     pass

    @abstractmethod
    def circumference(self):
        pass

    def info(self):
        print('this one is considered as a shape')

# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         return self.length*self.breadth
    
#     def perimeter(self):
#         return 2*(self.length+self.breadth)
    

# rect=rectangle(10,5)
# rect.info()

# print(rect.area())


class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
    def circumference(self):
        return 2*3.14*self.radius
    
circ=circle(5)
print('the area of circle with radius is:',circ.area())
print('the circumference of circle with radius is:',circ.circumference())
