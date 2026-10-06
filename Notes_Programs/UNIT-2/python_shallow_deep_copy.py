import copy

# ============================================================
# NORMAL COPY / ASSIGNMENT
# ============================================================

# This is the original list.
# It contains an inner list [30, 40].
# The inner list is mutable, so it helps us understand
# the difference between normal, shallow and deep copy.
original = [10, 20, [30, 40]]

print("Original:", original)
# Output:
# Original: [10, 20, [30, 40]]


# ------------------------------------------------------------
# NORMAL COPY USING =
# ------------------------------------------------------------

# IMPORTANT:
# normal = original does NOT create a new list.
# It only creates another reference to the SAME list object.
normal = original

print("\nNORMAL COPY / ASSIGNMENT")
print("original is normal:", original is normal)
# Output:
# original is normal: True
#
# "is" checks whether two variables refer to the same object.
# True means original and normal refer to exactly the same list.


# Change the list using normal.
normal.append(50)

print("After normal.append(50):")
print("original:", original)
print("normal  :", normal)
# Output:
# original: [10, 20, [30, 40], 50]
# normal  : [10, 20, [30, 40], 50]
#
# Why did original also change?
# Because original and normal are referring to the SAME list.
#
# Diagram:
#
# original ──────┐
#                ↓
#          [10, 20, [30, 40], 50]
#                ↑
# normal ────────┘
#
# Therefore:
# normal.append(50) changes the same object seen by original.


# ------------------------------------------------------------
# NORMAL ASSIGNMENT WITH INNER LIST
# ------------------------------------------------------------

# Reset the original list for the next example.
original = [10, 20, [30, 40]]

normal = original

# normal[2] refers to the inner list [30, 40].
normal[2].append(50)

print("\nAfter changing the INNER list:")
print("original:", original)
print("normal  :", normal)
# Output:
# original: [10, 20, [30, 40, 50]]
# normal  : [10, 20, [30, 40, 50]]
#
# Again, both show the change because both variables
# refer to the same complete list object.


# ============================================================
# SHALLOW COPY
# ============================================================

# Reset the original list.
original = [10, 20, [30, 40]]

# .copy() creates a NEW outer list.
# However, nested objects such as the inner list are NOT copied.
shallow = original.copy()

print("\nSHALLOW COPY")
print("original is shallow:", original is shallow)
# Output:
# original is shallow: False
#
# The outer lists are different objects.

print("original[2] is shallow[2]:",
      original[2] is shallow[2])
# Output:
# original[2] is shallow[2]: True
#
# The inner list is the SAME object in both lists.
#
# Diagram:
#
# original ──→ [10, 20, ──────→ [30, 40]]
#                                    ↑
# shallow ──→ [10, 20, ────────────┘
#
# Outer list  → different
# Inner list  → same


# ------------------------------------------------------------
# SHALLOW COPY: CHANGE OUTER LIST
# ------------------------------------------------------------

# append() changes only the outer list.
shallow.append(50)

print("\nAfter shallow.append(50):")
print("original:", original)
print("shallow :", shallow)
# Output:
# original: [10, 20, [30, 40]]
# shallow : [10, 20, [30, 40], 50]
#
# Why did original NOT change?
# Because original and shallow have DIFFERENT outer lists.
#
# So:
# Changing shallow itself      → original is NOT affected.


# ------------------------------------------------------------
# SHALLOW COPY: CHANGE INNER LIST
# ------------------------------------------------------------

# [2] refers to the inner list [30, 40].
# Since the inner list is shared, this change affects both.
shallow[2].append(60)

print("\nAfter shallow[2].append(60):")
print("original:", original)
print("shallow :", shallow)
# Output:
# original: [10, 20, [30, 40, 60]]
# shallow : [10, 20, [30, 40, 60], 50]
#
# Why did original also change?
# Because original[2] and shallow[2] refer to the SAME inner list.
#
# Therefore:
# Changing OUTER object → independent
# Changing SHARED INNER object → affects both
#
# This is the main concept of SHALLOW COPY.


# ============================================================
# DEEP COPY
# ============================================================

# Reset the original list.
original = [10, 20, [30, 40]]

# deepcopy() creates a completely independent copy.
# It creates a new outer list AND new copies of nested objects.
deep = copy.deepcopy(original)

print("\nDEEP COPY")

print("original is deep:", original is deep)
# Output:
# original is deep: False
#
# The outer lists are different.

print("original[2] is deep[2]:",
      original[2] is deep[2])
# Output:
# original[2] is deep[2]: False
#
# The inner lists are ALSO different objects.
#
# Diagram:
#
# original ──→ [10, 20, ──→ [30, 40]]
#
# deep ──────→ [10, 20, ──→ [30, 40]]
#
# The two [30, 40] lists look the same,
# but they are different objects.


# ------------------------------------------------------------
# DEEP COPY: CHANGE OUTER LIST
# ------------------------------------------------------------

deep.append(50)

print("\nAfter deep.append(50):")
print("original:", original)
print("deep    :", deep)
# Output:
# original: [10, 20, [30, 40]]
# deep    : [10, 20, [30, 40], 50]
#
# Changing the outer list of deep does not affect original.
# The outer lists are independent.


# ------------------------------------------------------------
# DEEP COPY: CHANGE INNER LIST
# ------------------------------------------------------------

deep[2].append(60)

print("\nAfter deep[2].append(60):")
print("original:", original)
print("deep    :", deep)
# Output:
# original: [10, 20, [30, 40]]
# deep    : [10, 20, [30, 40, 60], 50]
#
# original is NOT affected.
#
# Why?
# Because deep[2] and original[2] are different inner lists.
#
# Therefore:
# Changing OUTER object  → original NOT affected
# Changing INNER object  → original NOT affected
#
# This is the main concept of DEEP COPY.


# ============================================================
# COMPARISON OF ALL THREE
# ============================================================

print("\n================ COMPARISON ================")

print("NORMAL ASSIGNMENT : b = a")
# Output:
# NORMAL ASSIGNMENT : b = a
# Same outer object and same nested objects are referenced.

print("SHALLOW COPY      : b = a.copy()")
# Output:
# SHALLOW COPY      : b = a.copy()
# New outer object, but nested objects are shared.

print("DEEP COPY         : b = copy.deepcopy(a)")
# Output:
# DEEP COPY         : b = copy.deepcopy(a)
# New outer object and new copies of nested objects.


# ============================================================
# FINAL SUMMARY
# ============================================================

# NORMAL ASSIGNMENT
#
# b = a
#
# No new list is created.
# Both variables refer to the same object.
#
# a is b
# True


# SHALLOW COPY
#
# b = a.copy()
#
# A new outer list is created.
# Nested mutable objects are still shared.
#
# a is b
# False
#
# a[2] is b[2]
# True


# DEEP COPY
#
# b = copy.deepcopy(a)
#
# A new outer list is created.
# Nested objects are also copied.
#
# a is b
# False
#
# a[2] is b[2]
# False


# ============================================================
# ONE-LINE MEMORY TRICK
# ============================================================

# Normal assignment:
# "Same object, different reference name."
#
# Shallow copy:
# "Outer copy, inner objects shared."
#
# Deep copy:
# "Outer copy + inner objects copied."