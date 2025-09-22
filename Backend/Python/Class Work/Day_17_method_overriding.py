# Polymorphism
# Method Over riding
class animal:
    def speak(self):
        print('Animals Make sounds')

class dog(animal):
    def speak(self):
        print('Dogs Bark')

dog1 = dog()
dog1.speak()

# Method Over loading

# Operaor over loading
class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages
    def __sub__(self,other):
        return self.pages-other.pages
    def __mul__(self,other):
        return self.pages * other.pages
    
book1=book(1000)
book2=book(250)
print(book1 + book2)
print(book1 - book2)
print(book1 * book2)
