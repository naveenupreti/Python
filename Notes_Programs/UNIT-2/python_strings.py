# ============================================================
#                    PYTHON STRINGS
# ============================================================
# A string is a sequence of characters.
# A string can be written inside:
#     1. Single quotes      'Hello'
#     2. Double quotes      "Hello"
#     3. Triple quotes      '''Hello''' or """Hello"""
#
# Python strings are:
#     • Ordered      → characters have positions (indexes)
#     • Immutable    → individual characters cannot be changed
#     • Unicode      → can represent characters from many languages
# ============================================================


# ------------------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------------------

s1 = 'Hello'                 # String using single quotes
s2 = "World"                 # String using double quotes

# Triple quotes allow a string to span multiple lines.
s3 = '''This is
a multiline string.'''

print(s1, s2)
print(s3)


# ------------------------------------------------------------
# 2. ESCAPE SEQUENCES IN STRINGS
# ------------------------------------------------------------
# An escape sequence starts with a backslash (\).
# It gives a special meaning to the following character.

msg2 = "He said, \"Let Us Python\""
# \" means: put a double quote inside the string
# without treating it as the end of the string.

file1 = "C:\\temp\\newfile"
# \\ represents ONE literal backslash.
# Therefore Python stores:
# C:\temp\newfile

file2 = r"C:\temp\newfile"
# r before the string creates a RAW STRING.
# Most backslashes are treated literally.
# Therefore we do not need to write \\.

print(msg2)
print(file1)
print(file2)


# ------------------------------------------------------------
# 3. MULTILINE STRINGS
# ------------------------------------------------------------

# There are several ways to create a string over multiple
# lines of source code.


# ---- Method 1: Explicit line continuation using \ ----

msg3 = "multi...\n" \
       "line ..." \
       "string..."

# \ tells Python that the statement continues on the next line.
#
# \n is an escape sequence representing a newline.
#
# Output:
# multi...
# line ...string...

print("msg3=" + msg3)


# ---- Method 2: Triple-quoted string ----

msg4 = """multi...
line...
string......"""

# Triple quotes preserve the actual newline characters.

print("msg4=" + msg4)


# ---- Method 3: Implicit concatenation inside parentheses ----

msg5 = ("multi..."
        "line...."
        "string....")

# Python automatically joins adjacent string literals.
# No + operator is required.
#
# Notice that there is NO space or newline between the strings.

print("msg5=" + msg5)


# ------------------------------------------------------------
# 4. ACCESSING CHARACTERS USING INDEX
# ------------------------------------------------------------

s = "PYTHON"

# Index positions:
#
# Positive index:
#     P   Y   T   H   O   N
#     0   1   2   3   4   5
#
# Negative index:
#     P    Y    T    H    O    N
#    -6   -5   -4   -3   -2   -1

print(s[0])       # First character  → P
print(s[3])       # Fourth character → H
print(s[-1])      # Last character   → N
print(s[-3])      # Third from last  → H


# ------------------------------------------------------------
# 5. BASIC STRING OPERATIONS
# ------------------------------------------------------------

s1 = "Hello"
s2 = "World"

# + performs string concatenation.
print(s1 + " " + s2)
# Output: Hello World


# * repeats a string.
print(s1 * 3)
# Output: HelloHelloHello


# 'in' checks whether a character or substring exists.
print("H" in s1)
# Output: True


# len() returns the number of characters in a string.
print(len(s2))
# Output: 5


# ------------------------------------------------------------
# 6. STRING SLICING
# ------------------------------------------------------------
# Syntax:
#
#     string[start : stop : step]
#
# IMPORTANT:
#     start is INCLUDED
#     stop is EXCLUDED
#
# Example:
#     s[0:6]
#
# takes indexes 0,1,2,3,4,5
# but NOT index 6.
'''
The sign of step determines the direction.

| Slice   | Direction              | Example  |
| --------| ---------------------- | -------- |
| s[::1]  | Left → Right           | `PYTHON` |
| s[::2]  | Left → Right, skipping | `PTO`    |
| s[::-1] | Right → Left           | `NOHTYP` |
| s[::-2] | Right → Left, skipping | `NHP`    |
'''
s = "PYTHONPROGRAM"

