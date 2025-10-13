# 1. Bank Account System
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance = {self.balance}")
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest {interest} added. Balance = {self.balance}")

sa = SavingsAccount("12345", 1000, 0.05)
sa.deposit(500)
sa.add_interest()
sa.withdraw(200)

# 2. Library Management 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def download(self):
        print(f"Downloading {self.title} by {self.author} ({self.file_size}MB)")

ebook = EBook("Python Basics", "John Doe", 5)
ebook.download()

# 3. Employee Management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

dev = Developer("Alice", 70000, "Python")
print(f"{dev.name} earns {dev.salary} and codes in {dev.programming_language}")

# 4. Smartphone Features
class Camera:
    def take_photo(self):
        print("Photo taken")

class MusicPlayer:
    def play_music(self):
        print("Playing music")

class Smartphone(Camera, MusicPlayer):
    def browse_internet(self):
        print("Browsing internet")

phone = Smartphone()
phone.take_photo()
phone.play_music()
phone.browse_internet()

# 5. Vehicle Features
class Engine:
    def start_engine(self):
        print("Engine started")

class Wheels:
    def rotate_wheels(self):
        print("Wheels rotating")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.start_engine()
my_car.rotate_wheels()
my_car.drive()

# 6. Hospital Management
class Doctor:
    def treat_patient(self):
        print("Doctor treating patient")

class Researcher:
    def conduct_research(self):
        print("Researcher conducting research")

class DoctorResearcher(Doctor, Researcher):
    def publish_paper(self):
        print("Publishing medical research paper")

dr = DoctorResearcher()
dr.treat_patient()
dr.conduct_research()
dr.publish_paper()

# 7. Educational Hierarchy
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class HeadOfDepartment(Teacher):
    def __init__(self, name, subject, department_name):
        super().__init__(name, subject)
        self.department_name = department_name

hod = HeadOfDepartment("Dr. Smith", "Physics", "Science Department")
print(f"{hod.name}, {hod.subject}, {hod.department_name}")

# 8. Online Shopping System
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class Mobile(Electronics):
    def __init__(self, name, price, brand, ram, storage):
        super().__init__(name, price, brand)
        self.ram = ram
        self.storage = storage

mob = Mobile("Galaxy S25", 80000, "Samsung", "12GB", "256GB")
print(f"{mob.brand} {mob.name} costs {mob.price} with {mob.ram}/{mob.storage}")

# 9. Transport System
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class CarVehicle(Vehicle):  # renamed to avoid clash with Car above
    def __init__(self, speed, fuel_type):
        super().__init__(speed)
        self.fuel_type = fuel_type

class ElectricCar(CarVehicle):
    def __init__(self, speed, fuel_type, battery_capacity):
        super().__init__(speed, fuel_type)
        self.battery_capacity = battery_capacity

ecar = ElectricCar(120, "Electric", "75kWh")
print(f"ElectricCar speed {ecar.speed} km/h, fuel: {ecar.fuel_type}, battery: {ecar.battery_capacity}")