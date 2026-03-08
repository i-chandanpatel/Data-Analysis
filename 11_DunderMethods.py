a + b  →  a.__add__(b)
print(a) → a.__str__()
"""
===========================================================
FILE: dunder_add_str_demo.py
Concept: __add__ and __str__ special methods
===========================================================

Dunder = Double underscore methods.

These methods allow Python objects to interact
with built-in operations like:

+  → addition
print() → string representation
"""

# ---------------------------------------------------------
# 1️⃣ CLASS WITHOUT DUNDER METHODS
# ---------------------------------------------------------

class NumberBox:
    def __init__(self, value):
        self.value = value


# Creating objects
n1 = NumberBox(10)
n2 = NumberBox(20)

print("Objects without __str__:")
print(n1)
print(n2)

"""
Output will look like something like:

<__main__.NumberBox object at 0x000001A34F8>

Python prints the memory address because
we did not define how the object should appear.
"""


# ---------------------------------------------------------
# 2️⃣ CLASS WITH __str__ METHOD
# ---------------------------------------------------------

class PrettyNumberBox:
    def __init__(self, value):
        self.value = value

    # __str__ controls how object prints
    def __str__(self):
        return f"NumberBox value = {self.value}"


a = PrettyNumberBox(10)
b = PrettyNumberBox(20)

print("\nObjects WITH __str__:")
print(a)
print(b)

"""
Now Python prints a readable message instead
of a memory address.
"""


# ---------------------------------------------------------
# 3️⃣ CLASS WITH __add__ METHOD
# ---------------------------------------------------------

class AddableNumberBox:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"NumberBox({self.value})"

    # __add__ defines behaviour of +
    def __add__(self, other):
        return AddableNumberBox(self.value + other.value)


x = AddableNumberBox(5)
y = AddableNumberBox(15)

print("\nObjects WITH __add__:")
result = x + y

print("x =", x)
print("y =", y)
print("x + y =", result)


"""
Behind the scenes:

x + y

Python internally calls:

x.__add__(y)

and returns a new object.
"""