# ================================================================
#                 PYTHON LISTS - COMPLETE PROGRAM
# ================================================================
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
'''
A list is an ordered and mutable collection of elements.

A Python list is an ordered collection because its elements
maintain a definite position and can be accessed using indexes,
and it is mutable because its elements, size, and contents can
be changed after the list is created.

Lists are written using square brackets [].
'''
numbers = [10, 20, 30, 40, 50]

print("1. Original list:", numbers)
# Output: 1. Original list: [10, 20, 30, 40, 50]

# A list can contain different data types.
mixed = [10, "Python", 3.14, True]

print("2. Mixed list:", mixed)
# Output: 2. Mixed list: [10, 'Python', 3.14, True]

# A list can also be empty.
empty_list = []

print("3. Empty list:", empty_list)
# Output: 3. Empty list: []


# ================================================================
# 2. ACCESSING LIST ELEMENTS
# ================================================================

# List indexing starts from 0.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("4. First element:", fruits[0])
# Output: 4. First element: Apple

print("5. Third element:", fruits[2])
# Output: 5. Third element: Mango

print("6. Last element:", fruits[-1])
# Output: 6. Last element: Grapes

print("7. Second-last element:", fruits[-2])
# Output: 7. Second-last element: Orange


# ================================================================
# 3. LIST SLICING
# ================================================================

# Syntax:
# list[start : stop : step]
#
# start is included
# stop is excluded

print("8. First three fruits:", fruits[0:3])
# Output: 8. First three fruits: ['Apple', 'Banana', 'Mango']

print("9. Fruits from index 2:", fruits[2:])
# Output: 9. Fruits from index 2: ['Mango', 'Orange', 'Grapes']

print("10. Fruits before index 3:", fruits[:3])
# Output: 10. Fruits before index 3: ['Apple', 'Banana', 'Mango']

print("11. Reverse list using slicing:", fruits[::-1])
# Output: 11. Reverse list using slicing: ['Grapes', 'Orange', 'Mango', 'Banana', 'Apple']

print("12. Every second element:", fruits[::2])
# Output: 12. Every second element: ['Apple', 'Mango', 'Grapes']

# ================================================================
# 4. MODIFYING LIST ELEMENTS
# ================================================================

# Lists are mutable.
# Therefore, individual elements can be changed.

numbers = [10, 20, 30, 40, 50]
numbers[1] = 200
print("13. After changing second element:", numbers)
# Output: 13. After changing second element: [10, 200, 30, 40, 50]

# Multiple elements can be changed using slicing.
numbers[2:5] = [300, 400] # doesn't change the element at 4th index
print("14. After slice assignment:", numbers)
# Output: 14. After slice assignment: [10, 200, 300, 400, 50]

numbers[2:5] = [300, 400, 500] # changes all the elemnts from 2nd to 4th index
print("14. After slice assignment:", numbers)
# Output: 14. After slice assignment: [10, 200, 300, 400, 500]

# ================================================================
# 5. LIST OPERATIONS
# ================================================================

a = [1, 2, 3]
b = [4, 5, 6]

# ------------------------------------------------
# Concatenation (+)
# ------------------------------------------------
c = a + b
print("15. Concatenation:", c)
# Output: 15. Concatenation: [1, 2, 3, 4, 5, 6]

# += generally modifies the existing list in place, whereas a = a + b creates a new list.

# += → modifies the existing list
a = [1, 2, 3]
b = [4, 5]
a += b
print(a) # Here a is modified.
# [1, 2, 3, 4, 5]

# This distinction becomes specially interesting with aliases:
a = [1, 2, 3]
b = a # b and a both refer to the same list
a += [4, 5]
print(a)
# [1, 2, 3, 4, 5]
print(b)
# [1, 2, 3, 4, 5]
# Because a and b refer to the same list, the modification is visible through both.


a = [1, 2, 3]
b = a
a = a + [4, 5] # the concatenation operator + creates a new list
print(a)
# [1, 2, 3, 4, 5]
print(b)
# [1, 2, 3]
# This time b didn't change because
# a + [4, 5] created a new list, and then a was made to refer to that new list.

# ------------------------------------------------
# Repetition (*)
# ------------------------------------------------

d = [1, 2] * 3
print("16. Repetition:", d)
# Output: 16. Repetition: [1, 2, 1, 2, 1, 2]


# ------------------------------------------------
# Membership: in
# ------------------------------------------------

print("17. Is 2 present?", 2 in a)
# Output: 17. Is 2 present? True


# ------------------------------------------------
# Membership: not in
# ------------------------------------------------

print("18. Is 10 absent?", 10 not in a)
# Output: 18. Is 10 absent? True


# ================================================================
# 6. APPEND() VS EXTEND() - VERY IMPORTANT
# ================================================================

# append() adds ONE object as a single element.

