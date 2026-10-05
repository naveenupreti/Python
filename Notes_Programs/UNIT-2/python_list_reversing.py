# single program that demonstrates all three ways of reversing a list—reverse(), reversed(), and slicing [::-1]
# ================================================================
#       THREE WAYS TO REVERSE A LIST IN PYTHON
# ================================================================
#
# 1. list.reverse()
# 2. reversed(list)
# 3. list[::-1]
#
# ================================================================


# ------------------------------------------------
# ORIGINAL LIST
# ------------------------------------------------

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
# Output: Original list: [10, 20, 30, 40, 50]


# ================================================================
# 1. reverse()
# ================================================================

print("\n========== 1. reverse() ==========")

# reverse() is a LIST METHOD.
# It reverses the ORIGINAL list.
# It works IN-PLACE.
# It returns None.

numbers = [10, 20, 30, 40, 50]
result = numbers.reverse()
print("Reversed list:", numbers)
# Output: Reversed list: [50, 40, 30, 20, 10]
print("Return value:", result)
# Output: Return value: None

# The original list has been changed.
print("Original list after reverse():", numbers)
# Output: Original list after reverse(): [50, 40, 30, 20, 10]

# ================================================================
# 2. reversed()
# ================================================================

print("\n========== 2. reversed() ==========")

# reversed() is a BUILT-IN FUNCTION.
# It does NOT modify the original list.
# It returns a REVERSE ITERATOR.

numbers = [10, 20, 30, 40, 50]
result = reversed(numbers)
print("Original list:", numbers)
# Output: Original list: [10, 20, 30, 40, 50]

print("Type returned by reversed():", type(result))
# Output: Type returned by reversed(): <class 'list_reverseiterator'>

# To get a list from the iterator,
# we can use list().

reversed_list = list(result)
print("Reversed list:", reversed_list)
# Output: Reversed list: [50, 40, 30, 20, 10]
print("Original list after reversed():", numbers)
# Output: Original list after reversed(): [10, 20, 30, 40, 50]


# IMPORTANT:
#
# reversed(numbers)
#       ↓
# reverse iterator
#
# list(reversed(numbers))
#       ↓
# new list


# ================================================================
# 3. SLICING [::-1]
# ================================================================

print("\n========== 3. SLICING [::-1] ==========")

# [::-1] is slicing.
#
# General syntax:
#
# list[start : stop : step]
#
# Here:
# start = omitted
# stop  = omitted
# step  = -1
#
# Therefore, Python moves through the list backwards.

numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Original list:", numbers)
# Output: Original list: [10, 20, 30, 40, 50]

print("Reversed list:", reversed_list)
# Output: Reversed list: [50, 40, 30, 20, 10]

# The original list is unchanged.
print("Original list after slicing:", numbers)
# Output: Original list after slicing: [10, 20, 30, 40, 50]


# ================================================================
# 4. COMPARING ALL THREE
# ================================================================

print("\n========== 4. COMPARISON ==========")

numbers = [1, 2, 3, 4, 5]
# Method 1: reverse()
a = numbers.copy()
a.reverse()

# Method 2: reversed()
b = list(reversed(numbers))

# Method 3: slicing
c = numbers[::-1]


print("Original:", numbers)
# Output: Original: [1, 2, 3, 4, 5]

print("Using reverse():", a)
# Output: Using reverse(): [5, 4, 3, 2, 1]

print("Using reversed():", b)
# Output: Using reversed(): [5, 4, 3, 2, 1]

print("Using slicing:", c)
# Output: Using slicing: [5, 4, 3, 2, 1]

# ================================================================
# 5. WHICH METHODS MODIFY THE ORIGINAL LIST?
# ================================================================

print("\n========== 5. ORIGINAL LIST ==========")

numbers = [10, 20, 30, 40]

# reverse()
a = numbers.copy()
a.reverse()

print("After reverse():")
print("a:", a)
# Output:
# a: [40, 30, 20, 10]

