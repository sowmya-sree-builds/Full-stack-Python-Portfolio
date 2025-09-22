# 1. Animals Speak
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()

# 2. Calculator Operations
class Calculator:
    def calculate(self, a, b):
        pass

class Add(Calculator):
    def calculate(self, a, b):
        return a + b

class Subtract(Calculator):
    def calculate(self, a, b):
        return a - b

add = Add()
sub = Subtract()
print("Addition:", add.calculate(5, 3))
print("Subtraction:", sub.calculate(5, 3))

# 3. Transport Ride Fare
class Transport:
    def fare(self, distance):
        pass

class Bus(Transport):
    def fare(self, distance):
        return distance * 10

class Train(Transport):
    def fare(self, distance):
        return distance * 5

bus = Bus()
train = Train()
for t in [bus, train]:
    print(f"{t.__class__.__name__} fare:", t.fare(10))

# 4. Shape Area
import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

shapes = [Square(4), Circle(3)]
for s in shapes:
    print(f"{s.__class__.__name__} area:", s.area())

# 5. Employee Work
class Employee:
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing software")

employees = [Developer(), Tester()]
for e in employees:
    e.work()

from abc import ABC, abstractmethod

# 6. Vehicle Start
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

for v in [Car(), Bike()]:
    v.start()

# 7. Bank Account
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from savings")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from current")

for acc in [SavingsAccount(), CurrentAccount()]:
    acc.withdraw(1000)

# 8. Device Power
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

class TV(Device):
    def power_on(self):
        print("TV is ON")

class Laptop(Device):
    def power_on(self):
        print("Laptop is ON")

for d in [TV(), Laptop()]:
    d.power_on()

# 9. Student Exam
class Exam(ABC):
    @abstractmethod
    def start_exam(self):
        pass

class MathExam(Exam):
    def start_exam(self):
        print("Math exam started")

class EnglishExam(Exam):
    def start_exam(self):
        print("English exam started")

for ex in [MathExam(), EnglishExam()]:
    ex.start_exam()

# 10. Report Generation
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report generated")

for rep in [PDFReport(), ExcelReport()]:
    rep.generate()
