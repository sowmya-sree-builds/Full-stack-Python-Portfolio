from abc import ABC, abstractmethod
import math

# 1. Employee Details
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id



class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language

    def show_details(self):
        print(f"Developer: {self.name}, ID: {self.emp_id}, Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def show_details(self):
        print(f"Manager: {self.name}, ID: {self.emp_id}, Team Size: {self.team_size}")

dev = Developer("Alice", 101, "Python")
mgr = Manager("Bob", 102, 10)
dev.show_details()
mgr.show_details()

# 2. Shapes Area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(4, 5)
cir = Circle(3)
print("Rectangle area:", rect.area())
print("Circle area:", cir.area())

# 3. Vehicle Information
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def show(self):
        print(f"Car: {self.brand}, Year: {self.year}, Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def show(self):
        print(f"Bike: {self.brand}, Year: {self.year}, Type: {self.bike_type}")

car = Car("Toyota", 2023, 4)
bike = Bike("Yamaha", 2022, "Sports")
car.show()
bike.show()

# 4. Student Performance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Sports:
    def __init__(self, sport):
        self.sport = sport

class CollegeStudent(Student, Sports):
    def __init__(self, name, age, roll_no, sport):
        Student.__init__(self, name, age, roll_no)
        Sports.__init__(self, sport)

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_no}, Sport: {self.sport}")

cs = CollegeStudent("John", 20, "CSE01", "Cricket")
cs.show()

# 5. Teaching Staff (Hybrid)
class Staff:
    def __init__(self, staff_name):
        self.staff_name = staff_name

class Teacher(Staff):
    def teach(self):
        print(f"{self.staff_name} is teaching")

class Researcher(Staff):
    def research(self):
        print(f"{self.staff_name} is researching")

class Professor(Teacher, Researcher):
    def __init__(self, staff_name):
        Teacher.__init__(self, staff_name)
        Researcher.__init__(self, staff_name)

prof = Professor("Dr. Ray")
prof.teach()
prof.research()

# 6. Gadget Store
class Product:
    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        # No super() because Product is the top-most concrete class

class Electronics(Product):
    def __init__(self, name, price, brand, **kwargs):
        self.brand = brand
        super().__init__(name, price, **kwargs)

class Accessories(Product):
    def __init__(self, name, price, accessory_type, **kwargs):
        self.accessory_type = accessory_type
        super().__init__(name, price, **kwargs)

class Smartphone(Electronics, Accessories):
    def __init__(self, name, price, brand, accessory_type, ram, storage):
        self.ram = ram
        self.storage = storage
        # pass everything forward as kwargs
        super().__init__(name, price, brand=brand, accessory_type=accessory_type)

    def details(self):
        print(f"Name: {self.name}, Price: {self.price}, Brand: {self.brand}, "
              f"Accessory: {self.accessory_type}, RAM: {self.ram}, Storage: {self.storage}")

phone = Smartphone("iPhone", 90000, brand="Apple", accessory_type="Case", ram="8GB", storage="256GB")
phone.details()



# 7. School Fee Calculation
class Fee:
    def calculate(self):
        print("Base fee calculated")

class TuitionFee(Fee):
    def calculate(self):
        super().calculate()
        print("Tuition fee added")

tf = TuitionFee()
tf.calculate()

# 8. Bank Account deposit
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, balance=0, interest=0.05):
        super().__init__(balance)
        self.interest = interest

    def deposit(self, amount):
        super().deposit(amount)
        interest_amt = self.balance * self.interest
        self.balance += interest_amt
        print(f"Interest {interest_amt} added. Balance: {self.balance}")

sacc = SavingsAccount(1000, 0.1)
sacc.deposit(500)

# 9. Multiple Levels super()
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        super().show()
        print("B show")

class C(B):
    def show(self):
        super().show()
        print("C show")

c = C()
c.show()

# 10. Diamond Problem
class A_mro:
    def display(self):
        print("Display from A")

class B_mro(A_mro):
    def display(self):
        print("Display from B")

class C_mro(A_mro):
    def display(self):
        print("Display from C")

class D_mro(B_mro, C_mro):
    pass

d = D_mro()
d.display()  # Which executes?

# 11. Multi-Level + Multiple Inheritance MRO
print(D_mro.mro())  # shows the resolution order for D_mro

# 12. Practical Library Example
class Book:
    def info(self):
        print("Book info")

class EBook(Book):
    def info(self):
        print("EBook info")

class AudioBook(Book):
    def info(self):
        print("AudioBook info")

class DigitalLibrary(EBook, AudioBook):
    pass

dl = DigitalLibrary()
dl.info()  # check which info executes
print(DigitalLibrary.mro())
