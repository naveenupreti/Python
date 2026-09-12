"""
Program: Tuple Unpacking Examples in Python

This file demonstrates:
1. Basic unpacking
2. Swapping variables
3. Returning multiple values from a function
4. Iterating over list of tuples
5. Ignoring unneeded values
6. Variable-length unpacking

Inline comments explain each example.
Sample outputs are provided at the end of the file.
"""

# ---------------------------------------------------------
# 1. Basic unpacking
# Assign values from a tuple directly into variables
a, b, c = 1, 2, 3
print("1. Basic unpacking:")
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3
print("-"*40)

# ---------------------------------------------------------
# 2. Swapping variables without a temporary variable
# Python allows swapping in a single line using tuple unpacking
x, y = 5, 10
x, y = y, x
print("2. Swapping variables:")
print(f"x={x}, y={y}")  # x=10, y=5
print("-"*40)

# ---------------------------------------------------------
# 3. Returning multiple values from a function
# Functions can return multiple values as a tuple
def min_max(numbers):
    """
    Returns minimum and maximum of a list
    """
    return min(numbers), max(numbers)

low, high = min_max([4, 7, 1, 9])
print("3. Function returning multiple values:")
print(f"low={low}, high={high}")  # low=1, high=9
print("-"*40)

# ---------------------------------------------------------
# 4. Iterating over list of tuples
# Each tuple in the list can be unpacked directly in the loop
points = [(1, 2), (3, 4), (5, 6)]
print("4. Iterating over list of tuples:")
for x, y in points:
    print(f"x={x}, y={y}")
print("-"*40)

# ---------------------------------------------------------
# 5. Ignoring unneeded values
# Use underscore (_) to ignore values that are not needed
data = (10, 20, 30)
a, _, c = data
print("5. Ignoring unneeded values:")
print(f"a={a}, c={c}")  # a=10, c=30
print("-"*40)

# ---------------------------------------------------------
# 6. Variable-length unpacking
# Use * to capture multiple items in the middle
numbers = [1, 2, 3, 4, 5]
a, *middle, z = numbers
print("6. Variable-length unpacking:")
print(f"a={a}")          # a=1
print(f"middle={middle}")# middle=[2, 3, 4]
print(f"z={z}")          # z=5
print("-"*40)

# ============================================================
#                 SAMPLE OUTPUT OF THE PROGRAM
# ============================================================

"""
1. Basic unpacking:
a=1, b=2, c=3
----------------------------------------
2. Swapping variables:
x=10, y=5
----------------------------------------
3. Function returning multiple values:
low=1, high=9
----------------------------------------
4. Iterating over list of tuples:
x=1, y=2
x=3, y=4
x=5, y=6
----------------------------------------
5. Ignoring unneeded values:
a=10, c=30
----------------------------------------
6. Variable-length unpacking:
a=1
middle=[2, 3, 4]
z=5
----------------------------------------
"""
