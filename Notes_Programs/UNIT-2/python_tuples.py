"""
BMC301 - Python Programming
UNIT II : TUPLES

This single program demonstrates:
1. Introduction / creation of tuples
2. Accessing tuples
3. Tuple operations
4. Working with tuples
5. Built-in functions
6. Tuple methods
7. Important/tricky concepts:
   - Empty tuple
   - Singleton tuple
   - Tuple packing
   - Tuple unpacking
   - Extended unpacking
   - Negative indexing
   - Slicing
   - Concatenation and repetition
   - Membership
   - Immutability
   - Mutable object inside a tuple
   - Nested tuples
   - Tuple comparison
   - Function returning multiple values
   - sorted() returning a LIST
"""

print("=" * 60)
print("1. INTRODUCTION AND CREATION OF TUPLES")
print("=" * 60)

# A tuple is an ordered collection of immutable objects.
# Tuples are enclosed in parentheses () conventionally.
student = ("Naveen", 23, "MCA", 85.5)

print("student =", student)
# Output:
# student = ('Naveen', 24, 'MCA', 85.5)

# A tuple can contain values of different data types.
mixed = (10, "Python", 3.14, True)
print("mixed =", mixed)
# Output:
# mixed = (10, 'Python', 3.14, True)

# ------------------------------------------------------------
# TRICKY CONCEPT 1: EMPTY TUPLE
# ------------------------------------------------------------

empty_tuple = ()

print("empty_tuple =", empty_tuple)
print("type(empty_tuple) =", type(empty_tuple))
# Output:
# empty_tuple = ()
# type(empty_tuple) = <class 'tuple'>

# ------------------------------------------------------------
# TRICKY CONCEPT 2: SINGLETON TUPLE
# ------------------------------------------------------------

# IMPORTANT:
# (10) is NOT a tuple. It is simply an integer.
not_a_tuple = (10)

# The comma makes it a tuple.
single_tuple = (10,)

print("(10) =", not_a_tuple)
print("type((10)) =", type(not_a_tuple))

print("(10,) =", single_tuple)
print("type((10,)) =", type(single_tuple))

# Output:
# (10) = 10
# type((10)) = <class 'int'>
# (10,) = (10,)
# type((10,)) = <class 'tuple'>

# ------------------------------------------------------------
# TRICKY CONCEPT 3: tuple() FUNCTION
# ------------------------------------------------------------

# tuple() can convert an iterable into a tuple.
numbers = tuple([10, 20, 30, 40])

print("tuple([10, 20, 30, 40]) =", numbers)
# Output:
# tuple([10, 20, 30, 40]) = (10, 20, 30, 40)

print("\n" + "=" * 60)
print("2. TUPLE PACKING AND UNPACKING")
print("=" * 60)

# PACKING:
# Multiple values are automatically packed into one tuple.
packed = 10, 20, 30

print("packed =", packed)
print("type(packed) =", type(packed))
# Output:
# packed = (10, 20, 30)
# type(packed) = <class 'tuple'>

# UNPACKING:
# Values of a tuple are assigned to separate variables.
a, b, c = packed

print("a =", a)
print("b =", b)
print("c =", c)

# Output:
# a = 10
# b = 20
# c = 30

# ------------------------------------------------------------
# TRICKY CONCEPT 4: NUMBER OF VARIABLES MUST MATCH
# ------------------------------------------------------------

# The following would produce ValueError:
#
# a, b = (10, 20, 30)
#
# because there are 3 values but only 2 variables.

# ------------------------------------------------------------
# TRICKY CONCEPT 5: EXTENDED UNPACKING
# ------------------------------------------------------------

data = (10, 20, 30, 40, 50)

first, *middle, last = data

print("first =", first)
print("middle =", middle)
print("type(middle) =", type(middle))
print("last =", last)

# Output:
# first = 10
# middle = [20, 30, 40]
# type(middle) = <class 'list'>
# last = 50

# VERY IMPORTANT:
# *middle collects the remaining values into a LIST,
# not into a tuple.

print("\n" + "=" * 60)
print("3. ACCESSING TUPLES")
print("=" * 60)

marks = (78, 85, 92, 67, 88)

# Indexing starts from 0.
print("marks =", marks)
print("marks[0] =", marks[0])
print("marks[2] =", marks[2])

# Output:
# marks = (78, 85, 92, 67, 88)
# marks[0] = 78
# marks[2] = 92

# NEGATIVE INDEXING
# -1 means last element.
print("marks[-1] =", marks[-1])
print("marks[-2] =", marks[-2])

# Output:
# marks[-1] = 88
# marks[-2] = 67


# ------------------------------------------------------------
# SLICING
# ------------------------------------------------------------

