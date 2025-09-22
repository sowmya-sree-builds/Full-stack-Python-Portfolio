class vehicle:
    def fuel(self):
        print('All the vehicles use fuels')

class car(vehicle):
    def petrol(self):
        print('this car uses petrol')

class bike(vehicle):
    def petrol(self):
        print('bike uses petrol')


car1=car()
car1.fuel()
car1.petrol()

print(' ')

bike1=bike()
bike1.fuel()
bike1.petrol()


class food:
    def eating(self):
        print('Everyone must eat')

class restaurant(food):
    def check(self):
        print('Try different cusine')

class home(food):
    def check(Self):
        print('Eat whats there')


raj=restaurant()
raj.check()
raj.eating()

class coders:
    def func1(self):
        print("This function is in school.")

class Student1(coders):
    def func2(self):
        print("This function is in student 1.")

class Student2(coders):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, coders):
    def func4(self):
        print("This function is in student 3.")

obj = Student3()
obj.func1()
obj.func2()
print('   ')



class parent:
    def work(self):
        print('i can work')
class child1(parent):
    def skill(self):
        print('i can dance')
class child2(parent):
    def skill(self):
        print('i can sing')
class grand_child(child1,child2):    #-Method resolution order the first inherited names code will be executed
    def sleep(self):
        print('i can sleep')
g1=grand_child()
g1.skill()
g1.work()
g1.sleep()

c1=child1()
c1.skill()
c1.work()


print('   ')
class sivagami:
    def rule(self):
        print('who kills kalakeyaa will be the kinguuu')

class amarendra_bahubali(sivagami):
    def bet_kalakeya(self):
        print('full kotadu kalakeya2')

class balaladeva(sivagami):
    def kill_kalakeya(self):
        print('killed kalakeyaa')

class king(amarendra_bahubali,balaladeva):
    def rajuu(self):
        print('Balaladeva nuv kadhu pakaki tapukora')

kingu=king()
kingu.rajuu()

class animal:
    def __init__(self,species):
        self.species=species

    def sound(self):
        print('All animals make sound')

class dog(animal):
            def __init__(self,species,breed):
                super().__init__(species)
                self.breed = breed
                print(species,breed)
            
            def sound(self):
                super().sound()
                print('Bark---')
dog1=dog('Mammal','abracadabra')
dog1.sound()