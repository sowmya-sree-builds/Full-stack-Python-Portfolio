#Iterators: 
# 
# iterable and iterate:
# iterable: it is a collection or sequence of data which can be converted into a iterator.
# eg: string,list,tuple,set,dictionary,range and file object.

# iterate:
# accessing/viewing all the values in a sequence one by one.

# iterator:
# it is a collection of data where we access each value one at a time.

# syntax:
# iterName = iter(iterable)
# next(iterName)

# iter(): it converts an iterable into an iterator.
# next(): used to access each value in an iterator.


# list1 = [1,2,3,4,5]

# for i in list1:
#     print(i)
# print( )


# it1 = iter(list1)
# try:
#     print(next(it1))   #1
#     print(next(it1))   #2
#     print(next(it1))   #3
#     print(next(it1))   #4
#     print(next(it1))   #5
#     print(next(it1))   #1

# except StopIteration:
#     print('Max value reached')


# str1 = 'Lemon Soda'

# for i in str1:
#     print(i)
# print('--------------------------' )


# it1 = iter(str1)
# try:
#     print(next(it1))   #L
#     print(next(it1))   #e
#     print(next(it1))   #m
#     print(next(it1))   #o
#     print(next(it1))   #n
#     print(next(it1))   #
#     print(next(it1))   #s
#     print(next(it1))   #o
#     print(next(it1))   #d
#     print(next(it1))   #a

# except StopIteration:
#     print('Max value reached')

# dict1 = {1:'one',2:'two',3:'three'}

# for i,v in dict1.items():
#     print(i,v)
# print('--------------------------' )


# it1 = iter(dict1.items())
# try:
#     print(next(it1))   
#     print(next(it1))   
#     print(next(it1))   
#     print(next(it1))   
#     print(next(it1))   
#     print(next(it1))   
   

# except StopIteration:
#     print('Max value reached')

# raniter = iter(range(1,5))
# print(next(raniter))




# Iterating over a file
filename=open('D:\\10k Coders\\Backend\\Python\\Class Work\\Day_29_file.txt',encoding = 'UTF-8')
print(next(filename))
# By default every file object is an iterator.
# why:  it contains both  __iter__() and __next__() methods in it right away from creation.
# conclusion: anything that contains __iter__() and __next__() methods in it is an iterator.

# encoding: it is like a rule book to my program which tells which pattern of binary values form which character.
# UTF - 8 (unicode Tranformation Format) it is universal language format which recognizes all the characters of all elanguages in the world.