list1 = [1, 2, 3]
list1.append(4)
print("19. append(4):", list1)
# Output: 19. append(4): [1, 2, 3, 4]


# append() adds the entire list as ONE element.

list1.append([5, 6])
print("20. append([5, 6]):", list1)
# Output: 20. append([5, 6]): [1, 2, 3, 4, [5, 6]]


# extend() adds each element individually.

list2 = [1, 2, 3]
list2.extend([4, 5, 6])
print("21. extend([4, 5, 6]):", list2)
# Output: 21. extend([4, 5, 6]): [1, 2, 3, 4, 5, 6]


# ------------------------------------------------
# Important difference:
# ------------------------------------------------

append_example = [1, 2]
extend_example = [1, 2]

append_example.append([3, 4])
extend_example.extend([3, 4])

print("22. append result:", append_example)
# Output: 22. append result: [1, 2, [3, 4]]

print("23. extend result:", extend_example)
# Output: 23. extend result: [1, 2, 3, 4]


# append() increases length by 1.
# extend() increases length by the number of elements added.

print("24. Length after append:", len(append_example))
# Output: 24. Length after append: 3

print("25. Length after extend:", len(extend_example))
# Output: 25. Length after extend: 4

'''
+= and extend() both extend a list in place, but += is an operator while extend() is a list method.
for ordinary lists, we can say:

a += b ≈ a.extend(b)

a + b          → NEW list
a += b         → modify a
a.extend(b)    → modify a

'''
# ================================================================
# 7. INSERT()
# ================================================================

# insert(index, value) inserts an element at a specified position.

colors = ["Red", "Blue", "Green"]
colors.insert(1, "Yellow")
print("26. After insert:", colors)
# Output: 26. After insert: ['Red', 'Yellow', 'Blue', 'Green']


# ================================================================
# 8. REMOVE()
# ================================================================

# remove() removes the FIRST occurrence of a value.

values = [10, 20, 30, 20, 40]
values.remove(20)
print("27. After remove(20):", values)
# Output: 27. After remove(20): [10, 30, 20, 40]


# ================================================================
# 9. POP()
# ================================================================

# pop() removes and RETURNS an element.
# Without an index, it removes the last element.

values = [10, 20, 30, 40]
removed = values.pop()
print("28. Popped element:", removed)
# Output: 28. Popped element: 40

print("29. List after pop():", values)
# Output: 29. List after pop(): [10, 20, 30]


# pop(index) removes an element at a particular index.

removed = values.pop(1)
print("30. Popped element at index 1:", removed)
# Output: 30. Popped element at index 1: 20

print("31. List after pop(1):", values)
# Output: 31. List after pop(1): [10, 30]


# ================================================================
# 10. del() and CLEAR()
# ================================================================
#del is a Python statement, not a list method.
#It can delete an element using its index.
a = [10, 20, 30, 40]
del a[1]
print(a)
# [10, 30, 40]

#Unlike pop(), del does not return the deleted element.
#del can delete multiple elements using slicing
a = [10, 20, 30, 40, 50]
del a[1:4]
print(a)
# [10, 50]


# del can delete the entire list variable
a = [10, 20, 30]
del a
# Now a itself no longer exists
# del a removes the variable/reference itself


# clear() removes all elements from the list.
# The list still exists; it is simply empty.
temp = [1, 2, 3, 4]
temp.clear()
print("32. After clear():", temp)
# Output: 32. After clear(): []


# ================================================================
# 11. INDEX() AND COUNT()
# ================================================================

data = [10, 20, 30, 20, 40, 20]
print("33. Index of 20:", data.index(20))
# Output: 33. Index of 20: 1

print("34. Number of times 20 occurs:", data.count(20))
# Output: 34. Number of times 20 occurs: 3


# ================================================================
# 12. SORTING LISTS
# ================================================================

marks = [78, 45, 92, 61, 88]
marks.sort()
print("35. Sorted in ascending order:", marks)
# Output: 35. Sorted in ascending order: [45, 61, 78, 88, 92]


# Sort in descending order.

marks.sort(reverse=True)
print("36. Sorted in descending order:", marks)
# Output: 36. Sorted in descending order: [92, 88, 78, 61, 45]


# ================================================================
# 13. sort() VS sorted() - IMPORTANT
# ================================================================

data = [30, 10, 20]
# sort() modifies the original list.
result = data.sort()
print("37. List after sort():", data)
# Output: 37. List after sort(): [10, 20, 30]

# sort() returns None.

print("38. Return value of sort():", result)
# Output: 38. Return value of sort(): None


# sorted() creates and returns a NEW sorted list.

data = [30, 10, 20]
new_data = sorted(data)
print("39. Original list after sorted():", data)
# Output: 39. Original list after sorted(): [30, 10, 20]

