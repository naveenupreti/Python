# ================================================================
#                 PYTHON LISTS - COMPLETE PROGRAM
# ================================================================
#
# This program demonstrates the major concepts of Python Lists.
#
# Topics Covered:
# 1. Introduction to Lists
# 2. Creating Lists
# 3. Accessing List Elements
# 4. Positive and Negative Indexing
# 5. List Slicing
# 6. List Operations
# 7. Membership Operators
# 8. Concatenation and Repetition
# 9. Traversing Lists
# 10. Working with Lists
# 11. append() vs extend()
# 12. insert()
# 13. remove(), pop(), clear(), del
# 14. index() and count()
# 15. sort() vs sorted()
# 16. reverse()
# 17. List Functions: len(), min(), max(), sum(), etc.
# 18. List Comprehension
# 19. Nested Lists
# 20. Aliasing
# 21. Shallow Copy vs Deep Copy
# 22. Copying using slicing and copy()
# 23. Lists with functions
# 24. Mutable nature of Lists
# 25. Practical Example
# ================================================================


import copy


# ================================================================
# 1. INTRODUCTION TO LISTS
# ================================================================

# A list is an ORDERED and MUTABLE collection of elements.
#
# ORDERED means:
# - Elements maintain a definite sequence.
# - Each element has a position called an INDEX.
# - We can access elements using their indexes.
#
# MUTABLE means:
# - A list can be changed after it is created.
# - We can change existing elements.
# - We can add new elements.
# - We can remove elements.
#
# Lists are written using square brackets [].

numbers = [10, 20, 30, 40, 50]

print("1. Original list:", numbers)
# Output:
# 1. Original list: [10, 20, 30, 40, 50]


# A list can contain elements of different data types.
# Such a list is called a heterogeneous list.

mixed = [10, "Python", 3.14, True]

print("2. Mixed list:", mixed)
# Output:
# 2. Mixed list: [10, 'Python', 3.14, True]


# A list can also be empty.
# An empty list contains zero elements.

empty_list = []

print("3. Empty list:", empty_list)
# Output:
# 3. Empty list: []


# ================================================================
# 2. ACCESSING LIST ELEMENTS
# ================================================================

# Python uses ZERO-BASED indexing.
#
# For:
#     fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
#
# Positive indexes:
#
#     Apple    Banana    Mango    Orange    Grapes
#       0        1         2        3         4
#
# Negative indexes:
#
#     Apple    Banana    Mango    Orange    Grapes
#      -5       -4        -3       -2        -1

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("4. First element:", fruits[0])
# Output:
# 4. First element: Apple


print("5. Third element:", fruits[2])
# Output:
# 5. Third element: Mango


# -1 always refers to the last element.

print("6. Last element:", fruits[-1])
# Output:
# 6. Last element: Grapes


# -2 refers to the second-last element.

print("7. Second-last element:", fruits[-2])
# Output:
# 7. Second-last element: Orange


# ================================================================
# 3. LIST SLICING
# ================================================================

# Slicing is used to extract a portion of a list.
#
# General syntax:
#
#     list[start : stop : step]
#
# start → starting index; INCLUDED
# stop  → ending index; EXCLUDED
# step  → amount by which the index moves
#
# IMPORTANT:
# The stop index is NEVER included.

print("8. First three fruits:", fruits[0:3])
# Output:
# 8. First three fruits: ['Apple', 'Banana', 'Mango']
#
# Indexes 0, 1 and 2 are included.
# Index 3 is excluded.


# If start is omitted, slicing starts from index 0.

print("9. Fruits from index 2:", fruits[2:])
# Output:
# 9. Fruits from index 2: ['Mango', 'Orange', 'Grapes']


# If stop is omitted, slicing continues to the end.

print("10. Fruits before index 3:", fruits[:3])
# Output:
# 10. Fruits before index 3: ['Apple', 'Banana', 'Mango']


# A step of -1 moves backwards.
# Therefore, [::-1] creates a reversed copy of the list.

print("11. Reverse list using slicing:", fruits[::-1])
# Output:
# 11. Reverse list using slicing: ['Grapes', 'Orange', 'Mango', 'Banana', 'Apple']
#
# IMPORTANT:
# Slicing does NOT modify the original list.
# It creates a new list.

