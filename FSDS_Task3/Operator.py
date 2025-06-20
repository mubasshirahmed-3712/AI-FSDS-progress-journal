# Author: Mubasshir Ahmed
# Topic: Arithmetic Operations and Boolean Comparisons

# Basic Arithmetic Operations with Integers
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2)  # Division always returns a float
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Floor Division (no remainder): ', 7 // 2)
print('Modulus (remainder): ', 3 % 2)
print('Floor Division: ', 7 // 3)
print('Exponential: ', 3 ** 2)  # 3 raised to the power of 2

# Floating point numbers
print('PI Approximation: ', 3.14)
print('Gravity: ', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

# Assigning variables and doing arithmetic
a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Results
print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b =', exponential)

# More arithmetic with new variables
num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating weight
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Comparison and Logical Operators
print(3 > 2)     # True
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False
print(3 != 2)    # True

# Comparing string lengths
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True:', True == True)
print('True == False:', True == False)
print('False == False:', False == False)
print('True and True:', True and True)
print('True or False:', True or False)

# Identity and Membership Operators
print('1 is 1:', 1 is 1)                 # True
print('1 is not 2:', 1 is not 2)         # True
print('A in Mubasshir:', 'A' in 'Mubasshir')  # False
print('B in Mubasshir:', 'B' in 'Mubasshir')  # False
print('coding in sentence:', 'coding' in 'coding for all')  # True
print('a in an:', 'a' in 'an')           # True
print('4 == 2 ** 2:', 4 == 2 ** 2)       # True

# Logical combinations
print(3 > 2 and 4 > 3)   # True
print(3 > 2 and 4 < 3)   # False
print(3 < 2 and 4 < 3)   # False
print(3 > 2 or 4 > 3)    # True
print(3 > 2 or 4 < 3)    # True
print(3 < 2 or 4 < 3)    # False

# Using NOT operator
print(not 3 > 2)         # False
print(not True)          # False
print(not False)         # True
print(not not True)      # True
print(not not False)     # False