print("40. New sorted list:", new_data)
# Output: 40. New sorted list: [10, 20, 30]


# ================================================================
# 14. REVERSE()
# ================================================================

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("41. After reverse():", numbers) # reverse() changes the list.
# Output: 41. After reverse(): [5, 4, 3, 2, 1]

# reversed() doesn't change the original list.
numbers = [1, 2, 3, 4, 5]
new_numbers = list(reversed(numbers))
print(numbers)
# [1, 2, 3, 4, 5]
print(new_numbers)
# [5, 4, 3, 2, 1]

# reversed() itself returns an iterator; list(reversed(a)) creates a new list.

# ================================================================
# 15. IMPORTANT LIST FUNCTIONS
# ================================================================

numbers = [10, 20, 30, 40, 50]
print("42. Length:", len(numbers))
# Output: 42. Length: 5

print("43. Minimum:", min(numbers))
# Output: 43. Minimum: 10

print("44. Maximum:", max(numbers))
# Output: 44. Maximum: 50

print("45. Sum:", sum(numbers))
# Output: 45. Sum: 150


# any() returns True if at least one element is True.

values = [0, 0, 5, 0]
print("46. any(values):", any(values))
# Output: 46. any(values): True


# all() returns True only if all elements are True.

values = [1, 2, 3]
print("47. all(values):", all(values))
# Output: 47. all(values): True


# ================================================================
# 16. TRAVERSING A LIST
# ================================================================

names = ["Amit", "Ravi", "Neha"]
print("48. Traversing using for loop:")

for name in names:
    print(name)
# Output:
# 48. Traversing using for loop:
# Amit
# Ravi
# Neha


# ================================================================
# 17. ENUMERATE()
# ================================================================

# enumerate() gives both index and value.

for index, name in enumerate(names):
    print("Index:", index, "Value:", name)
# Output:
# Index: 0 Value: Amit
# Index: 1 Value: Ravi
# Index: 2 Value: Neha


# ================================================================
# 18. LIST COMPREHENSION
# ================================================================

# Traditional approach

squares = []

for i in range(1, 6):
    squares.append(i * i)

print("49. Squares using loop:", squares)
# Output: 49. Squares using loop: [1, 4, 9, 16, 25]


# Same operation using list comprehension.

squares = [i * i for i in range(1, 6)]

print("50. Squares using comprehension:", squares)
# Output: 50. Squares using comprehension: [1, 4, 9, 16, 25]


# List comprehension with condition.

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print("51. Even numbers:", even_numbers)
# Output: 51. Even numbers: [2, 4, 6, 8, 10]


# ================================================================
# 19. NESTED LISTS
# ================================================================

# A list can contain other lists.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("52. Matrix:", matrix)
# Output: 52. Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing row 1

print("53. Second row:", matrix[1])
# Output: 53. Second row: [4, 5, 6]

# Accessing an individual element.

print("54. Middle element:", matrix[1][1])
# Output: 54. Middle element: 5


# ================================================================
# 20. ALIASING - VERY IMPORTANT
# ================================================================

# When we write:
#
# b = a
#
# both variables refer to the SAME list.

a = [10, 20, 30]
b = a

b.append(40)

print("55. Original list after modifying b:", a)
# Output: 55. Original list after modifying b: [10, 20, 30, 40]

print("56. b:", b)
# Output: 56. b: [10, 20, 30, 40]

print("57. Are a and b the same object?", a is b)
# Output: 57. Are a and b the same object? True


# ================================================================
# 21. COPYING A LIST USING SLICING
# ================================================================

a = [10, 20, 30]

b = a[:]

b.append(40)

print("58. Original a:", a)
# Output: 58. Original a: [10, 20, 30]

print("59. Copied b:", b)
# Output: 59. Copied b: [10, 20, 30, 40]

print("60. Are a and b the same object?", a is b)
# Output: 60. Are a and b the same object? False


# ================================================================
# 22. SHALLOW COPY VS DEEP COPY - VERY IMPORTANT
# ================================================================

# A shallow copy creates a new outer list,
# but nested objects are still shared.

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(original)

# Modify a nested list through shallow copy.

shallow[0][0] = 999

print("61. Original after shallow nested modification:", original)
# Output: 61. Original after shallow nested modification: [[999, 2], [3, 4]]

print("62. Shallow copy:", shallow)
# Output: 62. Shallow copy: [[999, 2], [3, 4]]


# This happens because the INNER lists are shared.

print("63. Is outer list same?", original is shallow)
# Output: 63. Is outer list same? False

print("64. Is first inner list same?", original[0] is shallow[0])
# Output: 64. Is first inner list same? True


# ------------------------------------------------
# DEEP COPY
# ------------------------------------------------

# deepcopy() recursively copies the entire structure.

original = [
    [1, 2],
    [3, 4]
]