print("Original fruits:", fruits)
# Output:
# Original fruits: ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']


# [::2] means:
# Start from beginning, go to end, and take every second element.

print("12. Every second element:", fruits[::2])
# Output:
# 12. Every second element: ['Apple', 'Mango', 'Grapes']


# ================================================================
# 4. MODIFYING LIST ELEMENTS
# ================================================================

# Lists are mutable.
# Therefore, an individual element can be changed
# using its index.

numbers = [10, 20, 30, 40, 50]

numbers[1] = 200

print("13. After changing second element:", numbers)
# Output:
# 13. After changing second element: [10, 200, 30, 40, 50]
#
# Index 1 originally contained 20.
# It has now been replaced by 200.


# ------------------------------------------------
# Slice assignment
# ------------------------------------------------

# We can also replace multiple elements using slicing.
#
# numbers[2:5] refers to indexes:
#     2, 3, 4
#
# The stop index 5 is excluded.

numbers[2:5] = [300, 400]

print("14. After slice assignment:", numbers)
# Output:
# 14. After slice assignment: [10, 200, 300, 400, 50]
#
# IMPORTANT:
# The slice originally contained THREE elements:
#     [30, 40, 50]
#
# We replaced those three elements with TWO elements:
#     [300, 400]
#
# Therefore, the length of the list decreased by 1.


# We can also replace three elements with three new elements.

numbers[2:5] = [300, 400, 500]

print("15. After slice assignment:", numbers)
# Output:
# 15. After slice assignment: [10, 200, 300, 400, 500]


# ================================================================
# 5. LIST OPERATIONS
# ================================================================

a = [1, 2, 3]
b = [4, 5, 6]


# ------------------------------------------------
# Concatenation using +
# ------------------------------------------------

# The + operator joins two lists.
#
# It creates a NEW list.
# The original lists are not modified.

c = a + b

print("16. Concatenation:", c)
# Output:
# 16. Concatenation: [1, 2, 3, 4, 5, 6]


print("17. Original a:", a)
# Output:
# 17. Original a: [1, 2, 3]


print("18. Original b:", b)
# Output:
# 18. Original b: [4, 5, 6]


# ------------------------------------------------
# += operator
# ------------------------------------------------

# For normal Python lists:
#
#     a += b
#
# modifies the existing list in place.
#
# It is similar in effect to:
#
#     a.extend(b)
#
# But technically:
#     += is an operator
#     extend() is a list method.

a = [1, 2, 3]
b = [4, 5]

a += b

print("19. After a += b:", a)
# Output:
# 19. After a += b: [1, 2, 3, 4, 5]


# ------------------------------------------------
# += with aliasing
# ------------------------------------------------

# Aliasing means two variables refer to the SAME object.
#
# Here:
#
#     b = a
#
# does NOT create a copy.
# Both a and b refer to the same list.

a = [1, 2, 3]
b = a

a += [4, 5]

print("20. a after a += [4, 5]:", a)
# Output:
# 20. a after a += [4, 5]: [1, 2, 3, 4, 5]


print("21. b after a += [4, 5]:", b)
# Output:
# 21. b after a += [4, 5]: [1, 2, 3, 4, 5]
#
# Why did b also change?
# Because a and b refer to the SAME list.
#
# += modifies that existing list.


# ------------------------------------------------
# + versus += with aliases
# ------------------------------------------------

# Now consider:
#
#     a = a + [4, 5]
#
# The + operator creates a NEW list.
# Then a is made to refer to that new list.

a = [1, 2, 3]
b = a

a = a + [4, 5]

print("22. a after a = a + [4, 5]:", a)
# Output:
# 22. a after a = a + [4, 5]: [1, 2, 3, 4, 5]


print("23. b after a = a + [4, 5]:", b)
# Output:
# 23. b after a = a + [4, 5]: [1, 2, 3]
#
# Why did b NOT change?
#
# a + [4, 5] created a NEW list.
# a was then assigned to that new list.
# b still refers to the old list.
#
# This demonstrates the difference between:
#
#     a += b
#     a = a + b


