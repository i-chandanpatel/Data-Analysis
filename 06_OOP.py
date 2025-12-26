# 1️⃣ BASIC CLASS CREATION
# A class is a blueprint.
# It does NOTHING until an object is created.

class Student:
    pass    # pass means "empty for now"


# Creating an object of Student
s1 = Student()
# At this stage:
# • Student has no data
# • Student has no behavior


# 2️⃣ INSTANCE ATTRIBUTES (Object Data)

# Instance attributes belong to the OBJECT, not the class

s1.name = "Denver"
s1.age = 22

# Each object can have different data
s2 = Student()
s2.name = "Amit"
s2.age = 21



# 3️⃣ CONSTRUCTOR (__init__)

# Constructor automatically runs when object is created
# Used to initialize object data properly

class Person:
    def __init__(self, name, age):
        # self refers to the current object
        self.name = name
        self.age = age


p1 = Person("Denver", 22)
p2 = Person("Amit", 21)



# 4️⃣ INSTANCE METHODS

# Instance methods work with object data
# They ALWAYS take self as first parameter

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        # Accessing instance attributes using self
        print("Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Denver", 60000)
emp1.show_details()



# 5️⃣ CLASS ATTRIBUTES

# Class attributes are SHARED by all objects

class CompanyEmployee:
    company_name = "TechCorp"   # class attribute

    def __init__(self, name):
        self.name = name        # instance attribute

    def show(self):
        print("Name:", self.name)
        print("Company:", CompanyEmployee.company_name)


e1 = CompanyEmployee("Denver")
e2 = CompanyEmployee("Amit")

e1.show()
e2.show()



# 6️⃣ CLASS METHODS

# Class methods modify class-level data
# They use cls instead of self

class OfficeEmployee:
    company = "TechCorp"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


OfficeEmployee.change_company("NextGenSoft")
print("Updated Company:", OfficeEmployee.company)



# 7️⃣ STATIC METHODS
# Static methods:
# • Do NOT use self
# • Do NOT use cls
# • Utility/helper functions

class SalaryUtils:
    @staticmethod
    def is_high_salary(amount):
        return amount > 50000


print(SalaryUtils.is_high_salary(60000))



# 8️⃣ INHERITANCE (SINGLE)
=
# Child class gets features of Parent class

class Parent:
    def parent_method(self):
        print("This is parent method")


class Child(Parent):
    def child_method(self):
        print("This is child method")


c = Child()
c.parent_method()
c.child_method()



# 9️⃣ USING PARENT CONSTRUCTOR

# Child class can reuse parent's constructor

class BaseEmployee:
    def __init__(self, name):
        self.name = name


class Developer(BaseEmployee):
    def __init__(self, name, language):
        super().__init__(name)   # calling parent constructor
        self.language = language


dev = Developer("Denver", "Python")
print(dev.name, dev.language)



# 🔟 POLYMORPHISM (Method Overriding)

# Same method name, different behavior

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.sound()
d.sound()



# 1️⃣1️⃣ super() KEYWORD

# super() is used to call parent methods

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive")


car = Car()
car.start()



# 1️⃣2️⃣ ENCAPSULATION: Data protection


class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount()
acc.deposit(5000)
print("Balance:", acc.get_balance())



# 1️⃣3️⃣ MULTILEVEL INHERITANCE

class A:
    def show_a(self):
        print("Class A")


class B(A):
    def show_b(self):
        print("Class B")


class C(B):
    def show_c(self):
        print("Class C")


obj = C()
obj.show_a()
obj.show_b()
obj.show_c()



# 1️⃣4️⃣ ABSTRACTION (ADVANCED – LAST)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        print("Area = length * breadth")


r = Rectangle()
r.area()

