'''# Class & Object Basics Create a class Car with attributes brand and model. - Write a method
#  car_info() to display details. - Create 3 objects and print their information.
class car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand

    def car_info(self):
        print(f'the model of the car is {self.model} and its from the brand{self.brand}')

details=car('Bmw','G10')
details.car_info()

# Encapsulation (Private Variables) Define a class BankAccount with: - Private attribute __balance.- Methods deposit(amount) and withdraw(amount) to update balance safely. - A method
#  get_balance() to check the balance.  Prevent direct access to __balance from outside.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount(3000)
account.deposit(400)
account.withdraw(500)
print("Final Balance:", account.get_balance())


#  Encapsulation with Getter/Setter Create a class Student: - Private attribute __marks. - Use
#  @property and @marks.setter to implement getter and setter. - Restrict marks between 0 and 100
#  only. - If user tries to assign invalid marks, show 'Invalid marks'.

class Student:
    def __init__(self, marks):
        self.__marks = 0  
        self.marks = marks 
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")

s1 = Student(85)
print("Marks:", s1.marks)  

s1.marks = 95
print("Marks:", s1.marks)  

s1.marks = 150             
print("Marks:", s1.marks)   '''

#  Inheritance & Method Overriding Create a base class Animal with method sound(). - Create
#  derived classes Dog and Cat overriding the method. - When calling sound() on each object, it
#  should print their respective sounds.

class CoffeeShop:
    def order(self):
        print("Welcome! We serve coffee here.")

class Espresso(CoffeeShop):
    def order(self):
        print("You ordered a strong Espresso ")

class Latte(CoffeeShop):
    def order(self):
        print("You ordered a creamy Latte")

class Cappuccino(CoffeeShop):
    def order(self):
        print("You ordered a frothy Cappuccino")

shop = CoffeeShop()
e = Espresso()
l = Latte()
c = Cappuccino()

shop.order()
e.order()
l.order()
c.order()
