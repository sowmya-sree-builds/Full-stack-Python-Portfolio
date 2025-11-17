# write a program to calculate and print areas of different shapes using polymorphism and inheritance.
# Such that if any shape does not have a area method then that must be handled using inheritance and polymorphism

class Shape:
    def area(self):
        print( "code to calculate area of this shape is not provided")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        cirArea= 3.14 * self.radius * self.radius
        print(f'Area of circle is {cirArea}')

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        recArea= self.length * self.width
        print(f'Area of Rectangle is {recArea}')

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        triArea= 0.5 * self.base * self.height
        print(f'Area of circle is {triArea}')
class UnknownShape(Shape):
    pass


c2=Circle(5)
c2.area()
c3=Rectangle(5,10)
c3.area()
c4=Triangle(5,11)
c4.area()


# write a program to calculate total,average and grade of a student using OOPs.
# sowmya has scored {total}, his average is {average} and grade is {grade}

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        sum = 0
        for mark in self.marks:
            sum += mark 
        return sum

    def average(self):
        count = 0
        for i in self.marks:
            count+=1
        average= self.total() / count
        return average

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def details(self):
        total= self.total()
        Average =  self.average()
        grade =  self.grade()
        print(f'{self.name} has scored {total}, his average is {Average} and grade is {grade}')

student1 = Student('Sowmya', [34, 56, 76, 45, 32])
student1.details()


# write a program using oops such that salary of an employee. the class should have 3 methods one to set salary, 
# another one to increment the salary based on the percentage in it and another to display the salary. 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = 0     # to assign the value and use it in the function
        self.set_salary(salary)


    def set_salary(self,salary):
        if self.salary<0:
            print('Salary cannot be negative')
        else:
            self.salary = salary
            print(f'salary is {self.salary} ')
        
    def increment(self,value):
        pass

emp1 = Employee('Swathi',30000)
emp1.increment(10)


# write a program to book a room in a hotel using OOPs
# 1. To show the available rooms.
# 2. check in.
# 3. check out.
# 4. price calculation for the stay.