# ------------------------------------------------
# Repetition using *
# ------------------------------------------------

# The * operator repeats the elements of a list.

d = [1, 2] * 3

print("24. Repetition:", d)
# Output:
# 24. Repetition: [1, 2, 1, 2, 1, 2]


# ================================================================
# 6. MEMBERSHIP OPERATORS
# ================================================================

# "in" checks whether a value exists in the list.
# It returns True or False.

a = [1, 2, 3, 4, 5]

print("25. Is 2 present?", 2 in a)
# Output:
# 25. Is 2 present? True


# "not in" checks whether a value does NOT exist in the list.

print("26. Is 10 absent?", 10 not in a)
# Output:
# 26. Is 10 absent? True


# ================================================================
# 7. append() VS extend() - VERY IMPORTANT
# ================================================================

# append() adds ONE object to the end of a list.
#
# It treats its argument as ONE element.

list1 = [1, 2, 3]

list1.append(4)

print("27. append(4):", list1)
# Output:
# 27. append(4): [1, 2, 3, 4]


# If we append another list,
# the ENTIRE list becomes one element.

list1.append([5, 6])

print("28. append([5, 6]):", list1)
# Output:
# 28. append([5, 6]): [1, 2, 3, 4, [5, 6]]
#
# Notice:
# [5, 6] remains together as ONE element.


# ------------------------------------------------
# extend()
# ------------------------------------------------

# extend() adds the elements of an iterable
# individually to the end of the list.

list2 = [1, 2, 3]

list2.extend([4, 5, 6])

print("29. extend([4, 5, 6]):", list2)
# Output:
# 29. extend([4, 5, 6]): [1, 2, 3, 4, 5, 6]


# ------------------------------------------------
# append() versus extend()
# ------------------------------------------------

append_example = [1, 2]
extend_example = [1, 2]

append_example.append([3, 4])
extend_example.extend([3, 4])

print("30. append result:", append_example)
# Output:
# 30. append result: [1, 2, [3, 4]]


print("31. extend result:", extend_example)
# Output:
# 31. extend result: [1, 2, 3, 4]


# append() adds ONE object.
# Therefore, length increases by 1.

print("32. Length after append:", len(append_example))
# Output:
# 32. Length after append: 3


# extend() adds TWO elements in this example.
# Therefore, length increases by 2.

print("33. Length after extend:", len(extend_example))
# Output:
# 33. Length after extend: 4


# Important relationship:
#
#     a + b
#         → creates a NEW list
#
#     a += b
#         → modifies a in place
#
#     a.extend(b)
#         → modifies a in place
#
# For ordinary lists:
#
#     a += b
#     a.extend(b)
#
# have the same practical effect,
# although one is an operator and the other is a method.


# ================================================================
# 8. insert()
# ================================================================

# insert(index, value) inserts a value at a particular position.
#
# Syntax:
#
#     list.insert(index, value)
#
# Existing elements at that position and after it
# are shifted to the right.

colors = ["Red", "Blue", "Green"]

colors.insert(1, "Yellow")

print("34. After insert:", colors)
# Output:
# 34. After insert: ['Red', 'Yellow', 'Blue', 'Green']
#
# "Yellow" was inserted at index 1.
# "Blue" and "Green" shifted one position to the right.


# ================================================================
# 9. remove()
# ================================================================

# remove(value) removes the FIRST occurrence of the specified value.
#
# It searches by VALUE, not by index.

values = [10, 20, 30, 20, 40]

values.remove(20)

print("35. After remove(20):", values)
# Output:
# 35. After remove(20): [10, 30, 20, 40]
#
# There were two 20s.
# Only the FIRST 20 was removed.


# IMPORTANT:
# remove() returns None.
# It changes the original list.


# ================================================================
# 10. pop()
# ================================================================

# pop() removes an element AND returns the removed element.
#
# Without an index:
#
#     list.pop()
#
# removes the LAST element.

values = [10, 20, 30, 40]

removed = values.pop()

print("36. Popped element:", removed)
# Output:
# 36. Popped element: 40


print("37. List after pop():", values)
# Output:
# 37. List after pop(): [10, 20, 30]