print("marks[1:4] =", marks[1:4])
print("marks[:3] =", marks[:3])
print("marks[2:] =", marks[2:])
print("marks[::2] =", marks[::2])
print("marks[::-1] =", marks[::-1])

# Output:
# marks[1:4] = (85, 92, 67)
# marks[:3] = (78, 85, 92)
# marks[2:] = (92, 67, 88)
# marks[::2] = (78, 92, 88)
# marks[::-1] = (88, 67, 92, 85, 78)

# IMPORTANT:
# A slice of a tuple is also a tuple.


# ------------------------------------------------------------
# NESTED TUPLES
# ------------------------------------------------------------

nested = ("Python", (10, 20, 30), ("A", "B"))

print("nested =", nested)
print("nested[1] =", nested[1])
print("nested[1][2] =", nested[1][2])
print("nested[2][0] =", nested[2][0])

# Output:
# nested = ('Python', (10, 20, 30), ('A', 'B'))
# nested[1] = (10, 20, 30)
# nested[1][2] = 30
# nested[2][0] = A

print("\n" + "=" * 60)
print("4. TUPLE OPERATIONS")
print("=" * 60)

t1 = (1, 2, 3)
t2 = (4, 5)

# ------------------------------------------------------------
# CONCATENATION (+)
# ------------------------------------------------------------

result = t1 + t2

print("t1 + t2 =", result)
# Output:
# t1 + t2 = (1, 2, 3, 4, 5)

# ------------------------------------------------------------
# REPETITION (*)
# ------------------------------------------------------------

result = t1 * 2

print("t1 * 2 =", result)
# Output:
# t1 * 2 = (1, 2, 3, 1, 2, 3)


# ------------------------------------------------------------
# MEMBERSHIP OPERATORS
# ------------------------------------------------------------

print("2 in t1 =", 2 in t1)
print("10 in t1 =", 10 in t1)
print("10 not in t1 =", 10 not in t1)

# Output:
# 2 in t1 = True
# 10 in t1 = False
# 10 not in t1 = True

# ------------------------------------------------------------
# COMPARISON OF TUPLES
# ------------------------------------------------------------

print("(1, 2) == (1, 2) :", (1, 2) == (1, 2))
print("(1, 2) < (1, 3)  :", (1, 2) < (1, 3))
print("(2, 0) > (1, 100) :", (2, 0) > (1, 100))

# Output:
# (1, 2) == (1, 2) : True
# (1, 2) < (1, 3)  : True
# (2, 0) > (1, 100) : True

# TRICKY:
# Tuple comparison is lexicographical.
# Python first compares the first elements.
# If they are equal, it compares the next elements, and so on.

print("\n" + "=" * 60)
print("5. TUPLES ARE IMMUTABLE")
print("=" * 60)

immutable_tuple = (10, 20, 30)

print("immutable_tuple =", immutable_tuple)

# The following statement is NOT allowed:
#
# immutable_tuple[0] = 100
#
# It produces:
# TypeError: 'tuple' object does not support item assignment

try:
    immutable_tuple[0] = 100
except TypeError as e:
    print("Attempting immutable_tuple[0] = 100 gives:", e)

# Output:
# Attempting immutable_tuple[0] = 100 gives:
# 'tuple' object does not support item assignment


# ------------------------------------------------------------
# TRICKY CONCEPT 6:
# A TUPLE CAN CONTAIN A MUTABLE OBJECT
# ------------------------------------------------------------

# The tuple itself cannot have its elements replaced,
# but an object INSIDE the tuple may be mutable.

student_data = ("Naveen", [80, 85, 90])

print("Before modification:", student_data)

student_data[1].append(95)

print("After modification :", student_data)

# Output:
# Before modification: ('Naveen', [80, 85, 90])
# After modification : ('Naveen', [80, 85, 90, 95])

# IMPORTANT:
# The tuple has not changed its reference to the list.
# The LIST object inside the tuple was modified.


print("\n" + "=" * 60)
print("6. ITERATING / WORKING WITH TUPLES")
print("=" * 60)

subjects = ("Python", "DBMS", "Java", "OS")

print("Subjects:")

for subject in subjects:
    print(subject)

# Output:
# Subjects:
# Python
# DBMS
# Java
# OS


# Using index with range()
for i in range(len(subjects)):
    print(i, "->", subjects[i])

# Output:
# 0 -> Python
# 1 -> DBMS
# 2 -> Java
# 3 -> OS


# enumerate() gives index and value.
for index, subject in enumerate(subjects):
    print(index, subject)

# Output:
# 0 Python
# 1 DBMS
# 2 Java
# 3 OS


print("\n" + "=" * 60)
print("7. BUILT-IN FUNCTIONS USED WITH TUPLES")
print("=" * 60)

