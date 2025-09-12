# it is used to generate a sequence in a more simplified way and it makes code smaller, faster and easy to read
# numbers = [1,2,3,4,5]
# squares=[]
# for i in numbers:
#     sq = i*i
#     squares += [sq]
# print(squares) # easy for us

# compr1 = [i*i for i in numbers] #easy for computer
# print(compr1)

# number = (1,2,3)
# compr2 = tuple(i*i for i in number)
# print(compr2)

numbers = [15,30,45,3,5]
# tup1 = tuple(i*i for i in numbers if i%3==0 and i%5==0)
# list1 = [i*i for i in numbers if i%3==0 and i%5==0]
# set1 = {i*i for i in numbers if i%3==0 and i%5==0}
# print(tup1,list1,set1)
dict1 = {i: i**2 for i in numbers if i%3==0 and i%5==0}
print(dict1)

strng = 'Comprehension'
vowels = [ch for ch in strng if ch in'aeiou']
print(vowels)

