"""
====================================================================
PYTHON TOKENS AND DATA TYPES
====================================================================

This single program demonstrates:
1. Python tokens
2. Keywords
3. Identifiers
4. Literals
5. Operators
6. Delimiters / punctuators
7. Comments
8. Built-in data types
9. Type conversion
10. type() and id()
11. Mutable vs immutable objects

Everything is explained through comments and executable examples.
====================================================================
"""


# ==================================================================
# 1. COMMENTS
# ==================================================================
# Comments are ignored by Python.
# They are used to explain the program.

# This is a SINGLE-LINE COMMENT.

"""
This is a MULTI-LINE STRING.
It is often used like a multi-line comment,
although technically it is a string literal
when it is not used as a docstring.
"""


# ==================================================================
# 2. PYTHON TOKENS
# ==================================================================
"""
A TOKEN is the smallest meaningful unit of a Python program.

Major categories of tokens:

1. Keywords
2. Identifiers
3. Literals
4. Operators
5. Delimiters / punctuators

Example:

    age = 50 + 5

Tokens are:

    age     -> identifier
    =       -> assignment operator
    50      -> integer literal
    +       -> arithmetic operator
    5       -> integer literal
"""


# ==================================================================
# 3. KEYWORDS
# ==================================================================
"""
Keywords are reserved words having a predefined meaning in Python.

Examples:

False, None, True, and, as, assert, async, await,
break, case, class, continue, def, del, elif, else,
except, finally, for, from, global, if, import, in,
is, lambda, match, nonlocal, not, or, pass, raise,
return, try, while, with, yield

You cannot normally use a keyword as an identifier.

Example:

    if = 10       # INVALID

Python provides the 'keyword' module to see keywords.
"""

import keyword

print("\n--- KEYWORDS ---")

print(keyword.kwlist)

# Check whether a word is a keyword.
print(keyword.iskeyword("if"))       # True
print(keyword.iskeyword("student"))  # False


# ==================================================================
# 4. IDENTIFIERS
# ==================================================================
"""
An identifier is a name given to a program element.

Examples:

    age
    student_name
    marks
    calculate_total

Identifiers may contain:

    letters
    digits
    underscore (_)

Rules:

1. Cannot start with a digit.
2. Cannot contain spaces.
3. Cannot be a keyword.
4. Python is case-sensitive.

Valid:

    age
    age2
    _age
    student_name

Invalid:

    2age
    student-name
    student name
    class

"""

student_name = "Rahul"
age2 = 20
_marks = 85

print("\n--- IDENTIFIERS ---")

print(student_name)
print(age2)
print(_marks)

# Python is CASE-SENSITIVE.

name = "A"
Name = "B"

print(name)      # A
print(Name)      # B

# name and Name are two different identifiers.


# ==================================================================
# 5. LITERALS
# ==================================================================
"""
A literal is a fixed value written directly in the program.

Examples:

    100          -> integer literal
    3.14         -> float literal
    "Hello"      -> string literal
    True         -> Boolean literal
    None         -> None literal

Collection literals also exist:

    [1, 2, 3]       -> list
    (1, 2, 3)       -> tuple
    {1, 2, 3}       -> set
    {"a": 1}        -> dictionary
"""


# Integer literal
integer_value = 100

# Floating-point literal
float_value = 3.14

# String literal
string_value = "Python"

# Boolean literals
true_value = True
false_value = False

# None literal
none_value = None

print("\n--- LITERALS ---")

print(integer_value)
print(float_value)
print(string_value)
print(true_value)
print(false_value)
print(none_value)


# ==================================================================
# 6. NUMERIC DATA TYPES
# ==================================================================
"""
Python has three main built-in numeric types:

    int
    float
    complex
"""


# ---------------- INTEGER ----------------

age = 50

print("\n--- INTEGER ---")

print(age)
print(type(age))

# Python integers can be extremely large.

big_number = 123456789012345678901234567890

print(big_number)
print(type(big_number))


# Different integer representations

binary_number = 0b1010       # Binary = 10
octal_number = 0o12          # Octal = 10
decimal_number = 10          # Decimal = 10
hex_number = 0xA             # Hexadecimal = 10

print("\n--- INTEGER REPRESENTATIONS ---")

print(binary_number)
print(octal_number)
print(decimal_number)
print(hex_number)


# ---------------- FLOAT ----------------

price = 99.50

print("\n--- FLOAT ---")

print(price)
print(type(price))


# Scientific notation

scientific_number = 1.5e3

print(scientific_number)     # 1500.0
print(type(scientific_number))


# ---------------- COMPLEX ----------------

z = 3 + 4j

print("\n--- COMPLEX ---")

print(z)
print(type(z))

