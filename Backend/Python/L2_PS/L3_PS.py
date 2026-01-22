# Rotate the list to the right
list1 = [1,2,3,4,5]
n = len(list1)-1
temp=list1[n]
for i in range(n-1,-1,-1):
    list1[i+1] = list1[i]
list1[0] = temp
print(list1)



# write a program on prefix sum.
# ip = [2,5,7,9]
# op = [2,7,14,23]
arr1 = [2,5,7,9]
res=[]
sum = 0
for i in arr1:
    sum += i
    res += [sum]
print(res)

# find second largest element in an array.

arr = [7,3,1,4,5,2]
fir = sec = 0
for i in arr:
    if i >=fir:
        sec=fir
        fir = i
    elif i<fir and(sec == fir or i>sec):
        sec=i
print(fir,sec)


# write a program to fins the occurrences of character in a string.
# ip : aabbaaccd
# op : a4b2c2d1
# op : a2b2a2c2d1

str1='aabbaaccd'
res=""
count = 1
for i in range(len(str1)):
    if i < len(str1)-1 and str1[i] == str1[i+1]:
        count+=1
    else:
        res += str1[i]+str(count)
        count=1
print(res)



fin = ""
count = 0
z=str1[0]
for i in str1:
    if i==z:
        count+=1
        fin+= i
        p=str(count)
        fin+=p
print(fin)

