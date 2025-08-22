# Task:
# Python Random Module - First 5 Problems

# 1. Generate a random float between 0.0 and 1.0. 
# 2. Generate a random integer between 1 and 100. 
# 3. Pick a random fruit from a list ["apple", "banana", "mango", "orange"]. 
# 4. Shuffle a list of numbers [1, 2, 3, 4, 5]. 
# 5. Generate 5 random integers between 10 and 50

import random
# Code 1
print((random.random()))

# Code 2
print((random.randint(1,100)))

# Code 3
list1 = ["apple", "banana", "mango", "orange"]
print((random.choice(list1)))

# code 4
list2 = [1, 2, 3, 4, 5]
shuffled = random.sample(list2, k=len(list2))
print(shuffled)


# Code 5
for i in range(1,6):
    print((random.randint(10,50)),end = ' ')