print(z.real)       # Real part
print(z.imag)       # Imaginary part


# ==================================================================
# 7. BOOLEAN DATA TYPE
# ==================================================================
"""
bool represents logical values:

    True
    False

IMPORTANT:

bool is actually a subclass of int.

Therefore:

    True  == 1
    False == 0
"""

print("\n--- BOOLEAN ---")

print(True)
print(False)

print(type(True))
print(type(False))

print(True == 1)     # True
print(False == 0)   # True

print(isinstance(True, int))    # True


# ==================================================================
# 8. STRING DATA TYPE
# ==================================================================
"""
str represents text.

Strings can be created using:

    'single quotes'
    "double quotes"
    '''triple quotes'''
    \"\"\"triple double quotes\"\"\"

Strings are IMMUTABLE.

"""

name = "Python"

print("\n--- STRING ---")

print(name)
print(type(name))

# Indexing starts from 0.

print(name[0])      # P
print(name[1])      # y

# Negative indexing starts from -1.

print(name[-1])     # n
print(name[-2])     # o

# Slicing

print(name[0:3])    # Pyt
print(name[:3])     # Pyt
print(name[3:])     # hon
print(name[::-1])   # nohtyP


# String concatenation

first = "Hello"
second = "Python"

message = first + " " + second

print(message)


# String repetition

print("Hi " * 3)


# ==================================================================
# 9. ESCAPE SEQUENCES IN STRINGS
# ==================================================================

print("\n--- ESCAPE SEQUENCES ---")

print("Hello\nPython")       # New line
print("Hello\tPython")       # Tab
print("He said \"Hello\"")   # Double quote inside string
print('It\'s Python')        # Single quote inside string

'''
Python does not have a separate char (character) data type.

In Python, a single character is simply a string (str) of length 1.

ch = 'A'
print(ch)          # A
print(type(ch))    # <class 'str'>
print(len(ch))     # 1

a = 'A'
b = "A"
print(type(a))    # <class 'str'>
print(type(b))    # <class 'str'>

print(a == b)     # True

text = "Python"

print(text[0])         # P
print(type(text[0]))   # <class 'str'>
print(len(text[0]))    # 1

If you need the numeric Unicode value of a character, Python provides ord():
ch = 'A'
print(ord(ch))         # 65

And the reverse is chr():
print(chr(65))         # A

'''
# ==================================================================
# 10. LIST DATA TYPE
# ==================================================================
"""
list is:

    ordered
    mutable
    allows duplicate values
    allows different data types

Example:

    [10, 20, 30]
"""

numbers = [10, 20, 30, 20]

print("\n--- LIST ---")

print(numbers)
print(type(numbers))

# Lists are mutable.

numbers[0] = 100

print(numbers)

# Adding an item

numbers.append(40)

print(numbers)


# A list can contain different data types.

mixed_list = [
    10,
    3.14,
    "Python",
    True,
    None,
    [1, 2]
]

print(mixed_list)


# ==================================================================
# 11. TUPLE DATA TYPE
# ==================================================================
"""
tuple is:

    ordered
    immutable
    allows duplicates
    can contain different data types
"""

coordinates = (10, 20, 30)

print("\n--- TUPLE ---")

print(coordinates)
print(type(coordinates))

print(coordinates[0])

# The following would produce an error:

# coordinates[0] = 100


# IMPORTANT TRICK:
# Parentheses are NOT what make a tuple.
# The comma makes a tuple.

a = (10)

b = (10,)

print(type(a))      # int
print(type(b))      # tuple


# Empty tuple

empty_tuple = ()

print(type(empty_tuple))


# ==================================================================
# 12. SET DATA TYPE
# ==================================================================
"""
set is:

    unordered
    mutable
    does not allow duplicate elements
    generally used for unique values

"""

numbers_set = {10, 20, 30, 20, 10}

print("\n--- SET ---")

print(numbers_set)
print(type(numbers_set))

# Duplicates disappear.

# Add an element

numbers_set.add(40)

print(numbers_set)


# IMPORTANT TRICK:
#
# {} does NOT create an empty set.
# {} creates an empty dictionary.

empty_dictionary = {}
empty_set = set()

print(type(empty_dictionary))  # dict
print(type(empty_set))         # set


# ==================================================================
# 13. FROZENSET DATA TYPE
# ==================================================================
"""
frozenset is an IMMUTABLE version of a set.

It:

    does not allow duplicates
    is unordered
    cannot be modified after creation
"""

fs = frozenset([10, 20, 30, 20])

print("\n--- FROZENSET ---")

print(fs)
print(type(fs))

# This would be invalid:

# fs.add(40)


