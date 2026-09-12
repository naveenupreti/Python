# ==============================================================
# PYTHON INPUT / OUTPUT
# Keyboard input using input()
# Formatted output using print()
# ==============================================================


# --------------------------------------------------------------
# 1. BASIC print()
# --------------------------------------------------------------

print("Hello Python")                 # Prints a string and moves to next line
print(100)                            # Prints an integer
print(3.14)                           # Prints a floating-point number
print(True)                            # Prints a Boolean value
print()                               # Prints only a newline (blank line)


# --------------------------------------------------------------
# 2. print() CAN PRINT MULTIPLE VALUES
# --------------------------------------------------------------

print("Age:", 50)                     # Multiple objects can be printed
print("Python", "C", "Java")          # Values are separated by a space by default
print(10, 20, 30)


# sep — separator between multiple objects
print("2026", "09", "06", sep="-")    # Output: 2026-09-06
print("A", "B", "C", sep=" | ")      # Output: A | B | C

# sep is used ONLY between objects.
print("Hello", sep="-")               # No visible '-' because there is only one object


# --------------------------------------------------------------
# 3. end — WHAT TO PRINT AT THE END
# --------------------------------------------------------------

print("Hello", end=" ")               # Normally print() ends with '\n'
print("Python")                       # Because previous print() ended with space,
                                      # this appears on the same line

print("A", end="---")
print("B")                            # Output: A---B

print("1", end="")
print("2", end="")
print("3")                            # Output: 123


# sep and end can be used together
print("2026", "09", "06", sep="/", end=" --> ")
print("Sunday")
# Output: 2026/09/06 --> Sunday


# --------------------------------------------------------------
# 4. SPECIAL CHARACTERS IN print()
# --------------------------------------------------------------

print("Hello\nPython")                # \n = new line
print("Hello\tPython")                # \t = tab
print("He said \"Hello\"")            # \" = double quote
print('It\'s Python')                 # \' = single quote
print("C:\\Python")                   # \\ = backslash


# --------------------------------------------------------------
# 5. print() CONVERTS OBJECTS TO TEXT FOR DISPLAY
# --------------------------------------------------------------

x = 100
print(x)                              # Displays 100

# print() can display different data types together
print("Value =", x, "Type =", type(x))
# Output will contain something like:
# Value = 100 Type = <class 'int'>


# --------------------------------------------------------------
# 6. IMPORTANT: print() DOES NOT RETURN THE PRINTED VALUE
# --------------------------------------------------------------

result = print("Hello")
print("result =", result)
# Output:
# Hello
# result = None

# print() displays something on the screen,
# but its return value is None.


# ==============================================================
#                     INPUT USING input()
# ==============================================================


# --------------------------------------------------------------
# 7. BASIC input()
# --------------------------------------------------------------

# name = input("Enter your name: ")
# print("Hello", name)

# input() displays the prompt and waits for the user
# to type something and press ENTER.


# --------------------------------------------------------------
# 8. input() ALWAYS RETURNS A STRING
# --------------------------------------------------------------

# age = input("Enter your age: ")
# print(age)
# print(type(age))

# If the user enters:
# 50
#
# age contains the STRING "50", not integer 50.
#
# type(age) -> <class 'str'>


# --------------------------------------------------------------
# 9. TRICKY CASE: "10" + "20"
# --------------------------------------------------------------

a = "10"
b = "20"

print(a + b)                          # Output: 1020
                                      # String concatenation, NOT addition

# To perform numerical addition:
print(int(a) + int(b))                # Output: 30


# --------------------------------------------------------------
# 10. READING AN INTEGER
# --------------------------------------------------------------

# age = int(input("Enter your age: "))
# print("Next year:", age + 1)

# input() -> "50"
# int("50") -> 50
#
# Therefore age becomes an integer.


# --------------------------------------------------------------
# 11. READING A FLOAT
# --------------------------------------------------------------

# price = float(input("Enter price: "))
# print("Price =", price)

# Example:
# Input:  99.50
# float("99.50") -> 99.5


# --------------------------------------------------------------
# 12. READING MULTIPLE VALUES
# --------------------------------------------------------------

# Suppose the user enters:
# 10 20 30

# values = input("Enter three numbers: ").split()
# print(values)

# Output:
# ['10', '20', '30']

# IMPORTANT:
# split() produces strings.


# Convert them to integers:
# a, b, c = map(int, input("Enter 3 numbers: ").split())
# print(a + b + c)

# Input:
# 10 20 30
#
# map(int, ...) converts each string to int.
# a=10, b=20, c=30
# Output: 60


# --------------------------------------------------------------
# 13. READING MULTIPLE FLOATS
# --------------------------------------------------------------

