class Cars:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    def car_types(self):
        print(f'the name of the car is {self.name} which is launched by the brand {self.brand}')

model1 = Cars("Tata SUV", "TVS")
model1.car_types()


class Student:
    def __init__(self,id,name,age=32,place="Hyderabad"):
        self.id = id
        self.name = name
        self.age = age
        self.place = place
    def stu_details(self):
        print(f"Student ID: {self.id}")
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student place: {self.place}")
# sairam = Student()

# Devloper: id, name, role, salary | software skills(), coding(), intro()
# Tester:   id, name, role, salary | software skills(), debug(), intro()

class Gajala_sol:
    def __init__(self,id,name,role,salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary
    
    def software_skills(self):
        print(f"{self.name} has the software skills")

    def intro(self):
        print(f"Hey this is {self.name} my id is {self.id} and my role is {self.role} with a salary {self.salary}")

class developer(Gajala_sol):
    def coding(self):
        print("My skill is to CODE")

class tester(Gajala_sol):
    def debug(self):
        print("My skills is to DEBUG")

b = developer(24,"ram","developer",10000)
b.intro()
b.coding()
b.software_skills()

print("-----------------------")

a = tester(24,"sita","tester",10000)
a.intro()
a.debug()
a.software_skills()

# Types of inheritance:
# single level
# multi level
# hierarchial
# multiple
# hybrid

# single level ek niranjan
class parent:
    def drive(self):
        print("Driving")
    
class child(parent):
    def eating(self):
        print("eating")

d = child()
d.eating()
d.drive()


# multi level  parent - child - child ki child

class grandfather:
    def grand_father(self):
        print("i am a god father")
class Father(grandfather):
    def father(self):
        print("i am father")
class Son(Father):
    def son(self):
        print("i am self")
e = Son()
e.grand_father()
e.father()
e.son()

# hierarchial  single parent multiple childs
class Gajala_sol:
    def __init__(self,id,name,role,salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary
    
    def software_skills(self):
        print(f"{self.name} has the software skills")

    def intro(self):
        print(f"Hey this is {self.name} my id is {self.id} and my role is {self.role} with a salary {self.salary}")

class developer(Gajala_sol):
    def coding(self):
        print("My skill is to CODE")

class tester(Gajala_sol):
    def debug(self):
        print("My skills is to DEBUG")

b = developer(24,"ram","developer",10000)
b.intro()
b.coding()
b.software_skills()

print("-----------------------")

a = tester(24,"sita","tester",10000)
a.intro()
a.debug()
a.software_skills()


# multiple - multiple parents single childs

class Father:
    def eat(self):
        print("eating")                 # 2nd prioriy

class Mother:
    def sleep(self):
        print("sleeping")                 # 3rd prioriy

class son(Father,Mother):          # order goes from left to right 
    def bahubali(self):
        print("watches bahubali")        # 1 st priority
bro = son()
bro.eat()
bro.sleep()
bro.bahubali()
print(son.mro())        # [<class '__main__.son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]

# MRO - method resolution order 
# mro is inbuilt activated when we use multiple inheritances are used.
# every super classes parent is an object    internally writeen as father(object)





# hybrid - 

class A:
    def method_A(self):
        print("class A")

class B(A):
    def method_B(self):
        print("class B")

class C(A):
    def method_C(self):
        print("class C")

class D(B,C):
    def method_D(self):
        print("class D")

d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()


# super, types of methods.