deep = copy.deepcopy(original)

deep[0][0] = 999

print("65. Original after deep modification:", original)
# Output: 65. Original after deep modification: [[1, 2], [3, 4]]

print("66. Deep copy:", deep)
# Output: 66. Deep copy: [[999, 2], [3, 4]]

print("67. Is outer list same?", original is deep)
# Output: 67. Is outer list same? False

print("68. Is first inner list same?", original[0] is deep[0])
# Output: 68. Is first inner list same? False


# ================================================================
# 23. SHALLOW COPY: ANOTHER TRICKY CASE
# ================================================================

original = [[1, 2], [3, 4]]

shallow = original.copy()

# Adding a NEW element to the outer shallow list
# does NOT modify the original outer list.

shallow.append([5, 6])

print("69. Original after shallow append:", original)
# Output: 69. Original after shallow append: [[1, 2], [3, 4]]

print("70. Shallow copy after append:", shallow)
# Output: 70. Shallow copy after append: [[1, 2], [3, 4], [5, 6]]


# But modifying an EXISTING nested list affects both.

shallow[0].append(999)

print("71. Original after nested append:", original)
# Output: 71. Original after nested append: [[1, 2, 999], [3, 4]]

print("72. Shallow copy after nested append:", shallow)
# Output: 72. Shallow copy after nested append: [[1, 2, 999], [3, 4], [5, 6]]


# ================================================================
# 24. FUNCTIONS WITH LISTS
# ================================================================

# Lists can be passed to functions.

def calculate_total(values):
    return sum(values)


marks = [80, 75, 90, 85]

total = calculate_total(marks)

print("73. Total marks:", total)
# Output: 73. Total marks: 330


# Function can modify a mutable list.

def add_value(values):
    values.append(100)


numbers = [10, 20, 30]

add_value(numbers)

print("74. List after function:", numbers)
# Output: 74. List after function: [10, 20, 30, 100]


# ================================================================
# 25. FUNCTION TO FIND EVEN NUMBERS
# ================================================================

def get_even_numbers(values):

    result = []

    for value in values:
        if value % 2 == 0:
            result.append(value)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("75. Even numbers from function:", get_even_numbers(numbers))
# Output: 75. Even numbers from function: [2, 4, 6, 8]


# ================================================================
# 26. COPYING LIST INSIDE A FUNCTION
# ================================================================

def add_without_changing_original(values):

    new_values = values.copy()
    new_values.append(100)

    return new_values


numbers = [10, 20, 30]

new_numbers = add_without_changing_original(numbers)

print("76. Original list:", numbers)
# Output: 76. Original list: [10, 20, 30]

print("77. New list:", new_numbers)
# Output: 77. New list: [10, 20, 30, 100]


# ================================================================
# 27. LIST OF STRINGS
# ================================================================

students = ["Amit", "Ravi", "Neha", "Priya"]

print("78. Number of students:", len(students))
# Output: 78. Number of students: 4

print("79. Alphabetically sorted:", sorted(students))
# Output: 79. Alphabetically sorted: ['Amit', 'Neha', 'Priya', 'Ravi']


# ================================================================
# 28. JOINING LIST ELEMENTS INTO A STRING
# ================================================================

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print("80. Joined string:", sentence)
# Output: 80. Joined string: Python is easy


# ================================================================
# 29. CONVERTING OTHER ITERABLES INTO LISTS
# ================================================================

# range can be converted into a list.

numbers = list(range(1, 6))

print("81. List from range:", numbers)
# Output: 81. List from range: [1, 2, 3, 4, 5]


# String can also be converted into a list.

letters = list("PYTHON")

print("82. List from string:", letters)
# Output: 82. List from string: ['P', 'Y', 'T', 'H', 'O', 'N']


# ================================================================
# 30. ZIP WITH LISTS
# ================================================================

names = ["Amit", "Ravi", "Neha"]
marks = [80, 90, 85]

student_data = list(zip(names, marks))

print("83. Zipped list:", student_data)
# Output: 83. Zipped list: [('Amit', 80), ('Ravi', 90), ('Neha', 85)]


# ================================================================
# 31. PRACTICAL LIST PROGRAM
# ================================================================

# Find total, average, highest and lowest marks.

marks = [78, 85, 92, 67, 88]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("84. Marks:", marks)
# Output: 84. Marks: [78, 85, 92, 67, 88]

print("85. Total:", total)
# Output: 85. Total: 410

print("86. Average:", average)
# Output: 86. Average: 82.0

print("87. Highest:", highest)
# Output: 87. Highest: 92

print("88. Lowest:", lowest)
# Output: 88. Lowest: 67


# ================================================================
# 32. FINAL SUMMARY
# ================================================================

print("\n89. List demonstration completed successfully.")
# Output: 89. List demonstration completed successfully.