# ==================================================================
# 14. DICTIONARY DATA TYPE
# ==================================================================
"""
dict stores data in KEY : VALUE pairs.

Example:

    {"name": "Rahul", "age": 20}

Dictionary:

    is mutable
    stores key-value pairs
    keys must be hashable
"""

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

print("\n--- DICTIONARY ---")

print(student)
print(type(student))

print(student["name"])
print(student["age"])

# Dictionary is mutable.

student["age"] = 21

print(student)


# Add a new key-value pair

student["city"] = "Lucknow"

print(student)


# ==================================================================
# 15. NONE DATA TYPE
# ==================================================================
"""
None represents the absence of a value.

Its type is NoneType.

None is NOT:

    0
    ""
    False

"""

result = None

print("\n--- NONE ---")

print(result)
print(type(result))

print(result is None)      # True


# ==================================================================
# 16. RANGE DATA TYPE
# ==================================================================
"""
range represents a sequence of numbers.

Syntax:

    range(start, stop, step)

The stop value is EXCLUDED.
"""

r = range(1, 6)

print("\n--- RANGE ---")

print(r)
print(type(r))

print(list(r))
# Output:
# [1, 2, 3, 4, 5]


# Step

print(list(range(2, 11, 2)))
# [2, 4, 6, 8, 10]


# Reverse

print(list(range(5, 0, -1)))
# [5, 4, 3, 2, 1]


# ==================================================================
# 17. BYTES DATA TYPE
# ==================================================================
"""
bytes represents immutable binary data.

Each element is an integer between 0 and 255.
"""

data = b"ABC"

print("\n--- BYTES ---")

print(data)
print(type(data))

print(data[0])     # 65
print(data[1])     # 66
print(data[2])     # 67


# ==================================================================
# 18. BYTEARRAY DATA TYPE
# ==================================================================
"""
bytearray is similar to bytes,
but it is MUTABLE.
"""

data = bytearray(b"ABC")

print("\n--- BYTEARRAY ---")

print(data)
print(type(data))

data[0] = 90

print(data)
# 90 is ASCII value of Z


# ==================================================================
# 19. MEMORYVIEW DATA TYPE
# ==================================================================
"""
memoryview provides a view of binary data
without making a copy of the original data.
"""

data = bytearray(b"ABC")

view = memoryview(data)

print("\n--- MEMORYVIEW ---")

print(view)
print(type(view))

print(view[0])       # 65


# ==================================================================
# 20. OPERATORS
# ==================================================================
"""
Operators are symbols/keywords used to perform operations.

Major categories:

1. Arithmetic
2. Comparison
3. Assignment
4. Logical
5. Bitwise
6. Membership
7. Identity
"""


# ---------------- ARITHMETIC ----------------

a = 10
b = 3

print("\n--- ARITHMETIC OPERATORS ---")

print(a + b)      # Addition
print(a - b)      # Subtraction
print(a * b)      # Multiplication
print(a / b)      # True division
print(a // b)     # Floor division
print(a % b)      # Modulus
print(a ** b)     # Exponentiation


# ---------------- COMPARISON ----------------

print("\n--- COMPARISON OPERATORS ---")

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# ---------------- ASSIGNMENT ----------------

print("\n--- ASSIGNMENT OPERATORS ---")

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x //= 2
print(x)


# ---------------- LOGICAL ----------------

print("\n--- LOGICAL OPERATORS ---")

age = 20

print(age >= 18 and age <= 60)
print(age < 18 or age > 60)
print(not(age >= 18))


# ---------------- MEMBERSHIP ----------------

print("\n--- MEMBERSHIP OPERATORS ---")

language = "Python"

print("P" in language)
print("z" in language)
print("z" not in language)


# ---------------- IDENTITY ----------------

print("\n--- IDENTITY OPERATORS ---")

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x == y)     # Same contents
print(x is y)     # Same object

print(x == z)     # Same contents
print(x is z)     # Different objects


# ==================================================================
# 21. DELIMITERS / PUNCTUATORS
# ==================================================================
"""
Common Python delimiters include:

    ( )     function calls, tuples, grouping
    [ ]     lists, indexing, slicing
    { }     dictionaries and sets
    :       blocks, dictionary pairs, slicing
    ,       separates elements
    .       attribute access
    ;       separates statements (rarely needed)
    @       decorators
"""

my_list = [10, 20, 30]

my_dict = {
    "name": "Rahul",
    "age": 20
}

print("\n--- DELIMITERS ---")

print(my_list)
print(my_dict)

print(my_dict["name"])
print(my_dict.keys())


# ==================================================================
# 22. TYPE CHECKING USING type()
# ==================================================================
"""
type() tells us the type/class of an object.
"""

