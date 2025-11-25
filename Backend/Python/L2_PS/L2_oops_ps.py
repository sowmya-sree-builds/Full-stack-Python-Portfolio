# class emp:
#     sal = 30000
#     def __init__(self,name):
#         self.name = name
#     def salary(self):
#         return emp.sal
# class FullTimeEmp(emp):
#     def salary(self):
#         hike = emp.sal * 20//100
#         return emp.sal + hike 
# class partTimeEmp(emp):
#     def salary(self):
#         return emp.sal//2 
# class coolie(emp):
#     def salary(self):
#         return emp.sal//4
# e1 = FullTimeEmp("Sowmya")
# e2 = partTimeEmp("Kavya")
# e3 = coolie("rakhi")

# print(e1.name, e1.salary())
# print(e2.name, e2.salary())
# print(e3.name, e3.salary()) 


# class Book:
#     def __init__(self,title,name):
#         self.title = title
#         self.available = True
#         self.name=name
#     def issueBook(self):
#         print('this book is been issued for',self.name)
#         if self.available:
#             self.available = False
#             print('Book issued')
#             return True
#         return False
#     def returnBook(self):
#         self.available = True
#         print('book Returned')

# ends = Book('it ends with us','rocky,')
# print(ends.title, ends.issueBook()) 
# ends.returnBook()       
# print(ends.title,ends.issueBook()) 


# # simulate a bank sector with methods for withdraw, checkbalance, deposit, interest, (name, balance), account type - current account , savings account , rate, generate account number with random digits.
# class bank:
#     def __init__(self, balance, rate):
#         self.balance = balance
#         self.rate = rate
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#     def check_balance(self):
#         return self.balance
#     def interest(self):
#         self.balance += self.balance+ (self.rate//100)
    


# # WAP with oops such that pass distance in kilometers and write two methods one to convert distance to meters and another method to convert into centimeters

# class distance_converter:
#     def __init__(self,km):
#         self.km = km 
#     def to_meters(self):
#         return self.km*1000
#     def to_centimeters(self):
#         return self.km*100000
    
# road = distance_converter(8)
# print(road.to_meters())
# print(road.to_centimeters())


# # WAP that takes details off an employee(name,email,basic): write a method to calculate the net pay
# # netpay  =  basicpay + incentives--> 15% of basic pay  -->pf = 3% of basic pay

# class emp_pay:
#     def __init__(self,name,email,basic_pay):
#         self.name = name
#         self.email = email
#         self.basic_pay = basic_pay
    
#     def total_pay(self):
#         incentives = self.basic_pay * 0.15
#         pf = self.basic_pay * 0.03
#         net_pay = self.basic_pay + incentives - pf
#         return net_pay
    

# hamsa = emp_pay('sri','sri247@gmail.com',25000)
# print(hamsa.total_pay())

# # WAP to store the name & price of an product and write a method to change the price or the product only if new_price is > 0.

# class shopping:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def modify(self,p):
#         if p > 0:
#             self.price = p
#             print(self.price)

# deterg = shopping('surf excel',134)
# print(deterg.modify(40000))
    

# # WAP with two methods one to check password and another to update password
# class user:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#     def to_check(self,passw):
#         if self.__password == passw:
#             print('password correct')
#     def to_update(self,new):
#         self.__password = new
#         return self.__password

# ram = user('ram_varma','manohari')
# ram.to_check('manohari')
# print(ram.to_update('dhivara'))

        
