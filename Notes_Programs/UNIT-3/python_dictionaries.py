"""
===============================================================
                 PYTHON DICTIONARY BMC301: Python Programming
===============================================================

SYLLABUS TOPICS COVERED
-----------------------
1. Introduction to dictionaries
2. Accessing values in dictionaries
3. Working with dictionaries
4. Properties of dictionaries
5. Functions / methods used with dictionaries

IMPORTANT TRICKY CONCEPTS ALSO COVERED
--------------------------------------
* Key-value pairs
* Unique keys
* Duplicate keys
* Different types of keys
* Hashable vs mutable keys
* Insertion order
* Mutable nature of dictionaries
* Accessing using [] vs get()
* Adding and modifying elements
* update()
* Removing elements
* pop(), popitem(), del, clear()
* keys(), values(), items()
* Dictionary iteration
* Membership testing
* len(), type(), dict()
* Nested dictionaries
* Dictionary comprehension
* setdefault()
* fromkeys()
* Aliasing
* copy()
* Equality comparison
* Missing-key problem
* Mutable values

HOW TO STUDY THIS FILE
----------------------
Run the complete file from top to bottom. Each section prints a heading,
then demonstrates a concept. The expected output and explanation are placed
immediately after the relevant code block. Some dictionary displays may
vary in formatting slightly, but the values and ordering shown are correct
for modern Python (3.7+).
"""

# ===============================================================
# 1. INTRODUCTION TO DICTIONARIES
# ===============================================================

print("\n1. INTRODUCTION TO DICTIONARIES")
print("-" * 50)

# A dictionary stores data in KEY : VALUE pairs.
student = {
    "name": "Naveen",
    "age": 25,
    "course": "MCA",
    "marks": 85
}

print(student)

"""
OUTPUT:
{'name': 'Naveen', 'age': 25, 'course': 'MCA', 'marks': 85}

A dictionary is written using curly brackets {}.

General syntax:

    dictionary_name = {
        key1: value1,
        key2: value2,
        ...
    }

Each item consists of:

    key : value

Example:
    "name" : "Naveen"

Here:
    "name"   -> key
    "Naveen" -> value
"""


# ===============================================================
# 2. CREATING AN EMPTY DICTIONARY
# ===============================================================

print("\n2. EMPTY DICTIONARY")
print("-" * 50)

d1 = {}
d2 = dict()

print(d1)
print(d2)
print(type(d1))
print(type(d2))

"""
OUTPUT:
{}
{}
<class 'dict'>
<class 'dict'>

Both {} and dict() create an empty dictionary.

TRICK:
    {} creates an empty dictionary, NOT an empty set.

An empty set is created using:

    set()

Example:

    {}       -> dictionary
    set()    -> set
"""


# ===============================================================
# 3. ACCESSING VALUES IN A DICTIONARY
# ===============================================================

print("\n3. ACCESSING VALUES")
print("-" * 50)

student = {
    "name": "Naveen",
    "age": 25,
    "marks": 85
}

print(student["name"])
print(student["marks"])

"""
OUTPUT:
Naveen
85

Values are accessed using their keys:

    dictionary[key]

NOT by index.

Unlike a list:

    list[0]

a dictionary uses:

    dictionary["name"]

"""


# ===============================================================
# 4. [] VS get()  -- VERY IMPORTANT TRICK
# ===============================================================

print("\n4. [] VS get()")
print("-" * 50)

print(student["name"])

print(student.get("name"))

print(student.get("city"))

"""
OUTPUT:
Naveen
Naveen
None

IMPORTANT:

student["city"]

will generate:

    KeyError

because "city" does not exist.

But:

student.get("city")

returns:

    None

without generating an error.

Therefore:

    []     -> raises KeyError if key doesn't exist
    get()  -> returns None (or a default value)

We can also provide our own default value:

    student.get("city", "Not Available")
"""

print(student.get("city", "Not Available"))

"""
OUTPUT:
Not Available
"""