values = [
    10,
    3.14,
    2 + 3j,
    True,
    "Python",
    [1, 2],
    (1, 2),
    {1, 2},
    {"a": 1},
    None,
    range(5),
    b"ABC",
    bytearray(b"ABC"),
    frozenset([1, 2])
]

print("\n--- type() ---")

for value in values:
    print(value, "->", type(value))


# ==================================================================
# 23. isinstance()
# ==================================================================
"""
isinstance() checks whether an object belongs to a particular type.

Syntax:

    isinstance(object, type)
"""

number = 100

print("\n--- isinstance() ---")

print(isinstance(number, int))       # True
print(isinstance(number, float))     # False
print(isinstance(number, object))    # True


# ==================================================================
# 24. id()
# ==================================================================
"""
id() returns the identity of an object.

Every object has an identity during its lifetime.

IMPORTANT:

    id() is NOT the same thing as the value of an object.

Two variables can refer to the SAME object.
"""

a = [1, 2, 3]
b = a

print("\n--- id() ---")

print(id(a))
print(id(b))

print(a is b)      # True


# c contains the same values,
# but it is a different list object.

c = [1, 2, 3]

print(id(c))

print(a == c)      # True
print(a is c)      # False


# ==================================================================
# 25. MUTABLE VS IMMUTABLE
# ==================================================================
"""
IMMUTABLE objects cannot be changed after creation.

Examples:

    int
    float
    complex
    bool
    str
    tuple
    frozenset
    bytes

MUTABLE objects can be changed.

Examples:

    list
    set
    dict
    bytearray
"""

# Mutable example

a = [10, 20]

old_id = id(a)

a.append(30)

new_id = id(a)

print("\n--- MUTABILITY ---")

print(a)
print(old_id == new_id)
# True: the same list object was modified.


# Immutable example

x = 10

old_id = id(x)

x = x + 1

new_id = id(x)

print(x)
print(old_id == new_id)

# Usually False because a new integer object is created.


# ==================================================================
# 26. TYPE CONVERSION
# ==================================================================
"""
Python allows conversion between compatible types.

Examples:

    int()
    float()
    str()
    bool()
    list()
    tuple()
    set()
"""

print("\n--- TYPE CONVERSION ---")

print(int("100"))
print(float("3.14"))
print(str(100))
print(bool(1))

print(list("ABC"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))


# ==================================================================
# 27. TRICKY BOOLEAN CONVERSIONS
# ==================================================================
"""
In Python, many objects can be interpreted as True or False.

Generally FALSE values include:

    False
    None
    0
    0.0
    ""
    []
    ()
    {}
    set()

Most other objects are TRUE.
"""

print("\n--- TRUTH VALUE ---")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

print(bool(1))
print(bool("Python"))
print(bool([1, 2]))


# ==================================================================
# 28. EVERYTHING IS AN OBJECT
# ==================================================================
"""
One of Python's most important concepts:

    EVERYTHING IS AN OBJECT.

Numbers, strings, lists, functions, classes, etc.
are objects.

Objects have:

    identity
    type
    value/state
"""

number = 10
text = "Python"
items = [1, 2, 3]

print("\n--- EVERYTHING IS AN OBJECT ---")

print(type(number), id(number))
print(type(text), id(text))
print(type(items), id(items))


# ==================================================================
# 29. FINAL SUMMARY
# ==================================================================
"""
====================================================================
PYTHON TOKEN SUMMARY
====================================================================

TOKEN
 |
 +-- Keywords
 |      if, else, for, while, class, def, return...
 |
 +-- Identifiers
 |      age, name, student_marks...
 |
 +-- Literals
 |      10, 3.14, "Python", True, None...
 |
 +-- Operators
 |      +, -, *, /, ==, >, and, or, is, in...
 |
 +-- Delimiters
        (), [], {}, :, ,, ., @ ...

====================================================================
PYTHON BUILT-IN DATA TYPES
====================================================================

Numeric:
    int
    float
    complex

Boolean:
    bool

Text:
    str

Sequence:
    list
    tuple
    range

Set:
    set
    frozenset

Mapping:
    dict

Binary:
    bytes
    bytearray
    memoryview

Special:
    NoneType

====================================================================
MUTABLE
====================================================================

list
set
dict
bytearray

====================================================================
IMMUTABLE
====================================================================

int
float
complex
bool
str
tuple
range
frozenset
bytes
NoneType

====================================================================
MOST IMPORTANT FUNCTIONS
====================================================================

type()          -> tells the type of an object
id()            -> tells the identity of an object
isinstance()    -> checks an object's type
bool()          -> converts/checks truth value

====================================================================
"""

print("\n==============================================")
print("PROGRAM COMPLETED SUCCESSFULLY")
print("==============================================")