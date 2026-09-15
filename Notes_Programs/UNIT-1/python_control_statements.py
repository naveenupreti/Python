"""
===============================================================
        PYTHON CONTROL STRUCTURES
===============================================================
Control structures determine the order in which Python statements
are executed.

Main categories covered here:
1. Conditional execution
   - if
   - if-else
   - if-elif-else
   - nested if
2. Loops / iteration
   - for
   - while
3. Loop control statements
   - break
   - continue
   - pass

Run this entire program to see the examples.
===============================================================
"""


# =============================================================
# 1. if STATEMENT
# =============================================================

print("\n--- 1. if statement ---")

age = 20

if age >= 18:
    print("You are an adult.")

# IMPORTANT:
# Python uses indentation to define the body of if.
# There are no braces { } as in C/C++/Java.


# -------------------------------------------------------------
# if with a false condition
# -------------------------------------------------------------

if age < 18:
    print("You are a minor.")

# Nothing is printed because the condition is False.


# =============================================================
# 2. if-else
# =============================================================

print("\n--- 2. if-else ---")

number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Exactly ONE of the two blocks executes.


# -------------------------------------------------------------
# TRICKY CASE: 0 is considered False
# -------------------------------------------------------------

value = 0

if value:
    print("value is True")
else:
    print("value is False")

# 0 is a "falsy" value in Python.


# Other commonly used falsy values:
# False, None, 0, 0.0, "", [], (), {}, set()
#
# Most other values are truthy.


# =============================================================
# 3. if-elif-else
# =============================================================

print("\n--- 3. if-elif-else ---")

marks = 76

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# IMPORTANT:
# Conditions are checked from TOP to BOTTOM.
# As soon as one condition is True, its block executes
# and the remaining elif/else blocks are skipped.


# -------------------------------------------------------------
# TRICKY CASE: Order of conditions matters
# -------------------------------------------------------------

marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Excellent")

# Output:
# Pass
#
# Why?
# The first condition (marks >= 50) is already True.
# Python never reaches the elif.
#
# Therefore, put more specific conditions before general ones.


# =============================================================
# 4. Multiple independent if statements
# =============================================================

print("\n--- 4. Multiple if statements ---")

marks = 95

if marks >= 50:
    print("Passed")

if marks >= 90:
    print("Excellent")

# BOTH statements execute because these are two separate ifs.
#
# This is different from:
#
# if marks >= 50:
#     ...
# elif marks >= 90:
#     ...
#
# In an if-elif chain, only the first matching block executes.


# =============================================================
# 5. NESTED if
# =============================================================

print("\n--- 5. Nested if ---")

age = 25
has_id = True

if age >= 18:
    print("Age requirement satisfied.")

    if has_id:
        print("ID verified. Entry allowed.")
    else:
        print("ID required.")

else:
    print("Entry not allowed because you are under 18.")

# An if inside another if is called a nested if.


# -------------------------------------------------------------
# TRICKY CASE: nested conditions can be simplified
# -------------------------------------------------------------

# Instead of:
#
# if age >= 18:
#     if has_id:
#         print("Allowed")
#
# we can often write:
#
# if age >= 18 and has_id:
#     print("Allowed")
#
# But nested if can be clearer when different actions are needed.


# =============================================================
# 6. CONDITIONAL EXPRESSION (TERNARY EXPRESSION)
# =============================================================

print("\n--- 6. Conditional expression ---")

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)

# Syntax:
#
# value_if_true if condition else value_if_false
#
# This is an expression, not a normal if statement.


# =============================================================
# 7. for LOOP
# =============================================================

print("\n--- 7. for loop ---")

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
#
# range(5) produces 0, 1, 2, 3, 4.
# The ending value 5 is NOT included.


# -------------------------------------------------------------
# for loop with start and stop
# -------------------------------------------------------------

print("\nfor loop with start and stop:")

for i in range(2, 6):
    print(i)

# Output: 2 3 4 5


# -------------------------------------------------------------
# for loop with step
# -------------------------------------------------------------

print("\nfor loop with step:")

for i in range(2, 11, 2):
    print(i)

# Output:
# 2 4 6 8 10


# -------------------------------------------------------------
# TRICKY CASE: negative step
# -------------------------------------------------------------

print("\nfor loop with negative step:")

for i in range(5, 0, -1):
    print(i)

# Output:
# 5 4 3 2 1
#
# range(5, 0, -1) does NOT include 0.


