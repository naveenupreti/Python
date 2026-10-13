
"""
===========================================================
 PYTHON DICTIONARY: ALIASING, SHALLOW COPY AND DEEP COPY
===========================================================

OBJECTIVE:
To understand how copying a dictionary works and how
changes to one dictionary affect another.

THREE CONCEPTS:
1. Aliasing       : b = a
2. Shallow Copy   : b = a.copy()
3. Deep Copy      : b = copy.deepcopy(a)

IMPORTANT:
A dictionary is mutable. It can be modified after creation.
A dictionary may also contain mutable objects such as lists
and other dictionaries.
"""

import copy  # Provides the deepcopy() function.


# =========================================================
# 1. ALIASING: b = a
# =========================================================

print("\n1. ALIASING")
print("-" * 50)

# Create the original dictionary.
a = {
    "name": "Rahul",
    "marks": [80, 90],
    "address": {"city": "Lucknow"}
}

# Aliasing: b does NOT receive a new dictionary.
# Both a and b refer to the SAME dictionary object.
b = a

# Change a top-level value through b.
b["name"] = "Amit"

# Modify the nested list through b.
b["marks"].append(95)

# Modify the nested dictionary through b.
b["address"]["city"] = "Delhi"

print("Original a:", a)
print("Alias b   :", b)
print("Same object?", a is b)

# OUTPUT:
# Original a: {'name': 'Amit', 'marks': [80, 90, 95],
#              'address': {'city': 'Delhi'}}
# Alias b   : {'name': 'Amit', 'marks': [80, 90, 95],
#              'address': {'city': 'Delhi'}}
# Same object? True

# EXPLANATION:
# b = a does not create a copy.
# Both names refer to the same outer dictionary.
# Therefore, every change made through b is visible through a.


# =========================================================
# 2. SHALLOW COPY: b = a.copy()
# =========================================================

print("\n2. SHALLOW COPY")
print("-" * 50)

# Create a fresh original dictionary for this experiment.
a = {
    "name": "Rahul",
    "marks": [80, 90],
    "address": {"city": "Lucknow"}
}

# Create a SHALLOW COPY.
# A new outer dictionary is created.
# However, nested lists and dictionaries are still shared.
b = a.copy()

# Change a top-level value in b.
# This does not change a["name"] because the outer
# dictionaries are different.
b["name"] = "Amit"

print("After changing the name:")
print("Original a:", a)
print("Copied b  :", b)

# OUTPUT:
# After changing the name:
# Original a: {'name': 'Rahul', 'marks': [80, 90],
#              'address': {'city': 'Lucknow'}}
# Copied b  : {'name': 'Amit', 'marks': [80, 90],
#              'address': {'city': 'Lucknow'}}

# Now modify the nested list through b.
b["marks"].append(95)

# Modify the nested dictionary through b.
b["address"]["city"] = "Delhi"

print("\nAfter modifying nested objects:")
print("Original a:", a)
print("Copied b  :", b)
print("Same outer dictionary?", a is b)
print("Same marks list?", a["marks"] is b["marks"])
print("Same address dictionary?",
      a["address"] is b["address"])

# OUTPUT:
# After modifying nested objects:
# Original a: {'name': 'Rahul', 'marks': [80, 90, 95],
#              'address': {'city': 'Delhi'}}
# Copied b  : {'name': 'Amit', 'marks': [80, 90, 95],
#              'address': {'city': 'Delhi'}}
# Same outer dictionary? False
# Same marks list? True
# Same address dictionary? True

# EXPLANATION:
# a and b are different outer dictionaries.
# Therefore, changing b["name"] does not change a["name"].
#
# However, both dictionaries refer to the same nested list
# and the same nested address dictionary.
# Therefore, changes to these nested objects affect both.
#
# This is called a SHALLOW COPY.


# =========================================================
# 3. DEEP COPY: b = copy.deepcopy(a)
# =========================================================

print("\n3. DEEP COPY")
print("-" * 50)

# Create a fresh original dictionary.
a = {
    "name": "Rahul",
    "marks": [80, 90],
    "address": {"city": "Lucknow"}
}

# Create a DEEP COPY.
# The outer dictionary and nested mutable objects are
# recursively copied.
b = copy.deepcopy(a)

# Change a top-level value in b.
b["name"] = "Amit"

# Modify the nested list in b.
b["marks"].append(95)

# Modify the nested dictionary in b.
b["address"]["city"] = "Delhi"

print("Original a:", a)
print("Deep copy b:", b)

print("Same outer dictionary?", a is b)
print("Same marks list?", a["marks"] is b["marks"])
print("Same address dictionary?",
      a["address"] is b["address"])

# OUTPUT:
# Original a: {'name': 'Rahul', 'marks': [80, 90],
#              'address': {'city': 'Lucknow'}}
# Deep copy b: {'name': 'Amit', 'marks': [80, 90, 95],
#               'address': {'city': 'Delhi'}}
# Same outer dictionary? False
# Same marks list? False
# Same address dictionary? False

# EXPLANATION:
# deepcopy() recursively copies the dictionary and its
# nested objects in this example.
# Therefore, changing b does not change a, including its
# nested list and nested address dictionary.


# =========================================================
# 4. FINAL COMPARISON
# =========================================================

print("\n4. FINAL COMPARISON")
print("-" * 50)

print("Aliasing:")
print("  b = a")
print("  Both names refer to the same dictionary.")

print("\nShallow copy:")
print("  b = a.copy()")
print("  New outer dictionary; nested mutable objects shared.")

print("\nDeep copy:")
print("  b = copy.deepcopy(a)")
print("  Nested objects are recursively copied.")

"""
QUICK REVISION:

ALIASING
    b = a
    Same dictionary object.

SHALLOW COPY
    b = a.copy()
    New outer dictionary, but nested mutable objects
    can still be shared.

DEEP COPY
    b = copy.deepcopy(a)
    Recursively copies nested objects, so modifications
    to copied nested lists/dictionaries do not affect
    the original in this example.

NOTE:
Deep copying can behave differently for special objects
that implement custom copying behaviour.
"""
