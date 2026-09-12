# ==============================================================
# Check type(), id(), == and is at RUN TIME
# ==============================================================
#
# Enter numbers such as:
# -6, -5, 0, 256, 257
#
# Python (especially CPython) commonly caches integers -5 to 256.
# But caching is an implementation detail, NOT a Python language rule.
#
# int(input()) creates the integer from user input at run time.
# We create TWO separate objects so that == and is can be compared.
# ==============================================================


# Take the same number twice from the user
a = int(input("Enter an integer for object a: "))
b = int(input("Enter the same integer for object b: "))


print("\n---------------- RESULT ----------------")

# type() tells us the type/class of the object
print("type(a) =", type(a))
print("type(b) =", type(b))

# id() gives the identity of each object
print("id(a)   =", id(a))
print("id(b)   =", id(b))

# == compares VALUES
print("a == b  =", a == b)

# is compares OBJECT IDENTITY
print("a is b  =", a is b)


# ==============================================================
# INTERPRETATION
# ==============================================================

# If:
#     a == b → True
#
# it means both objects contain the same VALUE.
#
# If:
#     a is b → True
#
# it means both variables refer to the EXACT SAME OBJECT.
#
# If:
#     a is b → False
#
# it means they are DIFFERENT OBJECTS, even if their values
# are equal.
#
# Therefore:
#
#     ==  → value comparison
#     is  → identity comparison
#     id() → object identity
#     type() → object's type
#
# --------------------------------------------------------------
# TRY THESE:
#
# Enter 256 and 256
# Enter 257 and 257
# Enter -5 and -5
# Enter -6 and -6
#
# On standard CPython, you will commonly observe:
#
#       Value       a == b       a is b
#       --------------------------------
#       -5          True         True
#       256         True         True
#       -6          True         False
#       257         True         False
#
# The first column is guaranteed by the values being equal.
# The "is" result depends on object caching/implementation.
# Do NOT use "is" to compare integers.
# Always use == for comparing integer values.
# ==============================================================

