# encapsulation: wrapping of data inside of a class, so that it can't be accessed individually.
"""
public: by default all variables are public
protected: it is just a name thing, there are some specific access modifiers in python."_"
private:in private we use this convention "__"
"""

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance    # balance is the protected type

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        self.__balance-=amount
        print(amount)

    def checkbalance(self):
        print(f'nuv thagalapettaka migilindhi idhi {self.__balance}')


customer1=Account('Sudhaa',5000)

customer1.deposit(9000)

customer1.withdraw(2000)

customer1.checkbalance()
print(customer1.name)
# print(customer1.__balance) this gives error because balance is a private variable and it can't be accessed  

class cafe:
    freedish='brownie'
    def __init__(self,book,food,drinks):
        self.book = book
        self.food = food
        self._drinks = drinks
    
    def booktype(self):
        print(f'lets get the genre of the book {self.book} heres your freedish {self.freedish}')

    def foodcusine(self):
        print(f'lets get the genre of the book {self.food}')

    def drinkies(self):
        print(f'lets get the genre of the book {self._drinks}')

carla = cafe('death note','mushroom 65 ',' blueberry mojito')
carla.booktype()
carla.drinkies()
print(carla.drinkies())