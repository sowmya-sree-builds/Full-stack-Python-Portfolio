# generator are used to optimize iter function for short outputs.
# it is a type of iterator function




class counter:
    def number(self,limit):
        i=1
        while i <=limit: 
            yield i      # atleast one yield means its a generator function
            i += 1
# def num():
#     for i in range(1,6):
#         print(i)


c= counter()
x = c.number(2)
print(next(x))
print(next(x))
# print(next(x))

def outer():
    print("hello")
    def inner():
        print("hello world")
    print("hi")
    return inner

x = outer()
x()


def decor(func):
    print("program started")
    print(func())
    print("Program ended")

# @decor
def process():
    return "tasks are completed"

decor(process)





