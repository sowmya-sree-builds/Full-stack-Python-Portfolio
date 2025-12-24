# second largest in an array
# ip - [1,3,0,4,0,0,5]
# op - [1,3,4,5,0,0,0]

# ip - [1,0,0,0,4]
# op - [1,4,0,0,0]

# list1 = [1,0,0,0,4]
# shift = []
# count = 0
# for i in list1:
#     if i == 0:
#         count+=1
#     else:
#         shift += [i]
# for i in range(count):
#     shift += [0]
# print(shift)

#    T.C = O(n), S.C = O(n)
# list1 = [1,3,0,4,0,0,5]
# res = [0 for i in range(len(list1))]
# c = 0
# for i in range(0,len(list1)):
#     if list1[i] != 0:
#         res[c] = list1[i]
#         c += 1
# print(res)


# Problem of shifting zeroes to end.
# i = 0
# j = 0

# while j<=len(list1)-1:
#     if list1[j] != 0:
#         list1[i],list1[j] = list1[j],list1[i]
#         i+=1
#     j+=1
# print(list1)

# def move_zero(li):
#     i = 0
#     j = 0
#     while j<=len(list1)-1:
#         if list1[j] != 0:
#             list1[i],list1[j] = list1[j],list1[i]
#             i+=1
#         j+=1
#     return li
# print(move_zero([1,2,0,4,0,0,5]))


# unique elements 

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

list1 = [0,1,1,2,3,3,5]
i=0
j=1
while(j<len(list1)):
    if list1[i] != list1[j]:
        list1[i+1] = list1[j]
        i+=1
    j += 1
print(list1)


# list1 = [0,1,1,2,2,3,3,3,4,4,4,5]
list1 = [1,1,2]
i=0
j=1
while(j<len(list1)):
    if list1[i] != list1[j]:
        list1[i+1],list1[j] = list1[j],list1[i+1]
        i+=1
    j += 1
print(list1)


# right rotation 

# arr = [1,2,3,4,5]
arr = [3,7,2,6,4,9,7,1,3,0]
n = len(arr)-1
temp = arr[n]
for i in range(n-1,-1,-1):
    arr[i+1] = arr[i]
arr[0] = temp
print(arr)


def rotate_num(arr,k):
    while k > 0:
        n = len(arr)-1
        temp = arr[n]
        for i in range(n-1,-1,-1):
            arr[i+1] = arr[i]
        arr[0] = temp
        k -= 1
    return arr
print(rotate_num([1,2,3,4,5,6,7],4))



# Two sum
# find index of the array elements whos sum equals target

tar = 5
arr = [1,2,3,4,5,6]
i=0