# =============================================================
# 8. for LOOP OVER A STRING
# =============================================================

print("\n--- 8. Iterating over a string ---")

word = "Python"

for ch in word:
    print(ch)

# The loop variable receives one character at a time.


# =============================================================
# 9. for LOOP OVER A LIST
# =============================================================

print("\n--- 9. Iterating over a list ---")

numbers = [10, 20, 30]

for n in numbers:
    print(n)

# A for loop can iterate over many iterable objects:
# strings, lists, tuples, sets, dictionaries, ranges, etc.


# =============================================================
# 10. while LOOP
# =============================================================

print("\n--- 10. while loop ---")

count = 1

while count <= 5:
    print(count)
    count += 1

# while repeatedly executes its body while the condition is True.


# -------------------------------------------------------------
# TRICKY CASE: forgetting to update the condition
# -------------------------------------------------------------

# count = 1
#
# while count <= 5:
#     print(count)
#
# This creates an INFINITE LOOP because count never changes.
#
# Always make sure that a while loop can eventually become False.


# =============================================================
# 11. while LOOP MAY EXECUTE ZERO TIMES
# =============================================================

print("\n--- 11. while loop may execute zero times ---")

count = 10

while count < 5:
    print(count)
    count += 1

# Nothing is printed because the condition is False initially.


# =============================================================
# 12. for LOOP MAY ALSO EXECUTE ZERO TIMES
# =============================================================

print("\n--- 12. for loop may execute zero times ---")

for i in range(0):
    print(i)

# Nothing is printed because range(0) is empty.


# =============================================================
# 13. break
# =============================================================

print("\n--- 13. break ---")

for i in range(1, 11):

    if i == 6:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
#
# break immediately terminates the nearest enclosing loop.


# -------------------------------------------------------------
# break in while loop
# -------------------------------------------------------------

print("\nbreak with while:")

number = 1

while True:

    print(number)

    if number == 3:
        break

    number += 1

# while True creates a loop whose condition is always True.
# break provides the exit condition.


# =============================================================
# 14. continue
# =============================================================

print("\n--- 14. continue ---")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5
#
# continue SKIPS the remaining statements of the CURRENT
# iteration and starts the next iteration.


# -------------------------------------------------------------
# continue in while loop
# -------------------------------------------------------------

print("\ncontinue with while:")

i = 0

while i < 5:

    i += 1

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5
#
# IMPORTANT:
# In a while loop, update the loop variable BEFORE continue
# when necessary.
#
# Otherwise, continue may cause an infinite loop.


# =============================================================
# 15. pass
# =============================================================

print("\n--- 15. pass ---")

for i in range(3):

    if i == 1:
        pass

    print(i)

# Output:
# 0
# 1
# 2
#
# pass does NOTHING.
#
# It is simply a placeholder where Python requires a statement.


# -------------------------------------------------------------
# break vs continue vs pass
# -------------------------------------------------------------

print("""
break    -> terminates the loop completely
continue -> skips the current iteration
pass     -> does nothing; execution continues normally
""")


# =============================================================
# 16. pass IS NOT THE SAME AS continue
# =============================================================

print("\n--- 16. pass vs continue ---")

print("Using pass:")

for i in range(3):

    if i == 1:
        pass          # Does nothing

    print(i)

print("Using continue:")

for i in range(3):

    if i == 1:
        continue      # Skips print(i)

    print(i)

# pass output:
# 0
# 1
# 2
#
# continue output:
# 0
# 2


# =============================================================
# 17. break vs continue
# =============================================================

print("\n--- 17. break vs continue ---")

print("break:")

for i in range(1, 6):

    if i == 3:
        break

    print(i)

print("continue:")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# break:
# 1 2
#
# continue:
# 1 2 4 5


# =============================================================
# 18. NESTED LOOPS
# =============================================================

print("\n--- 18. Nested loops ---")

for i in range(1, 4):

    for j in range(1, 4):

        print("i =", i, "j =", j)

# The inner loop runs completely for every iteration
# of the outer loop.


# -------------------------------------------------------------
# TRICKY CASE: break affects only the nearest loop
# -------------------------------------------------------------

print("\nNested loop with break:")

for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            break

        print("i =", i, "j =", j)

# break terminates only the INNER loop.
# The outer loop continues.


# -------------------------------------------------------------
# continue in nested loop
# -------------------------------------------------------------