# ------------------------------------------------
# pop(index)
# ------------------------------------------------

# pop(index) removes and returns the element
# at the specified index.

removed = values.pop(1)

print("38. Popped element at index 1:", removed)
# Output:
# 38. Popped element at index 1: 20


print("39. List after pop(1):", values)
# Output:
# 39. List after pop(1): [10, 30]


# Important difference:
#
# remove(value)
#     → removes by VALUE
#
# pop(index)
#     → removes by INDEX
#     → returns removed value


# ================================================================
# 11. del AND clear()
# ================================================================

# del is a Python statement, NOT a list method.
#
# It can delete an element using its index.

a = [10, 20, 30, 40]

del a[1]

print("40. After del a[1]:", a)
# Output:
# 40. After del a[1]: [10, 30, 40]


# Unlike pop(), del does NOT return the deleted element.


# ------------------------------------------------
# del with slicing
# ------------------------------------------------

# del can delete multiple elements using a slice.

a = [10, 20, 30, 40, 50]

del a[1:4]

print("41. After del a[1:4]:", a)
# Output:
# 41. After del a[1:4]: [10, 50]
#
# Indexes 1, 2 and 3 were deleted.


# ------------------------------------------------
# del the entire variable
# ------------------------------------------------

# del can also delete the variable/reference itself.

a = [10, 20, 30]

del a

# After:
#
#     del a
#
# the variable a no longer exists.
#
# This is different from:
#
#     a.clear()
#
# clear() keeps the list variable alive but removes
# all its elements.


# ------------------------------------------------
# clear()
# ------------------------------------------------

# clear() removes ALL elements from a list.
# The list itself continues to exist.

temp = [1, 2, 3, 4]

temp.clear()

print("42. After clear():", temp)
# Output:
# 42. After clear(): []
#
# temp still exists.
# It is now an empty list.


# ================================================================
# 12. index() AND count()
# ================================================================

# index(value) returns the index of the FIRST occurrence
# of the specified value.

data = [10, 20, 30, 20, 40, 20]

print("43. Index of 20:", data.index(20))
# Output:
# 43. Index of 20: 1
#
# The first 20 occurs at index 1.

# there is no method to find the last occurrance of a specified value in a list
# write a program to find the last occurance of a specified value in a list

# count(value) returns how many times the value occurs.

print("44. Number of times 20 occurs:", data.count(20))
# Output:
# 44. Number of times 20 occurs: 3


# ================================================================
# 13. SORTING LISTS
# ================================================================

# sort() sorts the ORIGINAL list in ascending order by default.

marks = [78, 45, 92, 61, 88]

marks.sort()

print("45. Sorted in ascending order:", marks)
# Output:
# 45. Sorted in ascending order: [45, 61, 78, 88, 92]


# reverse=True makes sort() arrange the values
# in descending order.

marks.sort(reverse=True)

print("46. Sorted in descending order:", marks)
# Output:
# 46. Sorted in descending order: [92, 88, 78, 61, 45]


# ================================================================
# 14. sort() VS sorted() - IMPORTANT
# ================================================================

# sort() is a LIST METHOD.
#
# It changes the original list.
# It returns None.

data = [30, 10, 20]

result = data.sort()

print("47. List after sort():", data)
# Output:
# 47. List after sort(): [10, 20, 30]


print("48. Return value of sort():", result)
# Output:
# 48. Return value of sort(): None


# ------------------------------------------------
# sorted()
# ------------------------------------------------

# sorted() is a BUILT-IN FUNCTION.
#
# It does NOT modify the original list.
# It creates and returns a NEW sorted list.

data = [30, 10, 20]

new_data = sorted(data)

print("49. Original list after sorted():", data)
# Output:
# 49. Original list after sorted(): [30, 10, 20]


print("50. New sorted list:", new_data)
# Output:
# 50. New sorted list: [10, 20, 30]


# Remember:
#
#     sort()
#         → modifies original
#         → returns None
#
#     sorted()
#         → creates new sorted result
#         → original remains unchanged


# ================================================================
# 15. reverse() VS reversed() VS SLICING
# ================================================================

# There are three common ways to reverse a list.