# ===============================================================
# 5. ADDING A NEW KEY-VALUE PAIR
# ===============================================================

print("\n5. ADDING DATA")
print("-" * 50)

student["city"] = "Lucknow"

print(student)

"""
OUTPUT:
{'name': 'Naveen', 'age': 25, 'marks': 85, 'city': 'Lucknow'}

If the key does not already exist, assignment creates a
new key-value pair.

"""
# ===============================================================
# 6. MODIFYING AN EXISTING VALUE
# ===============================================================

print("\n6. MODIFYING DATA")
print("-" * 50)

student["marks"] = 90
student["age"] = 52

print(student)

"""
OUTPUT:
{'name': 'Naveen', 'age': 52, 'marks': 90, 'city': 'Lucknow'}

TRICK:

The same syntax is used for:

    Adding:
        dictionary[new_key] = value

    Modifying:
        dictionary[existing_key] = new_value

Python determines whether to add or modify by checking
whether the key already exists.
"""


# ===============================================================
# 7. DICTIONARY KEYS MUST BE UNIQUE
# ===============================================================

print("\n7. DUPLICATE KEYS")
print("-" * 50)

duplicate = {
    "name": "A",
    "name": "B"
}

print(duplicate)

"""
OUTPUT:
{'name': 'B'}

TRICKY CONCEPT:

Dictionary keys must be unique.

If the same key occurs more than once, the later value
replaces the earlier value.

Therefore:

    "name": "A"
    "name": "B"

results in:

    "name": "B"
"""


# ===============================================================
# 8. TYPES OF KEYS
# ===============================================================

print("\n8. DICTIONARY KEY TYPES")
print("-" * 50)

mixed_keys = {
    "name": "Naveen",
    101: "Student ID",
    3.14: "Pi",
    True: "Boolean key",
    (1, 2): "Tuple key"
}

print(mixed_keys)

"""
Dictionary keys can be of different hashable types.

Examples:
    string
    integer
    float
    boolean
    tuple

IMPORTANT TRICK:

Keys must be HASHABLE. Hashable means that a dictionary key must be an object
whose hash value can be calculated and remains stable while it is used as a key.
A hash is an integer calculated by Python using the built-in hash() function.
Python uses it to find dictionary keys efficiently.

Common hashable objects:
    int
    float
    str
    tuple (if its elements are hashable)
    bool

Lists, dictionaries and sets cannot normally be dictionary keys
because they are mutable and unhashable.

For example, this is INVALID:

    d = {[1, 2]: "value"}

It raises:

    TypeError: unhashable type: 'list'
"""


# ===============================================================
# 9. VALUES CAN BE OF ANY TYPE
# ===============================================================

print("\n9. DICTIONARY VALUES")
print("-" * 50)

data = {
    "name": "Naveen",
    "age": 25,
    "marks": [80, 85, 90],
    "address": {"city": "Lucknow", "state": "UP"}
}

print(data)

"""
Values are much less restricted than keys.

A value can be:
    string
    integer
    float
    list
    tuple
    set
    another dictionary
    even a function/object

This is why dictionaries are extremely useful for structured data.
"""


# ===============================================================
# 10. DICTIONARY PROPERTIES
# ===============================================================

print("\n10. PROPERTIES OF DICTIONARIES")
print("-" * 50)

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(d)

"""
IMPORTANT PROPERTIES:

1. Dictionaries are MUTABLE.
   Their contents can be changed after creation.

2. Keys are UNIQUE.

3. Keys must be HASHABLE.

4. Values can be duplicated.

5. Dictionaries preserve INSERTION ORDER in modern Python
   (Python 3.7+ as a language guarantee).

6. Dictionaries are accessed using KEYS, not numeric indexes.

7. A dictionary can contain another dictionary as a value.

8. A dictionary can contain mutable values such as lists.
"""

d["a"] = 100
print(d)

"""
OUTPUT:
{'a': 100, 'b': 20, 'c': 30}
"""


# ===============================================================
# 11. DICTIONARY LENGTH
# ===============================================================