numbers = (10, 25, 5, 40, 15)

print("numbers =", numbers)
print("len(numbers) =", len(numbers))
print("max(numbers) =", max(numbers))
print("min(numbers) =", min(numbers))
print("sum(numbers) =", sum(numbers))

# Output:
# numbers = (10, 25, 5, 40, 15)
# len(numbers) = 5
# max(numbers) = 40
# min(numbers) = 5
# sum(numbers) = 95


# ------------------------------------------------------------
# sorted() TRICKY CONCEPT
# ------------------------------------------------------------

sorted_numbers = sorted(numbers)

print("sorted(numbers) =", sorted_numbers)
print("type(sorted(numbers)) =", type(sorted_numbers))

# Output:
# sorted(numbers) = [5, 10, 15, 25, 40]
# type(sorted(numbers)) = <class 'list'>

# IMPORTANT:
# sorted(tuple) returns a LIST.
# It does NOT return a tuple.


# If a tuple is specifically required:
print("tuple(sorted(numbers)) =", tuple(sorted(numbers)))

# Output:
# tuple(sorted(numbers)) = (5, 10, 15, 25, 40)


print("\n" + "=" * 60)
print("8. TUPLE METHODS")
print("=" * 60)

values = (10, 20, 10, 30, 10, 40)

# Tuple has two important built-in methods:
# count() and index()

print("values =", values)

print("values.count(10) =", values.count(10))
print("values.count(50) =", values.count(50))

# Output:
# values.count(10) = 3
# values.count(50) = 0


print("values.index(30) =", values.index(30))

# Output:
# values.index(30) = 3

# TRICKY:
# index() returns the FIRST occurrence.

print("values.index(10) =", values.index(10))

# Output:
# values.index(10) = 0

# If an item is absent, index() raises ValueError.
try:
    values.index(100)
except ValueError as e:
    print("values.index(100) gives:", e)

# Output:
# values.index(100) gives: tuple.index(x): x not in tuple

print("\n" + "=" * 60)
print("9. TUPLE AND FUNCTION RETURN VALUES")
print("=" * 60)

def calculate(a, b):
    """
    A function can return multiple values.

    return a + b, a - b, a * b

    The three values are automatically PACKED into a tuple.
    """
    return a + b, a - b, a * b


result = calculate(10, 5)

print("result =", result)
print("type(result) =", type(result))

# Output:
# result = (15, 5, 50)
# type(result) = <class 'tuple'>


# The returned tuple can be UNPACKED.
addition, subtraction, multiplication = calculate(10, 5)

print("addition =", addition)
print("subtraction =", subtraction)
print("multiplication =", multiplication)

# Output:
# addition = 15
# subtraction = 5
# multiplication = 50


print("\n" + "=" * 60)
print("10. SWAPPING VARIABLES USING TUPLE UNPACKING")
print("=" * 60)

x = 100
y = 200

print("Before swapping: x =", x, ", y =", y)

x, y = y, x

print("After swapping : x =", x, ", y =", y)

# Output:
# Before swapping: x = 100 , y = 200
# After swapping : x = 200 , y = 100

# This is a very important Python application
# of tuple packing and unpacking.


print("\n" + "=" * 60)
print("11. TRICKY CONCEPT: TUPLE HASHABILITY")
print("=" * 60)

# A tuple containing only immutable/hashable elements
# can generally be used as a dictionary key.

coordinate = (10, 20)

location = {
    coordinate: "Point A"
}

print("location =", location)
print("location[(10, 20)] =", location[(10, 20)])

# Output:
# location = {(10, 20): 'Point A'}
# location[(10, 20)] = Point A


# But a tuple containing a mutable object such as a list
# cannot be used as a dictionary key.

bad_key = (10, [20, 30])

try:
    test = {bad_key: "value"}
except TypeError as e:
    print("Tuple containing a list cannot be a dictionary key:", e)

# Output:
# Tuple containing a list cannot be a dictionary key:
# unhashable type: 'list'


print("\n" + "=" * 60)
print("12. IMPORTANT FINAL SUMMARY")
print("=" * 60)

summary = (
    "Ordered",
    "Indexed",
    "Allows duplicate values",
    "Can contain different data types",
    "Immutable",
    "Supports slicing",
    "Supports + and *",
    "Supports membership operators",
    "Supports packing/unpacking",
    "Has count() and index() methods"
)

for item in summary:
    print("-", item)

# Output:
# - Ordered
# - Indexed
# - Allows duplicate values
# - Can contain different data types
# - Immutable
# - Supports slicing
# - Supports + and *
# - Supports membership operators
# - Supports packing/unpacking
# - Has count() and index() methods