print("\nNested loop with continue:")

for i in range(1, 3):

    for j in range(1, 4):

        if j == 2:
            continue

        print("i =", i, "j =", j)

# continue affects only the nearest enclosing loop.


# =============================================================
# 19. for-else
# =============================================================

print("\n--- 19. for-else ---")

for i in range(3):
    print(i)
else:
    print("Loop completed normally.")

# The else block executes when the loop finishes normally.


# -------------------------------------------------------------
# IMPORTANT: break prevents loop-else
# -------------------------------------------------------------

print("\nfor-else with break:")

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Loop completed normally.")

# Output:
# 0
# 1
# 2
#
# The else block does NOT execute because break terminated
# the loop.


# =============================================================
# 20. while-else
# =============================================================

print("\n--- 20. while-else ---")

i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("while loop completed normally.")

# while loops can also have an else clause.


# =============================================================
# 21. Practical use of for-else: SEARCH
# =============================================================

print("\n--- 21. Practical for-else search ---")

numbers = [10, 20, 30, 40]
target = 30

for n in numbers:

    if n == target:
        print("Found:", target)
        break

else:
    print("Not found:", target)

# If target is found -> break executes -> else is skipped.
# If target is not found -> loop finishes -> else executes.


# =============================================================
# 22. INPUT + CONDITIONAL EXECUTION
# =============================================================

print("\n--- 22. Input example ---")

# input() ALWAYS returns a string.
#
# Therefore, convert it when a number is required.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example:
# Input: 20
# Output: You are eligible to vote.


# =============================================================
# 23. INPUT + while LOOP
# =============================================================

print("\n--- 23. Input controlled while loop ---")

# Keep asking until the user enters 0.

while True:

    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    print("You entered:", number)

# break is useful when the number of iterations is not known
# in advance.


# =============================================================
# 24. COMBINING if + for + continue
# =============================================================

print("\n--- 24. Combining if, for and continue ---")

numbers = [10, 15, 20, 25, 30]

for n in numbers:

    if n % 2 != 0:
        continue       # Skip odd numbers

    print("Even:", n)

# Output:
# Even: 10
# Even: 20
# Even: 30


# =============================================================
# 25. COMBINING if + for + break
# =============================================================

print("\n--- 25. Finding the first number divisible by 7 ---")

numbers = [10, 15, 20, 22, 28, 35]

for n in numbers:

    if n % 7 == 0:
        print("First number divisible by 7:", n)
        break

# Once 28 is found, the loop terminates.


# =============================================================
# 26. pass IN A FUNCTION / CLASS / CONDITIONAL
# =============================================================

print("\n--- 26. pass as a placeholder ---")

def future_function():
    pass

# pass allows us to create an empty function temporarily.
# Without pass, an empty function causes a SyntaxError.


# pass can also be used in an empty class:

class Student:
    pass

# Student is a valid class even though it currently has no body.


# =============================================================
# 27. IMPORTANT: break, continue and pass ARE DIFFERENT
# =============================================================

print("""
===============================================================
SUMMARY
===============================================================

if
    Executes a block only when a condition is True.

if-else
    Selects one of two alternatives.

if-elif-else
    Selects the FIRST matching condition.

nested if
    An if statement inside another if/else block.

for
    Iterates over an iterable such as list, tuple, string,
    set, dictionary, range, etc.

while
    Repeats while its condition remains True.

break
    Immediately exits the nearest enclosing loop.

continue
    Skips the remaining part of the current iteration and
    proceeds to the next iteration.

pass
    Does nothing. It is a placeholder statement.

for-else / while-else
    else executes when the loop finishes normally,
    but NOT when it is terminated by break.

===============================================================
IMPORTANT TRICKY POINTS
===============================================================

1. Python uses indentation to define blocks.

2. range(stop) starts at 0 and excludes stop.
   range(5) -> 0, 1, 2, 3, 4

3. if-elif-else executes only the FIRST matching branch.

4. Multiple independent if statements can all execute.

5. break affects only the nearest enclosing loop.

6. continue affects only the nearest enclosing loop.

7. pass does NOT skip an iteration.

8. while loops need a condition that eventually becomes False
   or a break statement; otherwise they can run forever.

9. Be careful with continue in while loops:
   forgetting to update the loop variable can cause an
   infinite loop.

10. for-else and while-else are different from if-else:
    their else executes only when the loop terminates normally.
===============================================================
""")