print("\n11. len()")
print("-" * 50)

print(len(d))

"""
OUTPUT:
3

len(dictionary)

returns the number of KEY-VALUE PAIRS.

It does NOT count the number of individual values inside
nested structures.
"""


# ===============================================================
# 12. type() AND dict()
# ===============================================================

print("\n12. type() AND dict()")
print("-" * 50)

print(type(d))

new_dict = dict(name="Naveen", age=25)
print(new_dict)

"""
OUTPUT:
<class 'dict'>
{'name': 'Naveen', 'age': 25}

dict() can be used to create dictionaries.
"""


# ===============================================================
# 13. keys(), values(), items()
# ===============================================================

print("\n13. keys(), values(), items()")
print("-" * 50)

student = {
    "name": "Naveen",
    "age": 25,
    "marks": 90
}

print(student.keys())
print(student.values())
print(student.items())

"""
OUTPUT (conceptually):
dict_keys(['name', 'age', 'marks'])
dict_values(['Naveen', 25, 90])
dict_items([
    ('name', 'Naveen'),
    ('age', 25),
    ('marks', 90)
])

keys()   -> returns dictionary keys
values() -> returns dictionary values
items()  -> returns key-value pairs

IMPORTANT:

items() returns pairs in the form:

    (key, value)

which is a tuple.
"""


# ===============================================================
# 14. ITERATING THROUGH A DICTIONARY
# ===============================================================

print("\n14. ITERATING THROUGH A DICTIONARY")
print("-" * 50)

for key in student:
    print(key)

"""
OUTPUT:
name
age
marks

TRICK:

When we directly iterate over a dictionary:

    for x in dictionary:

x represents the KEYS, not values.
"""


print("\nKeys and values:")

for key, value in student.items():
    print(key, "=", value)

"""
OUTPUT:
name = Naveen
age = 25
marks = 90
"""


# ===============================================================
# 15. MEMBERSHIP OPERATOR
# ===============================================================

print("\n15. MEMBERSHIP TESTING")
print("-" * 50)

print("name" in student)
print("Naveen" in student)

"""
OUTPUT:
True
False

IMPORTANT TRICK:

    key in dictionary

checks KEYS, not values.

Therefore:

    "name" in student
        -> True

    "Naveen" in student
        -> False

To search values:

    "Naveen" in student.values()
"""


print("Naveen" in student.values())

"""
OUTPUT:
True
"""


# ===============================================================
# 16. update()
# ===============================================================

print("\n16. update()")
print("-" * 50)

student.update({
    "age": 26,
    "city": "Lucknow"
})

print(student)

"""
OUTPUT:
{'name': 'Naveen', 'age': 26, 'marks': 90, 'city': 'Lucknow'}

update() can:

1. Add new key-value pairs.
2. Modify existing key-value pairs.

If a key already exists -> its value is replaced.
If a key does not exist -> it is added.
"""


# ===============================================================
# 17. REMOVING DATA - pop()
# ===============================================================

print("\n17. pop()")
print("-" * 50)

removed_value = student.pop("city")

print("Removed:", removed_value)
print(student)

"""
pop(key)

removes the specified key-value pair and RETURNS the value
that was removed.

Therefore:

    x = d.pop("key")

stores the removed value in x.

TRICK:

    d.pop("missing_key")

causes KeyError unless a default value is supplied.
"""

print(student.pop("country", "Not found"))

"""
OUTPUT:
Not found

The second argument is a default value used if the key
does not exist.
"""


# ===============================================================
# 18. popitem()
# ===============================================================

print("\n18. popitem()")
print("-" * 50)

last_item = student.popitem()

print("Removed:", last_item)
print(student)

"""
popitem()

removes and returns the LAST inserted key-value pair
in modern Python.

The returned object is a tuple:

    (key, value)

TRICK:

Older Python versions did not guarantee the same insertion-order
semantics. For current Python, think of popitem() as removing
the last inserted item.
"""


# ===============================================================
# 19. del
# ===============================================================

