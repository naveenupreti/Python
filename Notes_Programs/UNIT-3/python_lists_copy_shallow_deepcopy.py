
"""
===========================================================
 PYTHON LISTS: ALIASING, SHALLOW COPY AND DEEP COPY
===========================================================

OBJECTIVE:
Understand how assignment and copying work with lists.

CONCEPTS:
1. Aliasing       : b = a
2. Shallow Copy   : b = a.copy()
3. Deep Copy      : b = copy.deepcopy(a)

IMPORTANT:
Lists are MUTABLE. Their elements can be changed, added,
or removed after the list has been created.

A list can also contain nested mutable objects such as
other lists and dictionaries.
"""

import copy  # Provides copy.copy() and copy.deepcopy().


# =========================================================
# 1. ALIASING: b = a
# =========================================================

print("\n1. ALIASING")
print("-" * 50)

# Create the original list.
a = [10, 20, [30, 40]]

# Aliasing: no new list is created.
# Both a and b refer to the SAME list object.
b = a

# Modify a simple element through b.
b[0] = 100

# Modify the nested list through b.
b[2].append(50)

print("Original a:", a)
print("Alias b   :", b)
print("Same object?", a is b)

# OUTPUT:
# Original a: [100, 20, [30, 40, 50]]
# Alias b   : [100, 20, [30, 40, 50]]
# Same object? True

# EXPLANATION:
# b = a does not create a copy.
# Both variables refer to the same outer list.
# Therefore, changes made through b are visible through a.


# =========================================================
# 2. SHALLOW COPY: b = a.copy()
# =========================================================

print("\n2. SHALLOW COPY")
print("-" * 50)

# Create a fresh original list for this experiment.
a = [10, 20, [30, 40]]

# Create a SHALLOW COPY.
# A new outer list is created, but the nested list is shared.
b = a.copy()

# Change a simple element in the copied list.
b[0] = 100

print("After changing a simple element:")
print("Original a:", a)
print("Copied b  :", b)

# OUTPUT:
# After changing a simple element:
# Original a: [10, 20, [30, 40]]
# Copied b  : [100, 20, [30, 40]]

# EXPLANATION:
# a and b are different outer lists.
# Therefore, replacing b[0] does not change a[0].

# Now modify the nested list through b.
b[2].append(50)

print("\nAfter modifying the nested list:")
print("Original a:", a)
print("Copied b  :", b)
print("Same outer list?", a is b)
print("Same nested list?", a[2] is b[2])

# OUTPUT:
# After modifying the nested list:
# Original a: [10, 20, [30, 40, 50]]
# Copied b  : [100, 20, [30, 40, 50]]
# Same outer list? False
# Same nested list? True

# EXPLANATION:
# The outer lists are different objects.
# However, both refer to the SAME nested list [30, 40, 50].
# Therefore, modifying the nested list through b
# also changes the list seen through a.
#
# This is called a SHALLOW COPY.


# =========================================================
# 3. DEEP COPY: b = copy.deepcopy(a)
# =========================================================

print("\n3. DEEP COPY")
print("-" * 50)

# Create a fresh original list.
a = [10, 20, [30, 40], {"city": "Lucknow"}]

# Create a DEEP COPY.
# Nested lists and dictionaries are recursively copied.
b = copy.deepcopy(a)

# Change a simple element in b.
b[0] = 100

# Modify the nested list in b.
b[2].append(50)

# Modify the nested dictionary in b.
b[3]["city"] = "Delhi"

print("Original a:", a)
print("Deep copy b:", b)

print("Same outer list?", a is b)
print("Same nested list?", a[2] is b[2])
print("Same nested dictionary?", a[3] is b[3])

# OUTPUT:
# Original a: [10, 20, [30, 40], {'city': 'Lucknow'}]
# Deep copy b: [100, 20, [30, 40, 50], {'city': 'Delhi'}]
# Same outer list? False
# Same nested list? False
# Same nested dictionary? False

# EXPLANATION:
# deepcopy() recursively copies the nested objects.
# Therefore, modifying b does not affect a in this example.
# The original nested list and dictionary remain unchanged.


# =========================================================
# 4. OTHER WAYS TO MAKE A SHALLOW COPY
# =========================================================

print("\n4. OTHER SHALLOW COPY METHODS")
print("-" * 50)

a = [10, 20, [30, 40]]

# Method 1: list.copy()
b = a.copy()

# Method 2: slicing
c = a[:]

# Method 3: list()
d = list(a)

print("Original a:", a)
print("Using copy():", b)
print("Using slicing:", c)
print("Using list():", d)

# OUTPUT:
# Original a: [10, 20, [30, 40]]
# Using copy(): [10, 20, [30, 40]]
# Using slicing: [10, 20, [30, 40]]
# Using list(): [10, 20, [30, 40]]

# IMPORTANT:
# All three methods create a new outer list.
# They are SHALLOW copies.
# Nested mutable objects can still be shared.

print("\nAre the outer lists identical?")
print(a is b)
print(a is c)
print(a is d)

# OUTPUT:
# False
# False
# False

print("\nAre their nested lists identical?")
print(a[2] is b[2])
print(a[2] is c[2])
print(a[2] is d[2])

# OUTPUT:
# True
# True
# True


# =========================================================
# 5. COMPARISON USING THE 'is' AND '==' OPERATORS
# =========================================================

print("\n5. 'is' VS '=='")
print("-" * 50)

a = [10, 20, 30]
b = a.copy()

print(a == b)
print(a is b)

# OUTPUT:
# True
# False

# EXPLANATION:
# == checks whether the lists have equal contents.
# is checks whether both variables refer to the same object.
#
# The lists have equal contents, so a == b is True.
# They are different list objects, so a is b is False.


# =========================================================
# 6. FINAL SUMMARY
# =========================================================

print("\n6. FINAL SUMMARY")
print("-" * 50)

print("Aliasing:")
print("  b = a")
print("  Both variables refer to the same list.")

print("\nShallow copy:")
print("  b = a.copy()")
print("  New outer list; nested mutable objects may be shared.")

print("\nDeep copy:")
print("  b = copy.deepcopy(a)")
print("  Nested objects are recursively copied.")

"""
QUICK REVISION:

ALIASING
    b = a
    Same outer list and same nested objects.

SHALLOW COPY
    b = a.copy()
    New outer list, but nested mutable objects can be shared.

DEEP COPY
    b = copy.deepcopy(a)
    Recursively copies nested objects.

OTHER SHALLOW COPY METHODS
    a.copy()
    a[:]
    list(a)

IMPORTANT DIFFERENCE
    ==  compares values.
    is  checks object identity.

NOTE:
Deep copy can behave differently for special objects that
define custom copying behaviour.
"""