# ------------------------------------------------
# Method 1: reverse()
# ------------------------------------------------

# reverse() is a LIST METHOD.
#
# It reverses the ORIGINAL list in place.
# It returns None.

numbers = [1, 2, 3, 4, 5]

result = numbers.reverse()

print("51. After reverse():", numbers)
# Output:
# 51. After reverse(): [5, 4, 3, 2, 1]


print("52. Return value of reverse():", result)
# Output:
# 52. Return value of reverse(): None


# ------------------------------------------------
# Method 2: reversed()
# ------------------------------------------------

# reversed() is a BUILT-IN FUNCTION.
#
# It does NOT modify the original list.
# It returns a reverse iterator.
#
# list(reversed(numbers)) converts that iterator
# into a new list.

numbers = [1, 2, 3, 4, 5]

new_numbers = list(reversed(numbers))

print("53. Original after reversed():", numbers)
# Output:
# 53. Original after reversed(): [1, 2, 3, 4, 5]


print("54. New reversed list:", new_numbers)
# Output:
# 54. New reversed list: [5, 4, 3, 2, 1]


# ------------------------------------------------
# Method 3: slicing [::-1]
# ------------------------------------------------

# [::-1] creates a NEW reversed list.
#
# The original list is not modified.

numbers = [1, 2, 3, 4, 5]

new_numbers = numbers[::-1]

print("55. Original after slicing:", numbers)
# Output:
# 55. Original after slicing: [1, 2, 3, 4, 5]


print("56. New reversed list:", new_numbers)
# Output:
# 56. New reversed list: [5, 4, 3, 2, 1]


# Final comparison:
#
# reverse()
#     → list method
#     → modifies original
#     → returns None
#
# reversed()
#     → built-in function
#     → original unchanged
#     → returns iterator
#
# [::-1]
#     → slicing
#     → original unchanged
#     → returns a new list


# ================================================================
# 16. IMPORTANT LIST FUNCTIONS
# ================================================================

numbers = [10, 20, 30, 40, 50]


# len() returns the number of elements.

print("57. Length:", len(numbers))
# Output:
# 57. Length: 5


# min() returns the smallest value.

print("58. Minimum:", min(numbers))
# Output:
# 58. Minimum: 10


# max() returns the largest value.

print("59. Maximum:", max(numbers))
# Output:
# 59. Maximum: 50


# sum() returns the total of numeric elements.

print("60. Sum:", sum(numbers))
# Output:
# 60. Sum: 150


# ------------------------------------------------
# any()
# ------------------------------------------------

# any() returns True if AT LEAST ONE element is truthy.
#
# 0 is considered False.
# Non-zero numbers are considered True.

values = [0, 0, 5, 0]

print("61. any(values):", any(values))
# Output:
# 61. any(values): True
#
# 5 is truthy, so any() returns True.


# ------------------------------------------------
# all()
# ------------------------------------------------

# all() returns True only if ALL elements are truthy.

values = [1, 2, 3]

print("62. all(values):", all(values))
# Output:
# 62. all(values): True
#
# All three values are non-zero and therefore truthy.


# ================================================================
# 17. TRAVERSING A LIST
# ================================================================

# Traversing means visiting each element of a list one by one.

names = ["Amit", "Ravi", "Neha"]

print("63. Traversing using for loop:")

for name in names:
    print(name)

# Output:
# 63. Traversing using for loop:
# Amit
# Ravi
# Neha


# ================================================================
# 18. enumerate()
# ================================================================

# enumerate() gives us BOTH:
#
#     index
#     value
#
# during traversal.

for index, name in enumerate(names):
    print("Index:", index, "Value:", name)

# Output:
# Index: 0 Value: Amit
# Index: 1 Value: Ravi
# Index: 2 Value: Neha


# ================================================================
# 19. LIST COMPREHENSION
# ================================================================

# List comprehension provides a short way to create lists.


# ------------------------------------------------
# Traditional approach
# ------------------------------------------------

squares = []

for i in range(1, 6):
    squares.append(i * i)

print("64. Squares using loop:", squares)
# Output:
# 64. Squares using loop: [1, 4, 9, 16, 25]


# ------------------------------------------------
# Using list comprehension
# ------------------------------------------------

