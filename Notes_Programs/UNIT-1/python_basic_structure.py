"""
Program to demonstrate basic structure of a Python script without using classes.

This file includes:
    - Comments (single-line and multi-line)
    - Constants (defined at top in UPPERCASE)
    - Imports
    - Global variables
    - Functions
    - Local variables
    - Main execution block
    - Sample output at the end
"""

# ---------------------------------------------------------
# IMPORT STATEMENTS
# ---------------------------------------------------------
import math                     # Standard math module
from datetime import datetime   # Import datetime class

# ---------------------------------------------------------
# CONSTANTS (always written in UPPERCASE)
# ---------------------------------------------------------
PI = 3.14159     # Mathematical constant value for π

# ---------------------------------------------------------
# GLOBAL VARIABLES (accessible throughout the file)
# ---------------------------------------------------------
global_variable = 10    # Global variable used inside and outside functions


# ---------------------------------------------------------
# FUNCTION DEFINITIONS
# ---------------------------------------------------------
def area_of_circle(radius):
    """
    Function to calculate the area of a circle.
    Demonstrates local variables inside functions.
    """
    area = PI * radius * radius   # Local variable (only inside this function)
    return area


# ---------------------------------------------------------
# CODE EXECUTED BEFORE MAIN BLOCK (NOT RECOMMENDED USUALLY)
# ---------------------------------------------------------
area = area_of_circle(global_variable)
print("Area using global_variable (10):", area)   # Demonstration print


# ---------------------------------------------------------
# MAIN PROGRAM EXECUTION BLOCK
# ---------------------------------------------------------
if __name__ == "__main__":

    # Local variable inside main block
    r = 7
    print("\n--- Inside Main Block ---")
    print("Radius:", r)
    print("Area of circle:", area_of_circle(r))

    # Modifying global variable inside main program
    global_variable = 'A'
    print("Modified global_variable:", global_variable)

    # Using imported module (datetime)
    print("Current Year:", datetime.now().year)


# ---------------------------------------------------------
# SAMPLE OUTPUT (REFERENCE ONLY – NOT EXECUTED BY PYTHON)
# ---------------------------------------------------------
"""
==================== SAMPLE OUTPUT ====================

Area using global_variable (10): 314.159

--- Inside Main Block ---
Radius: 7
Area of circle: 153.93751
Modified global_variable: A
Current Year: 2025

========================================================
"""
