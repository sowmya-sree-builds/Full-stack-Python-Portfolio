# 1. Walk Like a Duck
class Duck:
    def walk(self):
        print("Duck is walking")

class Person:
    def walk(self):
        print("Person is walking")

def make_it_walk(obj):
    obj.walk()  # Duck typing: doesn't care about type, just method

d = Duck()
p = Person()
make_it_walk(d)
make_it_walk(p)

# 2. Media Player Example
class MP3:
    def play(self):
        print("Playing MP3 music")

class Video:
    def play(self):
        print("Playing video")

def start_media(obj):
    obj.play()

m = MP3()
v = Video()
start_media(m)
start_media(v)

# 3. Payment System
class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

def process_payment(obj, amount):
    obj.pay(amount)

cc = CreditCard()
upi = UPI()
process_payment(cc, 500)
process_payment(upi, 300)

from abc import ABC, abstractmethod
import math

# 4. Shape Area (Abstract)
class Shape(ABC):
    @abstractmethod
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

# 5. Vehicle Start (Abstract)
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

# 6. Bank Account (Abstract)
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Cannot withdraw, minimum balance of 500 required")

class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

savings = SavingsAccount(2000)
current = CurrentAccount(1500)
savings.withdraw(1000)
current.withdraw(1200)

# 7. Report Generation (Abstract)
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

for r in [PDFReport(), ExcelReport()]:
    r.generate()

# 8. Employee Work (Abstract)
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing software")

for e in [Developer(), Tester()]:
    e.work()

# 9. Appliance Power (Abstract)
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan is ON")

class Light(Appliance):
    def turn_on(self):
        print("Light is ON")

for a in [Fan(), Light()]:
    a.turn_on()
