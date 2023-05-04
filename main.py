print("Hello, World!")

import random

# generate a random integer between 0 and 9
random_number = random.randint(0, 9)

print(random_number)

# take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# before swapping
print("Before swapping: a =", a, "and b =", b)

# swap the values
temp = a
a = b
b = temp

# after swapping
print("After swapping: a =", a, "and b =", b)
