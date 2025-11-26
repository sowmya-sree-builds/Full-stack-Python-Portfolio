# Linear Search: searching is happening in a straight line.
list1 = [1,2,3,4,5,6,7,8,9]
target = 11
def insearch(seq,target):
    ind = 0
    while(ind<len(list1)):
        if seq[ind] == target:
            return ind
        ind += 1
    return -1
rev = insearch(list1,target)
if rev != -1:
    print('element is found')
else:
    print('element not found')



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



def bin_search(li):
    ind = 0
    lin = len(li) - 1
    target = 7

    while ind<lin:
        mid = ind + lin//2
        if target ==li[mid]:
            print('value Found')
        elif target > li[mid]:
            ind = mid+1
        else:
            lin = mid-1
        return -1
print(bin_search([1,2,3,4,5,6,7,8,9,10]))



# Sorting
# Bubble Sorting
li = [5,3,7,4,9,1,7,6]
def bub_sort(li):
    num = len(li)
    for i in range(num-1):
        swap = False
        for j in range(num-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                swap = True
        if not swap:
            break
    return li

print(bub_sort(li))


