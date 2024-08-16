x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

############################################################
print("---------------------------------")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

############################################################
print("----------Type Conversion-----------------------")
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
############################################################
print("----------Random Number-----------------------")
"""
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

"""
import random

print(random.randrange(1, 10))