print("\n19. del")
print("-" * 50)

d = {
    "a": 10,
    "b": 20,
    "c": 30
}

del d["b"]

print(d)

"""
OUTPUT:
{'a': 10, 'c': 30}

del removes the specified key-value pair.

Unlike pop():

    del d["b"]

does NOT return the removed value.

If the key doesn't exist:

    del d["x"]

raises KeyError.
"""


# ===============================================================
# 20. clear()
# ===============================================================

print("\n20. clear()")
print("-" * 50)

d.clear()

print(d)

"""
OUTPUT:
{}

clear() removes ALL key-value pairs.

Important difference:

    d.clear()

keeps the dictionary object but empties it.

"""


# ===============================================================
# 21. setdefault()
# ===============================================================

print("\n21. setdefault()")
print("-" * 50)

student = {
    "name": "Naveen",
    "age": 25
}

result = student.setdefault("city", "Lucknow")

print(result)
print(student)

"""
OUTPUT:
Lucknow
{'name': 'Naveen', 'age': 25, 'city': 'Lucknow'}

setdefault(key, default):

If key exists:
    returns its existing value
    does NOT replace it.

If key does not exist:
    inserts the key with default value
    and returns the default value.

This is a very useful dictionary method.
"""


result = student.setdefault("age", 100)

print(result)
print(student)

"""
OUTPUT:
25
{'name': 'Naveen', 'age': 25, 'city': 'Lucknow'}

Notice that age did NOT become 100.

Because "age" already existed.
"""


# ===============================================================
# 22. fromkeys()
# ===============================================================

print("\n22. fromkeys()")
print("-" * 50)

keys = ["name", "age", "city"]

new_student = dict.fromkeys(keys, "Unknown")

print(new_student)

"""
OUTPUT:
{'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

fromkeys() creates a dictionary from a sequence of keys.

Syntax:

    dict.fromkeys(iterable, value)

The value is optional.

Without specifying a value:

    dict.fromkeys(["a", "b"])

produces:

    {'a': None, 'b': None}
"""


# ===============================================================
# 23. NESTED DICTIONARY
# ===============================================================

print("\n23. NESTED DICTIONARY")
print("-" * 50)

college = {
    "student": {
        "name": "Naveen",
        "age": 25
    },
    "course": {
        "name": "MCA",
        "semester": 3
    }
}

print(college)

print(college["student"]["name"])
print(college["course"]["semester"])

"""
OUTPUT:
Naveen
3

A dictionary can contain another dictionary.

Accessing nested data requires multiple keys:

    college["student"]["name"]

First:
    college["student"]

Then:
    ["name"]
"""


# ===============================================================
# 24. DICTIONARY WITH LIST AS VALUE
# ===============================================================

print("\n24. MUTABLE VALUE INSIDE DICTIONARY")
print("-" * 50)

student = {
    "name": "Naveen",
    "marks": [80, 85, 90]
}

student["marks"].append(95)

print(student)

"""
OUTPUT:
{'name': 'Naveen', 'marks': [80, 85, 90, 95]}

A dictionary itself is mutable, and its values can also be
mutable objects such as lists.
"""


# ===============================================================
# 25. DICTIONARY COMPREHENSION
# ===============================================================

print("\n25. DICTIONARY COMPREHENSION")
print("-" * 50)

squares = {x: x * x for x in range(1, 6)}

print(squares)

"""
OUTPUT:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

General syntax:

    {key_expression: value_expression for item in iterable}

Dictionary comprehension is a concise way to create dictionaries.

Although not explicitly named in the syllabus, it is an
important practical dictionary concept.
"""


# ===============================================================
# 26. CONDITIONAL DICTIONARY COMPREHENSION
# ===============================================================

print("\n26. CONDITIONAL DICTIONARY COMPREHENSION")
print("-" * 50)

even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)

"""
OUTPUT:
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
"""


# ===============================================================
# 27. DICTIONARY ALIASING - VERY IMPORTANT TRICK
# ===============================================================