# General form:
#
#     [expression for item in iterable]
#
# Here:
#
#     i * i
#         → expression
#
#     for i in range(1, 6)
#         → loop

squares = [i * i for i in range(1, 6)]

print("65. Squares using comprehension:", squares)
# Output:
# 65. Squares using comprehension: [1, 4, 9, 16, 25]


# ------------------------------------------------
# List comprehension with condition
# ------------------------------------------------

# General form:
#
#     [expression for item in iterable if condition]

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print("66. Even numbers:", even_numbers)
# Output:
# 66. Even numbers: [2, 4, 6, 8, 10]
#
# Only values satisfying:
#
#     i % 2 == 0
#
# are included.


# ================================================================
# 20. NESTED LISTS
# ================================================================

# A list can contain other lists.
# Such a structure is called a nested list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("67. Matrix:", matrix)
# Output:
# 67. Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# matrix[1] accesses the second inner list.

print("68. Second row:", matrix[1])
# Output:
# 68. Second row: [4, 5, 6]


# matrix[1][1] means:
#
#     first [1] → second row
#     second [1] → second element of that row

print("69. Middle element:", matrix[1][1])
# Output:
# 69. Middle element: 5


# ================================================================
# 21. ALIASING - VERY IMPORTANT
# ================================================================

# Aliasing occurs when two variables refer to the SAME object.
#
# Example:
#
#     b = a
#
# This does NOT create a copy.

a = [10, 20, 30]
b = a

b.append(40)

print("70. Original list after modifying b:", a)
# Output:
# 70. Original list after modifying b: [10, 20, 30, 40]


print("71. b:", b)
# Output:
# 71. b: [10, 20, 30, 40]


print("72. Are a and b the same object?", a is b)
# Output:
# 72. Are a and b the same object? True
#
# Because:
#
#     a ──────┐
#             ↓
#          [10,20,30,40]
#             ↑
#     b ──────┘


# ================================================================
# 22. COPYING A LIST USING SLICING
# ================================================================

# a[:] creates a new outer list.
#
# For a simple one-dimensional list,
# this gives us an independent outer list.

a = [10, 20, 30]

b = a[:]

b.append(40)

print("73. Original a:", a)
# Output:
# 73. Original a: [10, 20, 30]


print("74. Copied b:", b)
# Output:
# 74. Copied b: [10, 20, 30, 40]


print("75. Are a and b the same object?", a is b)
# Output:
# 75. Are a and b the same object? False


# IMPORTANT:
# a[:] is a SHALLOW copy.
#
# It creates a new outer list,
# but nested mutable objects are still shared.


# ================================================================
# 23. SHALLOW COPY VS DEEP COPY - VERY IMPORTANT
# ================================================================

# This is one of the most important concepts when
# working with nested lists.
#
# Consider:
#
#     original = [[1, 2], [3, 4]]
#
# There is an outer list containing two inner lists.
#
# A shallow copy creates:
#
#     NEW outer list
#     SAME inner lists
#
# A deep copy creates:
#
#     NEW outer list
#     NEW inner lists


# ------------------------------------------------
# SHALLOW COPY
# ------------------------------------------------

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

# Modify the first inner list.

shallow[0][0] = 999

print("76. Original after shallow nested modification:", original)
# Output:
# 76. Original after shallow nested modification: [[999, 2], [3, 4]]


print("77. Shallow copy:", shallow)
# Output:
# 77. Shallow copy: [[999, 2], [3, 4]]
#
# Why did original also change?
#
# Because the inner list [1, 2] is shared.


print("78. Is outer list same?", original is shallow)
# Output:
# 78. Is outer list same? False
#
# The outer lists are different.


print("79. Is first inner list same?", original[0] is shallow[0])
# Output:
# 79. Is first inner list same? True
#
# The first inner lists are the SAME object.


# ------------------------------------------------
# DEEP COPY
# ------------------------------------------------

# Reset original.

original = [
    [1, 2],
    [3, 4]
]

# deepcopy() recursively copies the complete structure.

deep = copy.deepcopy(original)

deep[0][0] = 999

