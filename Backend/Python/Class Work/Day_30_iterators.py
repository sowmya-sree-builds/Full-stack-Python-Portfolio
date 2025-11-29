# custom made iterator
# creating own iterators:
# file object already has __iter__() and __next__() method in it so it is an iterator.
# hence, any class that contains a __iter__() and __next__() in it is an iterator.

# iterators are used to load chunks of huge data into memory and process them, so that a huge file won't crash or lag the system.


class EvenNumbers:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        return self.num
  
evens = EvenNumbers()
print(next(evens))
print(next(evens))


class Stopwatch:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 0 :
            raise StopIteration
        self.num -= 1
        return self.num
watch = Stopwatch(10)
print(next(watch))
print(next(watch))



list1 = [1,2,3,4,5]
for i in list1:
    print(i)

it1 = iter(list1)
while True:
    try:
        i = next(it1)
        print(i)
    except StopIteration:
        break
    


# filename = open("")
# lines = filename.readlines()
# for line in lines:
#     print(line)

# print(next(filename))
# print(next(filename))


