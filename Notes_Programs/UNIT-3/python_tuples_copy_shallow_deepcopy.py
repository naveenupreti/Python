
"""
===========================================================
 PYTHON TUPLES: ALIASING, SHALLOW COPY AND DEEP COPY
===========================================================

OBJECTIVE:
To understand how assignment and copying work with tuples.

IMPORTANT:
1. Tuples are immutable.
2. A tuple cannot have its elements reassigned.
3. A tuple can contain mutable objects, such as lists.
4. A nested list can be modified even though the tuple
   containing that list is immutable.
5. copy.copy() creates a shallow copy.
6. copy.deepcopy() recursively copies nested objects.

TRICK:
For a tuple containing only immutable elements, Python's
copy operations may return the original tuple itself.
This is safe because its contents cannot be modified.
"""

import copy


# =========================================================
# 1. ALIASING: b = a
# =========================================================

print("\n1. TUPLE ALIASING")
print("-" * 50)

# Create a tuple containing a string and a mutable list.
a = ("Rahul", [80, 90])

# Assignment does not explicitly create a new tuple.
# Both variables refer to the same tuple object.
b = a

# Modify the list contained inside the tuple through b.
# This is allowed because the list itself is mutable.
b[1].append(95)

print("Original a:", a)
print("Alias b   :", b)
print("Same object?", a is b)

# OUTPUT:
# Original a: ('Rahul', [80, 90, 95])
# Alias b   : ('Rahul', [80, 90, 95])
# Same object? True

# EXPLANATION:
# a and b refer to the same tuple.
# The tuple itself has not changed its elements:
# its second element still refers to the same list.
# The list has changed, so both variables show the change.


# =========================================================
# 2. SHALLOW COPY: copy.copy(a)
# =========================================================

print("\n2. TUPLE SHALLOW COPY")
print("-" * 50)

# Create a fresh tuple with a nested mutable list.
a = ("Rahul", [80, 90])

# Request a shallow copy of the tuple.
b = copy.copy(a)

print("Original a:", a)
print("Copied b  :", b)
print("Same tuple object?", a is b)
print("Same nested list?", a[1] is b[1])

# OUTPUT:
# Original a: ('Rahul', [80, 90])
# Copied b  : ('Rahul', [80, 90])
# Same tuple object? True
# Same nested list? True

# IMPORTANT TRICK:
# Unlike a dictionary's copy() method, copy.copy() applied
# to a tuple may return the original tuple itself.
# Tuples are immutable, so creating another outer tuple
# is unnecessary in this case.

# Modify the nested list through b.
b[1].append(95)

print("\nAfter modifying the nested list:")
print("Original a:", a)
print("Copied b  :", b)

# OUTPUT:
# After modifying the nested list:
# Original a: ('Rahul', [80, 90, 95])
# Copied b  : ('Rahul', [80, 90, 95])

# EXPLANATION:
# Both variables refer to the same tuple and therefore
# to the same nested list.
# Modifying the list is visible through both variables.


# =========================================================
# 3. DEEP COPY: copy.deepcopy(a)
# =========================================================

print("\n3. TUPLE DEEP COPY")
print("-" * 50)

# Create a fresh tuple with a nested list and dictionary.
a = (
    "Rahul",
    [80, 90],
    {"city": "Lucknow"}
)

# Create a deep copy.
# Nested mutable objects are recursively copied.
b = copy.deepcopy(a)

print("Original a:", a)
print("Deep copy b:", b)
print("Same tuple object?", a is b)
print("Same nested list?", a[1] is b[1])
print("Same nested dictionary?", a[2] is b[2])

# OUTPUT:
# Original a: ('Rahul', [80, 90], {'city': 'Lucknow'})
# Deep copy b: ('Rahul', [80, 90], {'city': 'Lucknow'})
# Same tuple object? False
# Same nested list? False
# Same nested dictionary? False

# Modify the list in the copied tuple.
b[1].append(95)

# Modify the dictionary in the copied tuple.
b[2]["city"] = "Delhi"

print("\nAfter modifying nested objects in b:")
print("Original a:", a)
print("Deep copy b:", b)

# OUTPUT:
# Original a: ('Rahul', [80, 90], {'city': 'Lucknow'})
# Deep copy b: ('Rahul', [80, 90, 95], {'city': 'Delhi'})

# EXPLANATION:
# The original tuple retains its original nested list
# and dictionary.
# The copied tuple contains independent nested objects,
# so changes made through b do not affect a.


# =========================================================
# 4. COPYING A TUPLE OF IMMUTABLE ELEMENTS
# =========================================================

print("\n4. TUPLE CONTAINING ONLY IMMUTABLE ELEMENTS")
print("-" * 50)

a = (10, 20, 30)

b = copy.copy(a)
c = copy.deepcopy(a)

print("Original a:", a)
print("Shallow copy b:", b)
print("Deep copy c:", c)

print("a is b:", a is b)
print("a is c:", a is c)

# OUTPUT IN TYPICAL PYTHON IMPLEMENTATIONS:
# Original a: (10, 20, 30)
# Shallow copy b: (10, 20, 30)
# Deep copy c: (10, 20, 30)
# a is b: True
# a is c: True

# EXPLANATION:
# All tuple elements are immutable integers.
# Python can safely return the same tuple object.
# Do not rely on object identity as a general copying rule;
# the important point is that the tuple's contents are equal.


# =========================================================
# 5. WHY CAN'T WE CHANGE A TUPLE ELEMENT?
# =========================================================

print("\n5. TUPLE IMMUTABILITY")
print("-" * 50)

a = ("Rahul", [80, 90])

# The following statement is INVALID:
# a[0] = "Amit"
#
# OUTPUT IF UNCOMMENTED:
# TypeError: 'tuple' object does not support item assignment

# But modifying the list inside the tuple is valid:
a[1].append(100)

print(a)

# OUTPUT:
# ('Rahul', [80, 90, 100])

# EXPLANATION:
# We did not replace a tuple element.
# We modified the mutable list referenced by that element.
# Tuple immutability does not make nested lists immutable.


# =========================================================
# 6. FINAL COMPARISON
# =========================================================

print("\n6. FINAL COMPARISON")
print("-" * 50)

print("Aliasing:")
print("  b = a")
print("  Both variables refer to the same tuple.")

print("\nShallow copy:")
print("  b = copy.copy(a)")
print("  Nested mutable objects may remain shared.")
print("  For tuples, the original tuple may be returned.")

print("\nDeep copy:")
print("  b = copy.deepcopy(a)")
print("  Nested objects are recursively copied when needed.")

"""
QUICK REVISION:

1. Tuples are immutable.
2. Assignment b = a creates another reference, not a copy.
3. copy.copy() performs a shallow copy; for tuples, it may
   return the same object.
4. copy.deepcopy() recursively copies nested objects.
5. A tuple containing a list can show changes to that list.
6. A tuple containing only immutable elements does not need
   independent copies of its contents.

IMPORTANT:
Deep copy can behave differently for special objects that
define custom copying behaviour.
"""
