'''
                           Concept of Operator Precedence and Associativity

Operator Precedence determines the order in which operators are evaluated in an expression.
Higher precedence operators are evaluated before lower precedence operators.

Associativity decides the order of evaluation when operators of the same precedence appear.

Left-to-right: evaluated from left to right

Right-to-left: evaluated from right to left

Example:

x = 3 + 4 * 2
# * has higher precedence than +, so it is evaluated first
# 3 + (4*2) = 11


Python Operator Precedence and Associativity

Precedence	Operator(s)			Description																	Associativity
1			()			Parentheses (expression grouping, function calls, tuple creation with commas)	Left → Right
2	x[index], x(attr), x.attribute		Indexing, slicing, function call, attribute reference			Left → Right
3	**					Exponentiation																	Right → Left
4	+x, -x, ~x			Unary plus, minus, bitwise NOT													Right → Left
5	*, /, //, %			Multiplication, division, floor division, modulo								Left → Right
6	+, -				Addition, subtraction															Left → Right
7	<<, >>				Bitwise shifts																	Left → Right
8	&					Bitwise AND																		Left → Right
9	^					Bitwise XOR																		Left → Right
10	|					Bitwise OR																		Left → Right
11	<, <=, >, >=, ==, !=, is, is not, in, not in	Comparison operators								Left → Right
12	not					Logical NOT																		Right → Left
13	and					Logical AND																		Left → Right
14	or					Logical OR																		Left → Right
15	if … else …			Conditional expression															Right → Left
16	lambda				Lambda expression																Left → Right
17	=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=	Assignment operators						Right → Left
18	,					Comma (tuple, argument separator, multiple assignments)							Left → Right
# comma(,) is not a operator in python. It is a used as a separator.

**Example 1: Mixed + and ***
result = 3 + 4 * 2
print(result)  # 11
# * is higher precedence than + → 4*2=8 → 3+8=11

Example 2: Parentheses override precedence
result = (3 + 4) * 2
print(result)  # 14
# Parentheses first → 3+4=7 → 7*2=14

Example 3: Exponentiation right-to-left
result = 2 ** 3 ** 2
print(result)  # 512
# Right-to-left → 3**2=9 → 2**9=512

Example 4: Unary + and -
x = -2 ** 2
print(x)  # -4
# Unary - has lower precedence than ** → -(2**2)=-4

Example 5: Floor division and modulo
x = 17 // 3 % 2
print(x)  # 1
# // and % same precedence → left-to-right: 17//3=5 → 5%2=1

Example 6: Comparison chaining
x = 5
print(1 < x < 10)  # True
# Python allows chaining → (1<x) and (x<10)

Example 7: Logical operators precedence
x = True or False and False
print(x)  # True
# and > or → True or (False and False) → True or False → True

Example 8: Assignment right-to-left
a = b = c = 10
print(a, b, c)  # 10 10 10
# Right-to-left → c=10 → b=c → a=b

Example 9: Bitwise operators
x = 5 | 3 & 2
print(x)  # 5
# & > | → 3&2=2 → 5|2=7

Example 10: Shift operators
x = 2 << 3 + 1
print(x)  # 32
# + higher than << → 3+1=4 → 2<<4 = 32

Example 11: Mixing not, and, or
x = not True or False and True
print(x)  # False
# Precedence: not > and > or
# not True = False → False or (False and True) → False or False → False

Example 12:Exponentiation right-to-left
x = -2 ** -2

Step 1: Operator precedence
** (exponentiation) has higher precedence than unary -.
Exponentiation is right-to-left associative.
So Python interprets it as:
x = -(2 ** -2)

Step 2: Calculate 2 ** -2
Negative exponent: 
= (2**(-2)) = 1/(2**2)
= 1/4
= 0.25

Step 3: Apply unary minus
x = -0.25


Example 13:
result = a + b * c > 10 and a & b | c == 2

Step 1: Operator precedence
Python precedence (highest → lowest for operators in this expression):

* (multiplication)
+ (addition)
> (comparison)
& (bitwise AND)
| (bitwise OR)
== (comparison)
and (logical AND)

So the expression is interpreted as:
'''
a, b, c = 5, 3, 2
result = ((a + (b * c)) > 10) and (((a & b) | c) == 2)
print(result)
'''
Step 2: Evaluate arithmetic first

b * c = 3 * 2 = 6
a + (b * c) = 5 + 6 = 11
11 > 10 → True
Left side of and → True

Step 3: Evaluate bitwise operations

a & b = 5 & 3
# 5 = 0b101
# 3 = 0b011
# 0b101 & 0b011 = 0b001 = 1

(a & b) | c = 1 | 2
# 1 = 0b001
# 2 = 0b010
# 0b001 | 0b010 = 0b011 = 3

(a & b) | c == 2 → 3 == 2 → False
Right side of and → False

Step 4: Evaluate logical AND

True and False → False

Final Answer: result = False


Operators with Right-to-Left Associativity in Python:-
Exponentiation → **
Unary operators → +x, -x, ~x
Logical NOT → not
Conditional expression → x if cond else y
Assignment operators → =, +=, -=, etc.

Examples:

# Exponentiation (**) → right to left
exp_result = 2 ** 3 ** 2   # 2 ** (3 ** 2) = 2 ** 9 = 512

# Unary operators (+, -, ~) → right to left
unary_result = -~+5        # - (~(+5)) → -(~5) = -( -6 ) = 6

# Logical NOT → right to left
not_result = not not False # not (not False) = not True = False

# Assignment (=) → right to left
x = y = z = 7  # z=7 → y=z → x=y → all 7

print("Exponentiation:", exp_result) # Exponentiation: 512
print("Unary:", unary_result)		# Unary: 6
print("Logical NOT:", not_result) # Logical NOT: False
print("Assignment:", x, y, z) # Assignment: 7 7 7


# Conditional expression (if-else) → right to left
a, b, c = 5, 10, 20
cond_result = a if a > b else b if b > c else c  # grouped right-to-left → result = 20

Step 1: Understand right-to-left associativity
The conditional expression (ternary operator) in Python:

x if condition else y
has right-to-left associativity, which means that when you chain them like this:

a if a > b else b if b > c else c
Python interprets it as:

a if a > b else (b if b > c else c)
Not as (a if a > b else b) if b > c else c

Step 2: Evaluate the first condition
a > b → 5 > 10 → False
Since the first condition is False, Python moves to the else part, which is:
b if b > c else c

Step 3: Evaluate the right-hand conditional
b > c → 10 > 20 → False
Since this condition is also False, the else part is chosen:
c → 20

Step 4: Assign the result
cond_result = 20

Step 5: Output
print(cond_result)  # 20

# In Python, Comma is the tuple-making operator/separator in expressions, while parentheses merely group the expression.
x = 1, 2, 3       # tuple
x = (1, 2, 3)     # tuple
x = (1)            # integer
x = (1,)           # tuple

x = 1 + 2, 3 * 4
print(x)
#Output: (3, 12)

x = 10, 20 + 30, 40 * 2
print(x)
#Output: (10, 50, 80)
'''