# x, y = map(float, input("Enter two numbers: ").split())
# print("Sum =", x + y)

# Input:
# 10.5 20.5
#
# Output:
# Sum = 31.0


# --------------------------------------------------------------
# 14. WHAT HAPPENS IF INVALID DATA IS ENTERED?
# --------------------------------------------------------------

# age = int(input("Enter age: "))

# If user enters:
# abc
#
# int("abc") raises:
# ValueError
#
# So the program terminates unless the error is handled.


# --------------------------------------------------------------
# 15. SAFELY READING A NUMBER USING try-except
# --------------------------------------------------------------

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid integer.")

# Example:
# Input: 25
# Output: Your age is: 25
#
# Input: abc
# Output: Please enter a valid integer.


# ==============================================================
#                 FORMATTED OUTPUT
# ==============================================================


# --------------------------------------------------------------
# 16. BASIC FORMATTING USING f-STRINGS
# --------------------------------------------------------------

name = "Naveen"
age = 52

print(f"My name is {name} and I am {age} years old.")

# Anything inside { } is evaluated and inserted into the string.


# --------------------------------------------------------------
# 17. EXPRESSIONS INSIDE f-STRINGS
# --------------------------------------------------------------

a = 10
b = 20

print(f"Sum = {a + b}")               # Expression is evaluated first
print(f"Product = {a * b}")


# --------------------------------------------------------------
# 18. FORMATTING DECIMAL NUMBERS
# --------------------------------------------------------------

price = 123.456789

print(f"{price:.2f}")                 # 2 digits after decimal
# Output: 123.46

print(f"{price:.3f}")                 # 3 digits after decimal
# Output: 123.457


# --------------------------------------------------------------
# 19. PERCENTAGE FORMAT
# --------------------------------------------------------------

percentage = 0.8567

print(f"{percentage:.2%}")
# Output: 85.67%

# .2% means:
# multiply by 100 and display 2 decimal places.


# --------------------------------------------------------------
# 20. WIDTH AND ALIGNMENT
# --------------------------------------------------------------

name = "Python"

print(f"{name:10}")                   # Width 10, left aligned by default
print(f"{name:<10}")                  # Explicit left alignment
print(f"{name:>10}")                  # Right alignment
print(f"{name:^10}")                  # Center alignment

# The width is a MINIMUM width.
# It does NOT truncate a longer value.

print(f"{'PythonProgramming':10}")
# The complete string is printed even though it is longer than 10.


# --------------------------------------------------------------
# 21. FILL CHARACTER + ALIGNMENT
# --------------------------------------------------------------

print(f"{'Python':*<10}")             # Fill unused space with *
print(f"{'Python':-^10}")             # Fill with -
print(f"{'Python':.>10}")             # Fill with .


# --------------------------------------------------------------
# 22. FORMATTING INTEGERS WITH COMMAS
# --------------------------------------------------------------

number = 123456789

print(f"{number:,}")
# Output: 123,456,789


# --------------------------------------------------------------
# 23. INTEGER NUMBER SYSTEM FORMATTING
# --------------------------------------------------------------

n = 255

print(f"Decimal : {n:d}")              # Decimal
print(f"Binary  : {n:b}")              # Binary
print(f"Octal   : {n:o}")              # Octal
print(f"Hex     : {n:x}")              # Hexadecimal
print(f"HEX     : {n:X}")              # Uppercase hexadecimal


# --------------------------------------------------------------
# 24. SHOWING + / - SIGN
# --------------------------------------------------------------

#The + format option means:

#Always display the sign, even for positive numbers.

#So:

n = 25
print(f"{n:+}")       # +25

n = -25
print(f"{n:+}")       # -25

n = 0
print(f"{n:+}")       # +0
n = 25

#The - option means:

#Display the minus sign only for negative numbers.

#This is actually the default behavior for numeric formatting.

n = 25
print(f"{n:-}")       # 25

n = -25
print(f"{n:-}")       # -25

n = 0
print(f"{n:-}")       # 0

#So - does not mean "display a plus sign for positive numbers."
n = 27
print(f"{n:+}")                        # +27
print(f"{n:-}")                        # 27
print(f"{-n:+}")                       # -27

#In Python's numeric format specification:

# +   → always show sign (+ or -)
# -   → show only negative sign (default)
# space → show a space for positive, - for negative

# --------------------------------------------------------------
# 25. ZERO PADDING
# --------------------------------------------------------------

number = 42

print(f"{number:05}")                  # Output: 00042

# Useful for IDs, serial numbers, dates, etc.


# --------------------------------------------------------------
# 26. COMBINING FORMAT OPTIONS
# --------------------------------------------------------------

number = 1234567.891

print(f"{number:,.2f}")
# Output: 1,234,567.89