# Index:
#
# P Y T H O N P R O G R A M
# 0 1 2 3 4 5 6 7 8 9 10 11 12


print(s[0:6])
# PYTHON
# Characters at indexes 0 to 5


print(s[:6])
# PYTHON
# Missing start means: start from index 0.


print(s[6:])
# PROGRAM
# Missing stop means: continue to the end.


print(s[-7:-1])
# PROGRA
# -7 is included, -1 is excluded.


print(s[::2])
# Every second character
# step = 2

#s[::-1] means: start from the end, move toward the beginning, one character at a time
print(s[::-1])
# Reverse the complete string.
# A step of -1 means move from right to left.


# ------------------------------------------------------------
# 7. COMMON STRING METHODS
# ------------------------------------------------------------

s = " hello python "


# upper() → converts letters to uppercase
print(s.upper())
# " HELLO PYTHON "


# lower() → converts letters to lowercase
print(s.lower())
# " hello python "


# title() → first letter of each word becomes uppercase
print(s.title())
# " Hello Python "


# capitalize() → only the first character becomes uppercase
print(s.capitalize())
# " hello python "
# Note: the first character of s is a space,
# so the visible letters remain lowercase.


# strip() → removes whitespace from both ends
print(s.strip())
# "hello python"

'''
| Method   | What it removes | Example                           |
| ---------| --------------- | ----------------------------------|
| strip()  | Both sides      | "  Hello  ".strip()  → "Hello"    |
| lstrip() | Left side only  | "  Hello  ".lstrip() → "Hello  "  |
| rstrip() | Right side only | "  Hello  ".rstrip() → "  Hello"  |

'''

# find() → returns the index of the first occurrence.
# rfind() -> returns the index of the last occurrence.
# If the substring is not found, it returns -1.

s = "Python is easy and Python is powerful"

print(s.find("Python"))    # First occurrence 0
print(s.rfind("Python"))   # Last occurrence 19

s = "Hello Python"
print(s.find("Java")) # -1
print(s.rfind("Java")) # -1

'''
string.find(substring)
string.find(substring, start)
string.find(substring, start, end)
    Form				Meaning
s.find("x")			Search entire string
s.find("x", 5)		Search from index 5
s.find("x", 5, 10)	Search from index 5 to 9
Not found			Returns -1
rfind()				Finds last occurrence
'''

s = " hello python "
# count() → counts occurrences of a substring
print(s.count("o")) # 2

# replace(old, new) → returns a new string
print(s.replace("python", "world"))
# " hello world "

# split() → breaks a string into a LIST.
# By default, whitespace is used as the separator.
words = s.split()

print(words)
# ['hello', 'python']


# join() → joins elements of a sequence into one string.
print("-".join(words))
# hello-python


# isdigit() → True if all characters are digits
print("123".isdigit())
# True


# isalpha() → True if all characters are alphabetic
print("abc".isalpha())
# True


# isspace() → True if all characters are whitespace
print(" ".isspace())
# True


# ------------------------------------------------------------
# 8. chr() FUNCTION
# ------------------------------------------------------------
# chr(number) returns the Unicode character represented by
# that number.
#
# ASCII is a subset of Unicode.
# Therefore the familiar ASCII codes also work with chr().

print(chr(65))       # A
print(chr(97))       # a
print(chr(48))       # 0
print(chr(32))       # Space
print(chr(8377))     # ₹


# ============================================================
#                       CHR() AND ORD()
# ============================================================

# ------------------------------------------------------------
# 9. ord() FUNCTION
# ------------------------------------------------------------
# ord(character) does the opposite of chr().
#
#     chr(65)  → 'A'
#     ord('A') → 65
#
# ord() accepts exactly ONE character.