print("80. Original after deep modification:", original)
# Output:
# 80. Original after deep modification: [[1, 2], [3, 4]]
#
# The original is NOT affected.


print("81. Deep copy:", deep)
# Output:
# 81. Deep copy: [[999, 2], [3, 4]]


print("82. Is outer list same?", original is deep)
# Output:
# 82. Is outer list same? False


print("83. Is first inner list same?", original[0] is deep[0])
# Output:
# 83. Is first inner list same? False
#
# Both the outer list and inner list are different objects.


# ------------------------------------------------
# FINAL COPY COMPARISON
# ------------------------------------------------

# NORMAL ASSIGNMENT:
#
#     b = a
#
#     Outer object  → SAME
#     Inner objects → SAME
#
#     No actual copy is created.


# SHALLOW COPY:
#
#     b = a.copy()
#     b = a[:]
#     b = copy.copy(a)
#
#     Outer object  → DIFFERENT
#     Inner objects → SAME
#
#     Only the outer structure is copied.


# DEEP COPY:
#
#     b = copy.deepcopy(a)
#
#     Outer object  → DIFFERENT
#     Inner objects → DIFFERENT
#
#     The complete nested structure is copied.


# ================================================================
# 24. SHALLOW COPY - ANOTHER TRICKY CASE
# ================================================================

original = [[1, 2], [3, 4]]

shallow = original.copy()


# Adding a completely NEW element to shallow:
#
# This changes only the outer shallow list.

shallow.append([5, 6])

print("84. Original after shallow append:", original)
# Output:
# 84. Original after shallow append: [[1, 2], [3, 4]]


print("85. Shallow copy after append:", shallow)
# Output:
# 85. Shallow copy after append: [[1, 2], [3, 4], [5, 6]]
#
# Original did not change because the outer lists are different.


# But if we modify an EXISTING inner list:
#
# The change is visible in both lists because
# the existing inner list is shared.

shallow[0].append(999)

print("86. Original after nested append:", original)
# Output:
# 86. Original after nested append: [[1, 2, 999], [3, 4]]


print("87. Shallow copy after nested append:", shallow)
# Output:
# 87. Shallow copy after nested append: [[1, 2, 999], [3, 4], [5, 6]]


# This demonstrates the two sides of shallow copying:
#
# Change outer list:
#     → original NOT affected
#
# Change shared inner list:
#     → original IS affected


# ================================================================
# 25. FUNCTIONS WITH LISTS
# ================================================================

# Lists can be passed to functions just like other objects.


def calculate_total(values):

    return sum(values)


marks = [80, 75, 90, 85]

total = calculate_total(marks)

print("88. Total marks:", total)
# Output:
# 88. Total marks: 330


# ------------------------------------------------
# Function modifying a list
# ------------------------------------------------

# Lists are mutable.
#
# Therefore, a function can modify the original list
# if it changes the list itself.

def add_value(values):

    values.append(100)


numbers = [10, 20, 30]

add_value(numbers)

print("89. List after function:", numbers)
# Output:
# 89. List after function: [10, 20, 30, 100]
#
# The original list changed because append()
# modified the same list object.


# ================================================================
# 26. FUNCTION TO FIND EVEN NUMBERS
# ================================================================

def get_even_numbers(values):

    result = []

    for value in values:

        if value % 2 == 0:
            result.append(value)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("90. Even numbers from function:",
      get_even_numbers(numbers))
# Output:
# 90. Even numbers from function: [2, 4, 6, 8]


# ================================================================
# 27. COPYING LIST INSIDE A FUNCTION
# ================================================================

# If we want to modify a list inside a function
# WITHOUT modifying the caller's original list,
# we can first create a copy.

def add_without_changing_original(values):

    # copy() creates a new outer list.
    new_values = values.copy()

    # This modifies the copy, not the original.
    new_values.append(100)

    return new_values


numbers = [10, 20, 30]

new_numbers = add_without_changing_original(numbers)

print("91. Original list:", numbers)
# Output:
# 91. Original list: [10, 20, 30]


print("92. New list:", new_numbers)
# Output:
# 92. New list: [10, 20, 30, 100]


# ================================================================
# 28. LIST OF STRINGS
# ================================================================

