'''
In Python, packing and unpacking are techniques for grouping multiple values into a collection
and then extracting those values back into separate variables.

1. Packing

Packing means putting multiple values into a single variable, usually a tuple.

x = 10
y = 20
z = 30

data = x, y, z       # Packing
print(data)          # (10, 20, 30)

Python automatically creates a tuple containing the three values.

2. Unpacking

Unpacking means extracting values from a collection into separate variables.

data = (10, 20, 30)

x, y, z = data       # Unpacking

print(x)             # 10
print(y)             # 20
print(z)             # 30

'''
# ============================================================
#        PACKING AND UNPACKING IN PYTHON
# ============================================================

# -------------------- PACKING --------------------

# Packing means putting multiple values into one collection.
# Parentheses are optional when creating a tuple.

data = 10, 20, 30

print("Packed tuple:", data, "type(data)=",type(data))
# Output: Packed tuple: (10, 20, 30)

# The same thing can be written explicitly as:
data = (10, 20, 30)

print("Packed tuple:", data)
# Output: Packed tuple: (10, 20, 30)


# -------------------- UNPACKING --------------------

# Unpacking means extracting the values of a collection
# into separate variables.

x, y, z = data

print("x =", x)     # x = 10
print("y =", y)     # y = 20
print("z =", z)     # z = 30


# -------------------- PACKING WITH * --------------------

# * can collect multiple values into a list.
# This is called extended unpacking.

a, *b = (10, 20, 30, 40)

print("a =", a)     # a = 10
print("b =", b)     # b = [20, 30, 40]


# The * variable can be in the middle.

first, *middle, last = (10, 20, 30, 40, 50)

print("first  =", first)      # first  = 10
print("middle =", middle)     # middle = [20, 30, 40]
print("last   =", last)       # last   = 50


# -------------------- UNPACKING A LIST --------------------

numbers = [100, 200, 300]

p, q, r = numbers

print(p, q, r)
# Output: 100 200 300


# -------------------- UNPACKING A STRING --------------------

# A string is iterable, so its characters can be unpacked.

a, b, c = "ABC"

print(a)          # A
print(b)          # B
print(c)          # C


# -------------------- SWAPPING VARIABLES --------------------

# Python uses packing and unpacking to make swapping easy.

x = 10
y = 20

x, y = y, x        # 20 and 10 are packed and then unpacked

print("After swapping:")
print("x =", x)    # x = 20
print("y =", y)    # y = 10


# -------------------- FUNCTION RETURN VALUES --------------------

# A function can return multiple values.
# Internally, they are returned as a tuple (packing).

def calculate(a, b):
    return a + b, a - b, a * b

result = calculate(10, 5)

print("Returned value:", result)
# Output: Returned value: (15, 5, 50)

# We can unpack the returned tuple directly.

addition, subtraction, multiplication = calculate(10, 5)

print("Addition =", addition)           # 15
print("Subtraction =", subtraction)     # 5
print("Multiplication =", multiplication) # 50


# ============================================================
# IMPORTANT:
#
# Packing:
#     x = 10, 20, 30
#     Multiple values -> ONE tuple
#
# Unpacking:
#     x, y, z = (10, 20, 30)
#     ONE collection -> MULTIPLE variables
#
# Extended unpacking:
#     x, *y = (10, 20, 30, 40)
#     x = 10
#     y = [20, 30, 40]
# ============================================================