print("numbers:", numbers)
# Output: numbers: [10, 20, 30, 40]


# reversed()

b = list(reversed(numbers))

print("\nAfter reversed():")
print("b:", b)
# Output:
# b: [40, 30, 20, 10]

print("numbers:", numbers)
# Output: numbers: [10, 20, 30, 40]


# slicing

c = numbers[::-1]

print("\nAfter slicing:")
print("c:", c)
# Output:
# c: [40, 30, 20, 10]

print("numbers:", numbers)
# Output: numbers: [10, 20, 30, 40]


# ================================================================
# 6. reverse() RETURNS NONE
# ================================================================

print("\n========== 6. reverse() RETURNS NONE ==========")

numbers = [1, 2, 3]

result = numbers.reverse()

print("numbers:", numbers)
# Output: numbers: [3, 2, 1]

print("result:", result)
# Output: result: None


# Therefore, DON'T do this:
#
# numbers = numbers.reverse()
#
# because numbers would become None.


# ================================================================
# 7. reversed() RETURNS AN ITERATOR
# ================================================================

print("\n========== 7. reversed() RETURNS AN ITERATOR ==========")

numbers = [1, 2, 3, 4]
result = reversed(numbers)
print("Type:", type(result))
# Output: Type: <class 'list_reverseiterator'>


# We can use the iterator in a for loop.

print("Elements using reversed():")
for value in reversed(numbers):
    print(value)

# Output:
# Elements using reversed():
# 4
# 3
# 2
# 1

# ================================================================
# 8. SLICING CREATES A NEW LIST
# ================================================================

print("\n========== 8. SLICING CREATES A NEW LIST ==========")

numbers = [1, 2, 3, 4]

reversed_numbers = numbers[::-1]

print("numbers:", numbers)
# Output: numbers: [1, 2, 3, 4]

print("reversed_numbers:", reversed_numbers)
# Output: reversed_numbers: [4, 3, 2, 1]

print("Are they the same object?", numbers is reversed_numbers)
# Output: Are they the same object? False


# ================================================================
# 9. reversed() ALSO WORKS WITH STRINGS
# ================================================================

print("\n========== 9. reversed() WITH STRING ==========")

word = "PYTHON"
# reversed() returns an iterator.
result = reversed(word)
print("Reversed characters:")
for character in result:
    print(character)

# Output:
# Reversed characters:
# N
# O
# H
# T
# Y
# P


# We can convert it into a string using join().
word = "PYTHON"
reverse_word = "".join(reversed(word))
print("Reverse string:", reverse_word)
# Output: Reverse string: NOHTYP

# ================================================================
# 10. SLICING ALSO WORKS WITH STRINGS
# ================================================================
word = "PYTHON"
reverse_word = word[::-1]
print("Reverse string using slicing:", reverse_word)
# Output: Reverse string using slicing: NOHTYP

# ================================================================
# 11. IMPORTANT DIFFERENCE:
#    reverse() DOES NOT SORT
# ================================================================
print("\n========== 11. reverse() VS SORTING ==========")

numbers = [30, 10, 40, 20]
numbers.reverse()
print("After reverse():", numbers)
# Output: After reverse(): [20, 40, 10, 30]

# Notice:
# reverse() simply reverses the CURRENT order.
# It does NOT arrange numbers from largest to smallest.

numbers = [30, 10, 40, 20]
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)
# Output: After sort(reverse=True): [40, 30, 20, 10]


# ================================================================
# 12. FINAL SUMMARY
# ================================================================

print("\n========== FINAL SUMMARY ==========")

print("1. reverse()  -> modifies original list and returns None")
print("2. reversed() -> returns a reverse iterator")
print("3. [::-1]     -> creates a new reversed list")

# Output:
# 1. reverse()  -> modifies original list and returns None
# 2. reversed() -> returns a reverse iterator
# 3. [::-1]     -> creates a new reversed list