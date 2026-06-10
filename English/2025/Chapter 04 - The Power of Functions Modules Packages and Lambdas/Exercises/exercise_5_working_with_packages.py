# Exercise 5: Working with Packages
#
# This exercise demonstrates Python packages. To run it, create
# the following folder structure:
#
#   mypackage/
#       __init__.py
#       module1.py
#       module2.py
#   main.py
#
# The code for each file is provided below. You can also find
# the individual files in the exercise_5_package/ subfolder.

# --- mypackage/__init__.py ---
# (this file can be empty)

# --- mypackage/module1.py ---
def greet(name):
    return f"Hello, {name}!"

# --- mypackage/module2.py ---
def farewell(name):
    return f"Goodbye, {name}!"

# --- main.py ---
from mypackage.module1 import greet
from mypackage.module2 import farewell

print(greet("Alice"))      # Hello, Alice!
print(farewell("Alice"))   # Goodbye, Alice!
