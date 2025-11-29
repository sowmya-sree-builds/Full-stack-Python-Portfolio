# Linear Search: searching is happening in a straight line.
# list1 = [1,2,3,4,5,6,7,8,9]
# target = 11
# def insearch(seq,target):
#     ind = 0
#     while(ind<len(list1)):
#         if seq[ind] == target:
#             return ind
#         ind += 1
#     return -1
# rev = insearch(list1,target)
# if rev != -1:
#     print('element is found')
# else:
#     print('element not found')



# Binary Search: it breaks the list into 2 halfs
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = (low + high) // 2   # middle index
#         if arr[mid] == target:
#             return mid   # found at index
#         elif arr[mid] < target:
#             low = mid + 1   # search right half
#         else:
#             high = mid - 1  # search left half
    
#     return -1  
# numbers = [i for i in range(1, 101)]
# print(binary_search(numbers, 45))  



# def bin_search(li):
#     ind = 0
#     lin = len(li) - 1
#     target = 7

#     while ind<lin:
#         mid = ind + lin//2
#         if target ==li[mid]:
#             print('value Found')
#         elif target > li[mid]:
#             ind = mid+1
#         else:
#             lin = mid-1
#         return -1
# print(bin_search([1,2,3,4,5,6,7,8,9,10]))


# sort  -  whats the internal technique
# how internally a for loop work
# brute force 2d array matrix single array avg sum whats backend
# Sorting       - bubble, selection, insertion, merge, quick, heap, shell, radix
# # Bubble Sorting
# li = [5,3,7,4,9,1,7,6]
# def bub_sort(li):
#     num = len(li)
#     for i in range(num-1):
#         swap = False
#         for j in range(num-1-i):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#                 swap = True
#         if not swap:
#             break
#     return li

# print(bub_sort(li))
# [4,7,6,3,2]
# [4.6.3.2.7]
# [4,3,2,6,7]
# [3,2,4,6,7]
# [2,3,4,6,7]     #it takes len of list in worst case


# Selection Sort

# [7,10,77,21,11,11]
# [7,10,77,21,11,11]
# [7,10,11,77,21,11]
# [7,10,11,11,77,21]
# [7,10,11,11,21,77]

# li = [10,7,77,21,11,11]
# def sel_sort(li):
#     num = len(li)
#     for i in range(num):
#         min = i
#         for j in range(i+1,num):
#             if li[min]>li[j]:
#                 min = j
#         li[i],li[min]= li[min],li[i]
#     return li
# print(sel_sort(li))



# Insertion Sort
# [5,|4,3,2,1]      [10,17,12,1,4]
# [4,5|,3,2,1]      [10,17,12,1,4]
# [3,4,5|,2,1]      [10,12,17,1,4]
# [2,3,4,5|,1]      [1,10,12,17,4]
# [1,2,3,4,5].      [1,4,10,12,17]
# li=[5,4,3,2,1]


# Insertion sort:     first compares then inserts until then it holds
li = [11,7,4,6,2]
def ins_sort(li):
    num = len(li)
    for i in range(1,num):
        key = li[i]
        j = i - 1
        while j >= 0 and li[j] > key:
            li[j+1] = li[j]
            j -= 1
        
        li[j+1] = key
    return li

print(ins_sort(li))



# Quick Sort
li = [7,4,6,2,5]

#  working
# [42,7,19,73,5,88,34,27,61,12]
# [42,7,19,5,88,34,27,61,12,73]