print("\n27. ALIASING")
print("-" * 50)

original = {
    "a": 10,
    "b": 20
}

alias = original

alias["a"] = 100

print(original)
print(alias)

"""
OUTPUT:
{'a': 100, 'b': 20}
{'a': 100, 'b': 20}

TRICKY CONCEPT:

    alias = original

does NOT create a new dictionary.

Both variables refer to the SAME dictionary object.

Therefore changing alias also changes original.
"""


# ===============================================================
# 28. copy() - SHALLOW COPY
# ===============================================================

print("\n28. copy()")
print("-" * 50)

original = {
    "a": 10,
    "b": 20
}

copied = original.copy()

copied["a"] = 100

print("Original:", original)
print("Copied:", copied)

"""
OUTPUT:
Original: {'a': 10, 'b': 20}
Copied: {'a': 100, 'b': 20}

copy() creates a separate dictionary.

Therefore changing a top-level value in copied does not
change original.

BUT copy() is a SHALLOW COPY.

This distinction becomes important when the dictionary
contains mutable nested objects such as lists.
"""


# ===============================================================
# 29. SHALLOW COPY TRICK
# ===============================================================

print("\n29. SHALLOW COPY WITH NESTED LIST")
print("-" * 50)

original = {
    "numbers": [1, 2, 3]
}

copied = original.copy()

copied["numbers"].append(4)

print("Original:", original)
print("Copied:", copied)

"""
OUTPUT:
Original: {'numbers': [1, 2, 3, 4]}
Copied: {'numbers': [1, 2, 3, 4]}

WHY?

copy() creates a new outer dictionary, but the nested list
is still the SAME list object.

This is called a SHALLOW COPY.

For a completely independent nested copy, Python provides
copy.deepcopy(), but that is beyond the core dictionary
syllabus.
"""


# ===============================================================
# 30. DICTIONARY COMPARISON
# ===============================================================

print("\n30. DICTIONARY COMPARISON")
print("-" * 50)

d1 = {"a": 10, "b": 20}
d2 = {"b": 20, "a": 10}
d3 = {"a": 10, "b": 30}

print(d1 == d2)
print(d1 == d3)

"""
OUTPUT:
True
False

Dictionary equality is based on the key-value contents.

The insertion order does NOT make these two dictionaries
unequal:

    {"a": 10, "b": 20}
    {"b": 20, "a": 10}

They contain the same key-value pairs.
"""


# ===============================================================
# 31. COPYING USING dict()
# ===============================================================

print("\n31. COPYING USING dict()")
print("-" * 50)

original = {"a": 1, "b": 2}

copy2 = dict(original)

copy2["a"] = 100

print(original)
print(copy2)

"""
OUTPUT:
{'a': 1, 'b': 2}
{'a': 100, 'b': 2}

dict(original) creates a new outer dictionary.

Like copy(), it is a shallow copy.
"""


# ===============================================================
# 32. PRACTICAL EXAMPLE - STUDENT RECORD
# ===============================================================

print("\n32. PRACTICAL STUDENT RECORD")
print("-" * 50)

student = {
    "roll_no": 101,
    "name": "Naveen",
    "subjects": {
        "Python": 85,
        "C": 90,
        "DBMS": 88
    }
}

print("Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Python Marks:", student["subjects"]["Python"])

average = sum(student["subjects"].values()) / len(student["subjects"])

print("Average:", average)

"""
OUTPUT:
Name: Naveen
Roll No: 101
Python Marks: 85
Average: 87.66666666666667

This example demonstrates how dictionaries are commonly used
to represent structured real-world data.
"""


# ===============================================================
# 33. COMMON MISTAKES / TRICKY EXAM QUESTIONS
# ===============================================================

print("\n33. IMPORTANT EXAM TRICKS")
print("-" * 50)