ch = 'A'

print(f"ASCII/Unicode value of {ch} is {ord(ch)}")


# ------------------------------------------------------------
# 10. CONVERTING A NUMBER INTO A CHARACTER
# ------------------------------------------------------------

num = 8377

print(f"Character for code {num} is {chr(num)}")
# Output:
# Character for code 8377 is ₹


# ------------------------------------------------------------
# 11. PRINTING A-Z AND a-z USING chr()
# ------------------------------------------------------------

print("Uppercase letters:")

# ASCII/Unicode values of A-Z are 65-90.
#
# range(65, 91) generates:
# 65, 66, ..., 90
#
# 91 is NOT included.

for i in range(65, 91):
    print(chr(i), end=" ")

print()


print("Lowercase letters:")

# ASCII/Unicode values of a-z are 97-122.

for i in range(97, 123):
    print(chr(i), end=" ")

print()


# ------------------------------------------------------------
# 12. CHARACTER PATTERN USING chr()
# ------------------------------------------------------------

rows = 5

# Outer loop controls the number of rows.
for i in range(65, 65 + rows):

    # Inner loop prints characters from A up to the
    # character represented by i.
    for j in range(65, i + 1):
        print(chr(j), end=" ")

    # Move to the next line after completing one row.
    print()


# Output:
#
# A
# A B
# A B C
# A B C D
# A B C D E


# ============================================================
#                    STRING COMPARISON
# ============================================================

# Strings are compared lexicographically (dictionary-like
# order), character by character.
#
# Python compares the Unicode code points of corresponding
# characters.
#
# For the English alphabet:
#
# A = 65, B = 66, ... Z = 90
# a = 97, b = 98, ... z = 122
#
# Therefore:
#     "A" < "a"
#
# IMPORTANT:
# Do not say that Python uses only ASCII for string comparison.
# Python strings use Unicode code points.
# ASCII values are relevant for ordinary English characters
# because ASCII is included in Unicode.


s1 = "Bombay"
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"


print(s1 == s2)
# False
# 'B' and 'b' are different characters.


print(s1 == s5)
# True
# Both strings contain exactly the same characters.


print(s1 <= s3)
# True
# Comparison starts with the first character:
# 'B' < 'N'


print(s1 > s5)
# False
# Both strings are equal.


print(s1 < s2)
# True
# 'B' has a smaller Unicode value than 'b'.


print(s1 <= s4)
# True
# "Bombay" is a prefix of "Bombaywala".
# When all characters of the shorter string match,
# the shorter string is considered smaller.


# ============================================================
#                 FINDING CHARACTERS
# ============================================================

s = "The Terrible Tiger Tore The Towel"
print(s)
# We want to find every occurrence of uppercase 'T'.

pos = -1

while True:

    # Search for the next 'T'.
    #
    # pos + 1 ensures that the search starts AFTER the
    # previous occurrence.
    #
    # find() returns:
    #     index → if found
    #     -1   → if not found

    pos = s.find("T", pos + 1)

    if pos == -1:
        # No more 'T' characters found.
        break

    print(pos, s[pos])


# ------------------------------------------------------------
# 13. COUNTING CHARACTERS
# ------------------------------------------------------------

count_t = s.count("T")

print(f"count_t = {count_t}")


# ------------------------------------------------------------
# 14. REPLACING CHARACTERS
# ------------------------------------------------------------

# replace(old, new, count)
#
# count_t tells Python to replace at most that many
# occurrences of 'T'.
#
# Since count_t is the total number of T's, all uppercase
# T characters will be replaced.

s = s.replace("T", "t", count_t)

print(s)

'''
output:
The Terrible Tiger Tore The Towel
0 T
4 T
13 T
19 T
24 T
28 T
count_t = 6
the terrible tiger tore the towel
'''
