'''
                 Short-Circuit Operators in Python
                 
In Python, the logical operators and, or avoid evaluating the second operand.
This is called short-circuit evaluation.

Why?
Because once the result is already known from the first operand, Python doesn’t bother checking the second one.

and operator Rule:

If the first operand is False, result will always be False.
So Python skips evaluating the second operand.

'''
def func_a():
    print("func_a called")
    return False

def func_b():
    print("func_b called")
    return True

print("Result:", func_a() and func_b())

'''
Output:
func_a called
Result: False

Notice func_b() was never called, because False and anything = False.
'''


'''
or operator Rule:

If the first operand is True, result will always be True.
So Python skips evaluating the second operand.

'''

def func_c():
    print("func_c called")
    return True

def func_d():
    print("func_d called")
    return False

print("Result:", func_c() or func_d())


'''
Output:
func_c called
Result: True

func_d() never ran, because True or anything = True.
'''


'''
and: stops if left operand is False.
or: stops if left operand is True.
Useful for: avoiding errors, improving performance, setting defaults.

'''

#Avoiding errors
s = None
# Check safely if s has length
if s is not None and len(s) > 0:
    print("String has characters")

'''
Here, len(s) won’t be evaluated if s is None.
Without short-circuiting, it would raise an error.
'''

#Providing default values
name = ""
default = "Guest"
print(name or default)   # Output: Guest

#If name is empty (falsy), Python skips checking and just returns "Guest".


#Chaining conditions efficiently
age = 20
is_student = True

if age > 18 and is_student:
    print("Eligible for discount")


#If age > 18 is False, Python won’t even check is_student
    
'''
Truthy and Falsy in Python

Falsy values: 0, 0.0, '', [], {}, set(), None, False
Everything else → Truthy
So when and / or are evaluated, Python uses truthiness, not just booleans.
In Python, and or don’t just return True/False like in C/C++/Java — they return the actual operand.
'''
'''
and operator Rule:

If the first operand is falsy, return it immediately (short-circuit).
Otherwise, return the second operand.

'''
print(0 and 10)   # 0  (first falsy value)
print(5 and 10)   # 10 (last truthy value)
print(0 or 10)    # 10 (first truthy value)
print(5 or 10)    # 5  (first truthy value)

print(0 and 10)      # 0  (first falsy value)
print("" and "Hi")   # "" (first falsy value)
print(5 and 10)      # 10 (since 5 is truthy, returns second value)
print("Hi" and "Ok") # "Ok" (first is truthy, so return second)

'''
or operator Rule:

If the first operand is truthy, return it immediately (short-circuit).
Otherwise, return the second operand.
'''
print(0 or 10)       # 10 (first is falsy, return second)
print("" or "Guest") # "Guest" (default value pattern)
print(5 or 10)       # 5  (first is truthy, return it)
print("Hi" or "Ok")  # "Hi" (first truthy returned)

    
    
#Combined with functions
def get_value():
    print("Function called++++")
    return 42

print(0 and get_value())   # 0 (short-circuits, function not called)
print(1 and get_value())   # 42 (since first is truthy, function called and second returned)

print(1 or get_value())    # 1 (short-circuits, function not called)
print(0 or get_value())    # 42 (since first falsy, function called and second returned)


#Nested Examples
print([] or {} or "hello")
# [] is falsy → {} is falsy → return "hello"
# Output: "hello"

print([1] and "Hello" and 123)
# [1] truthy → "Hello" truthy → return last: 123
# Output: 123
