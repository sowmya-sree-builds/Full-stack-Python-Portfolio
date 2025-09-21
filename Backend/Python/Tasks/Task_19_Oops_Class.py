# Task: Build a class Car with brand name as class variable, and methods like engineStart, engineStop, accelerate, brake, sudden brake, gear.
# For every call of accelerate must increase speed by 25 kmph and when car reaches the speed of 300 kmph it should say max speed reached,
# Every call of gear function must change gear from 1,2,3 upto 5.
# For each call to break must reduce the speed by 25 kmph. When sudden break method is called then the speed must be 0.
class Car:
    brand = ""   # class variable shared by all cars

    def __init__(self, speed, brand_name):
        Car.brand = brand_name   # set class variable
        self.speed = speed
        self.current_gear = 0

    def enginestart(self):
        print(f'{Car.brand} engine has now started. Lets go')

    def enginestop(self):
        print(f'{Car.brand} engine has now stopped.')

    def accelerate(self):
        if self.speed < 300:
            self.speed += 25
            if self.speed > 300:
                self.speed = 300
            print("Speed:", self.speed)
        else:
            print('Max speed reached.')

    def brake(self):
        if self.speed <= 0:
            print("Car is already stopped.")
        else:
            self.speed -= 25
            if self.speed < 0:
                self.speed = 0
            print("Speed after brake:", self.speed)

    def sudden_brake(self):
        self.speed = 0
        print("Speed after sudden brake:", self.speed)

    def gear(self):
        if self.current_gear < 5:
            self.current_gear += 1
        return self.current_gear

car1 = Car(300, 'Hyundai')
car1.enginestart()
car1.accelerate()          
print("Gear:", car1.gear()) 
print("Gear:", car1.gear()) 
print("Gear:", car1.gear()) 
print("Gear:", car1.gear()) 
print("Gear:", car1.gear()) 
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.sudden_brake()
car1.enginestop()
