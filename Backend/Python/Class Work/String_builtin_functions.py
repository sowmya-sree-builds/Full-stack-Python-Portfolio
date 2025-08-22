'''The built in functions for strings are of various type:
    they are: .lower(), .upper(), .islower(), .isupper(), .captialize(), .title()'''

# s = "hey sowmya its 18th today"

# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())


# Trimming and replace built-in functions 
# a = "    hiii    "
# a = a.strip()
# b = a.lstrip()
# c = a.rstrip()

# print(a,b,c,)

# str = "I Today I'm listening to java class"
# str = str.replace("java", "python")
# ytr = str.replace("a","b")
# print(ytr)


# Searching builtin functions
# if we give a different value thats not in the string find returns -1 and index returns error

# f = "Sravaaaaaaaaaan" 
# print(f.find("o"))
# print(f.find("x"))
# print(f.rfind("a"))
# print(f.count("a"))
# print(f.index("a"))

# List methods
# list1 = [1,2,2.5,3,4,5,6,7]

# list1.pop(0)
# print(list1)

# list1.remove(7)
# print(list1)

# list1.append(8)
# print(list1)

# list1.insert(2,2.5)
# print(list1)

# list1.extend([8,9,10])
# print(list1)

# list1.clear()
# print(list1)

# # Tuple methods
# tuple1 = (1,2,3,4,5,6,7,8,8,5,4,6,7,5,3,7,4)
# print(tuple1.count(5))

# print(tuple1.index(5))

# Set methods

# set1 = {1,2,3,4,5}

# set1.add(6)
# print(set1)

# set1.remove(6)
# print(set1)

# set1.discard(7)
# print(set1)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2))
print(set1.intersection(set2))

dict1={'a':1,'b':2,'c':3}

# keys()
print(dict1.keys())
print(dict1.values())
print(dict1.items())


