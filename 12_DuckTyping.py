"""
===========================================================
PYTHON CONCEPT NOTES
Topic: Polymorphism & Duck Typing
===========================================================

Python is dynamically typed. Instead of worrying about the exact type of an object, Python focuses on behavior.

Two important ideas emerge from this philosophy:

1️⃣ Polymorphism
2️⃣ Duck Typing
"""
# ---------------------------------------------------------
# 1️⃣ POLYMORPHISM
# ---------------------------------------------------------
"""
Polymorphism means:

👉 Same function / method name
👉 Works differently depending on the object

"Poly" = many
"Morph" = forms

So it literally means:
ONE INTERFACE → MANY BEHAVIORS
"""

# Example 1: Polymorphism with built-in functions

print(len("Denver"))        # String length
print(len([1,2,3,4]))       # List length
print(len({"a":1,"b":2}))   # Dictionary length

"""
Same function → len()
Different objects → string, list, dictionary

But Python handles each differently.
That is polymorphism.
"""


# Example 2: Polymorphism with classes

class Dog:
    def speak(self):
        return "Dog barks"


class Cat:
    def speak(self):
        return "Cat meows"


class Bird:
    def speak(self):
        return "Bird chirps"


animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(animal.speak())

"""
Even though the objects are different,
they all respond to the same method: speak()
"""


# ---------------------------------------------------------
# 2️⃣ DUCK TYPING
# ---------------------------------------------------------
"""
Duck typing comes from a famous idea:

"If it walks like a duck and quacks like a duck, then it is probably a duck."

Python doesn't care about the object's type. It only cares if the object has the required method.
"""

# Example of Duck Typing

class Laptop:
    def code(self):
        print("Coding on laptop")


class Tablet:
    def code(self):
        print("Coding on tablet")


class Phone:
    def code(self):
        print("Coding on phone")


def start_coding(device):
    device.code()   # Python only checks if 'code()' exists


start_coding(Laptop())
start_coding(Tablet())
start_coding(Phone())

"""
Notice something interesting:

start_coding() never checks:
type(device)

It only calls:
device.code()

If the object has that method → it works.

This is Duck Typing.
"""


"""
===========================================================
DUCK TYPING WITH TYPE HINTS
===========================================================

Even if we specify a type hint for a function parameter, Python will still allow other objects to work as long as they have the required method.

Type hints are NOT strict type enforcement in Python.
They are mainly for readability and tools like linters.
"""



# Notice the type hint here 👇
def start_coding2(device: Laptop):
    device.code()


# Calling the function with different objects
start_coding2(Laptop())
start_coding2(Tablet())
start_coding2(Phone())