# --------------------------------------------------------------
# 27. OLD % FORMATTING
# --------------------------------------------------------------

name = "Python"
age = 34

print("Language: %s, Age: %d" % (name, age))

# %s -> string
# %d -> integer
# %f -> floating-point number

value = 12.3456
print("Value = %.2f" % value)
# Output: Value = 12.35


# --------------------------------------------------------------
# 28. str.format() METHOD
# --------------------------------------------------------------

name = "Python"
version = 3.14

print("Language: {}, Version: {}".format(name, version))

# Positional arguments
print("{0} {1} {0}".format("Python", "Programming"))
# Output: Python Programming Python

# Named arguments
print("Name={name}, Age={age}".format(name="Naveen", age=50))


# ==============================================================
#                 COMMON TRICKY CASES
# ==============================================================


# --------------------------------------------------------------
# 29. print() VS RETURN
# --------------------------------------------------------------

def display():
    print("Hello")                     # Displays Hello
                                      # but does NOT return Hello

x = display()
print("x =", x)
# Output:
# Hello
# x = None


# --------------------------------------------------------------
# 30. print() WITH sep
# --------------------------------------------------------------

print(1, 2, 3, sep="")
# Output: 123

print(1, 2, 3, sep=",")
# Output: 1,2,3


# --------------------------------------------------------------
# 31. sep MUST BE A STRING
# --------------------------------------------------------------

# print(1, 2, 3, sep=10)
# TypeError!
#
# sep must be a string.


# --------------------------------------------------------------
# 32. end MUST ALSO BE A STRING
# --------------------------------------------------------------

# print("Hello", end=10)
# TypeError!
#
# end must be a string.


# --------------------------------------------------------------
# 33. input() STRIPS THE ENTER KEY
# --------------------------------------------------------------

# text = input("Enter text: ")
#
# If user types:
# Hello<ENTER>
#
# text contains:
# "Hello"
#
# The newline generated by pressing ENTER is not included.


# --------------------------------------------------------------
# 34. input() CAN READ AN EMPTY STRING
# --------------------------------------------------------------

# text = input("Enter something: ")
#
# If the user simply presses ENTER:
#
# text == ""
# type(text) == str


# --------------------------------------------------------------
# 35. SPACES ARE PRESERVED BY input()
# --------------------------------------------------------------

# text = input("Enter text: ")
#
# Input:
#   Hello World
#
# text contains "Hello World"
#
# input() does NOT automatically split words.
# split() is needed if individual words are required.


# --------------------------------------------------------------
# 36. input().split() DEFAULT BEHAVIOR
# --------------------------------------------------------------

text = "   Python   is   easy   "

words = text.split()

print(words)
# Output:
# ['Python', 'is', 'easy']

# split() without an argument:
# - removes leading/trailing whitespace
# - treats consecutive whitespace as one separator.


# --------------------------------------------------------------
# 37. print() CAN DISPLAY MANY DIFFERENT TYPES
# --------------------------------------------------------------

data = [1, 2, 3]
info = {"name": "Python"}

print(data)
print(info)

# print() uses the object's string representation for display.


# ==============================================================
# 38. A SMALL PRACTICAL PROGRAM
# ==============================================================

# Uncomment these lines to run the complete example:

# name = input("Enter your name: ")
# marks1, marks2, marks3 = map(float, input("Enter 3 marks: ").split())

# total = marks1 + marks2 + marks3
# average = total / 3

# print("\n----- RESULT -----")
# print(f"Student : {name}")
# print(f"Total   : {total:.2f}")
# print(f"Average : {average:.2f}")
# print(f"Status  : {'PASS' if average >= 40 else 'FAIL'}")


# ==============================================================
# 39. IMPORTANT SUMMARY
# ==============================================================

# print()
#   -> Displays output on the screen.
#   -> Can print multiple objects.
#   -> sep controls the separator between objects.
#   -> end controls what is printed after the output.
#   -> Returns None.
#
# input()
#   -> Displays a prompt (optional).
#   -> Waits for keyboard input.
#   -> User normally presses ENTER to finish.
#   -> ALWAYS returns a str.
#
# int(input(...))
#   -> Reads an integer.
#
# float(input(...))
#   -> Reads a floating-point number.
#
# input().split()
#   -> Reads multiple whitespace-separated strings.
#
# map(int, input().split())
#   -> Reads multiple integers.
#
# f"...{expression}..."
#   -> Modern and usually preferred way of formatting output.
#
# :.2f
#   -> Two digits after decimal.
#
# :, 
#   -> Thousands separator.
#
# :05
#   -> Zero-padding to width 5.
#
# :<10
#   -> Left aligned, width 10.
#
# :>10
#   -> Right aligned, width 10.
#
# :^10
#   -> Center aligned, width 10.