students = ["Amit", "Ravi", "Neha", "Priya"]

print("93. Number of students:", len(students))
# Output:
# 93. Number of students: 4


# sorted() returns a NEW sorted list.
# The original students list is not modified.

print("94. Alphabetically sorted:", sorted(students))
# Output:
# 94. Alphabetically sorted: ['Amit', 'Neha', 'Priya', 'Ravi']


# ================================================================
# 29. JOINING LIST ELEMENTS INTO A STRING
# ================================================================

# join() combines string elements of a list into one string.
#
# " ".join(words)
#
# means:
# Join the elements using a SPACE as the separator.

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print("95. Joined string:", sentence)
# Output:
# 95. Joined string: Python is easy


# ================================================================
# 30. CONVERTING OTHER ITERABLES INTO LISTS
# ================================================================

# range() produces a sequence of numbers.
# list() converts that sequence into an actual list.

numbers = list(range(1, 6))

print("96. List from range:", numbers)
# Output:
# 96. List from range: [1, 2, 3, 4, 5]


# A string is also iterable.
# list() converts each character into a separate element.

letters = list("PYTHON")

print("97. List from string:", letters)
# Output:
# 97. List from string: ['P', 'Y', 'T', 'H', 'O', 'N']


# ================================================================
# 31. zip() WITH LISTS
# ================================================================

# zip() combines corresponding elements from multiple iterables.
#
# names:
#     Amit, Ravi, Neha
#
# marks:
#     80,   90,   85
#
# zip() pairs them as:
#
#     (Amit, 80)
#     (Ravi, 90)
#     (Neha, 85)

names = ["Amit", "Ravi", "Neha"]
marks = [80, 90, 85]

student_data = list(zip(names, marks))

print("98. Zipped list:", student_data)
# Output:
# 98. Zipped list: [('Amit', 80), ('Ravi', 90), ('Neha', 85)]


# ================================================================
# 32. PRACTICAL LIST PROGRAM
# ================================================================

# We can use built-in list functions to calculate:
#
#     Total
#     Average
#     Highest mark
#     Lowest mark

marks = [78, 85, 92, 67, 88]

total = sum(marks)

average = total / len(marks)

highest = max(marks)

lowest = min(marks)


print("99. Marks:", marks)
# Output:
# 99. Marks: [78, 85, 92, 67, 88]


print("100. Total:", total)
# Output:
# 100. Total: 410


print("101. Average:", average)
# Output:
# 101. Average: 82.0


print("102. Highest:", highest)
# Output:
# 102. Highest: 92


print("103. Lowest:", lowest)
# Output:
# 103. Lowest: 67


# ================================================================
# 33. FINAL QUICK REVISION
# ================================================================

# LIST:
#     Ordered + Mutable collection
#
# INDEXING:
#     Positive index starts from 0.
#     Negative index starts from -1.
#
# SLICING:
#     list[start:stop:step]
#     start included
#     stop excluded
#
# append(x):
#     Adds ONE object.
#
# extend(iterable):
#     Adds elements individually.
#
# insert(index, value):
#     Inserts at a specified position.
#
# remove(value):
#     Removes FIRST occurrence by value.
#
# pop(index):
#     Removes by index AND returns the removed value.
#
# del:
#     Deletes element/slice/variable.
#
# clear():
#     Removes all elements but keeps the list.
#
# index(value):
#     Returns index of first occurrence.
#
# count(value):
#     Counts occurrences.
#
# sort():
#     Modifies original list.
#     Returns None.
#
# sorted():
#     Creates a new sorted list.
#
# reverse():
#     Reverses original list in place.
#     Returns None.
#
# reversed():
#     Returns a reverse iterator.
#     Does not modify original.
#
# [::-1]:
#     Creates a new reversed list.
#
# a = b:
#     Aliasing; same object.
#
# a.copy() / a[:]:
#     Shallow copy.
#
# copy.deepcopy(a):
#     Deep copy.
#
# LIST COMPREHENSION:
#     Short way to create lists.
#
# NESTED LIST:
#     A list containing other lists.
#
# ================================================================
# END OF PYTHON LISTS COMPLETE PROGRAM
# ================================================================
