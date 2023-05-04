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