"""
1. DICTIONARY HAS NO NUMERIC INDEXING

    d = {"a": 10, "b": 20}

    d[0]

does NOT mean the first element.

It raises KeyError unless 0 itself is a key.

---------------------------------------------------------------

2. "in" CHECKS KEYS

    "a" in d

checks whether "a" is a KEY.

---------------------------------------------------------------

3. DUPLICATE KEYS ARE NOT STORED

    {"a": 10, "a": 20}

becomes:

    {"a": 20}

---------------------------------------------------------------

4. [] AND get() ARE DIFFERENT

    d["x"]
        -> KeyError if x doesn't exist

    d.get("x")
        -> None if x doesn't exist

---------------------------------------------------------------

5. KEYS MUST BE HASHABLE

    d = {[1, 2]: "hello"}

is invalid because list is mutable/unhashable.

---------------------------------------------------------------

6. DICTIONARY IS MUTABLE

    d["a"] = 100

is valid.

---------------------------------------------------------------

7. DICTIONARY KEYS ARE UNIQUE BUT VALUES DON'T HAVE TO BE

    {"a": 10, "b": 10}

is perfectly valid.

---------------------------------------------------------------

8. ITERATING DIRECTLY GIVES KEYS

    for x in d:
        print(x)

prints keys.

---------------------------------------------------------------

9. items() GIVES KEY-VALUE PAIRS

    for k, v in d.items():
        print(k, v)

---------------------------------------------------------------

10. pop() RETURNS THE REMOVED VALUE

    x = d.pop("a")

---------------------------------------------------------------

11. del DOES NOT RETURN THE REMOVED VALUE

    del d["a"]

---------------------------------------------------------------

12. popitem() RETURNS A (KEY, VALUE) TUPLE

---------------------------------------------------------------

13. update() CAN ADD AND MODIFY

---------------------------------------------------------------

14. setdefault() DOES NOT OVERWRITE AN EXISTING KEY

---------------------------------------------------------------

15. copy() IS A SHALLOW COPY

Nested mutable objects can still be shared.

---------------------------------------------------------------

16. DICTIONARIES PRESERVE INSERTION ORDER IN MODERN PYTHON

But order should not be confused with numeric indexing.
"""


# ===============================================================
# 34. FINAL SUMMARY
# ===============================================================

print("\n34. DICTIONARY SUMMARY")
print("-" * 50)

summary = {
    "Create": "{} or dict()",
    "Access": "d[key] or d.get(key)",
    "Add": "d[key] = value",
    "Modify": "d[key] = new_value",
    "Remove": "pop(), popitem(), del",
    "All remove": "clear()",
    "Keys": "keys()",
    "Values": "values()",
    "Pairs": "items()",
    "Update": "update()",
    "Default insertion": "setdefault()",
    "Create from keys": "fromkeys()",
    "Length": "len()",
    "Type": "type()"
}

for operation, meaning in summary.items():
    print(f"{operation:20} -> {meaning}")
'''
# items() gives each key-value pair as a tuple.
# The loop unpacks each tuple into operation and meaning.
for operation, meaning in summary.items():

    # :20 reserves at least 20 character positions
    # for operation and left-aligns it.
    # The arrow separates the operation from its meaning.
    print(f"{operation:20} -> {meaning}")

'''

"""
===============================================================
                 QUICK REVISION
===============================================================

Dictionary
    |
    +-- key : value
    |
    +-- Keys
    |     +-- unique
    |     +-- hashable
    |
    +-- Values
    |     +-- can be duplicate
    |     +-- can be mutable
    |
    +-- Access
    |     +-- d[key]
    |     +-- d.get(key)
    |
    +-- Add / Modify
    |     +-- d[key] = value
    |     +-- update()
    |
    +-- Remove
    |     +-- pop()
    |     +-- popitem()
    |     +-- del
    |     +-- clear()
    |
    +-- Information
    |     +-- len()
    |     +-- type()
    |     +-- keys()
    |     +-- values()
    |     +-- items()
    |
    +-- Special
          +-- setdefault()
          +-- fromkeys()
          +-- nested dictionaries
          +-- dictionary comprehension
          +-- copy / aliasing
===============================================================
"""
