# fruits = ['apples','oranges','banana','grapes','guava']
# for i in range(len(fruits)):
#     print(i,' ',fruits[i])

# fruits = ['apples','oranges','banana','grapes','guava']
# count = 0
# for i in fruits:
#     print(count,' ',i)
#     count +=1

# enumerated() function: it is used to provide index values to a sequence of data
# syntax = enumerate(sequence,start = 0)

# fruits = ['apples','oranges','banana','grapes','guava']
# for index,fruit in enumerate(fruits):
#     print(index,' ',fruit)

# for index,fruit in enumerate(fruits,start = 100):
#     print(index,' ',fruit) 

# dict1 = {'one':1,'two':2,'three':3}
# for index,(key,value) in enumerate(dict1.items(),start=1):
#     print(f'{index} {key} is {value}')

# set1 = {1,23,3,35,2,1,'uno',4,7,6,5,8,4,'uno'}
# for index,se in enumerate(set1,start = 1):
#     print(index,' ',se) 

# zip() - used to access 2x or more sequences at once can take list or tuple or set
stu = ['sow','kav','jinishi','mao']
scores = (85,78,65)
roll = [2,3,4,5]

# for i in range(len(stu)):
#     print(stu[i],scores[i])

# for name, marks,rolls in zip(stu,scores,roll):
#     print(f'{name} scored {marks} with roll numbers {rolls}')

combo = zip(stu,scores,roll)
for i in combo:
    print(i)

















