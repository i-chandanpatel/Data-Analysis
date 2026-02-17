#Input methods
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=(float(input("Enter your height: ")))


#Output methods
print(f"Name: {name}, Age: {age}, Height: {height}")
print("Name: ", name, " Age: ", age, "Height: ", height)
print("Name: "+ name+ " Age: "+ str(age)+ " Height: "+ str(height))


#Typecasting
age2=str(age)
print("Type of age ",type(age))
print("Type of age2 ",type(age2))


#Swapping
a=1
b=2

print("Before swap")
print("a ",a)
print("b ",b)

a,b=b,a

print("After swap")
print("a ",a)
print("b ",b)


#Arithmetic Operators: "+", "-", "/",Floor Division "//", "*", "%", Power: "**"
#Comparision Operators: "<", ">", "<=", ">=", "!=", "=="
#Internelly if compared than the String will be compared using ASCII code but we can't compare String with a number
#Logical Operators: and, or, not
#Assignment Operators: "=", "+=", "-=", "*=", "/="

#Identity Operators: Check the memory address of two objects. Check weather two variable refer to same object.
a=[1,2,3]
b=a
c=[1,2,3]

print("a is b ",a is b)
print("a is c ",a is c)
print("a is not c ",a is not c)

#Bitwise Operators
print("Binary of 15 is ", bin(15))
print("Binary of 10 is ", bin(10))

#AND "&" Operator
print("15 & 10: ", 15&10)

#OR "|" Operator
print("15 | 10: ", 15|10)

#XOR "^" Operator:
    #Works in binary form
     #  0 0 = 0
     #  1 0 = 1
     #  0 1 = 1
     #  1 1 = 0
print("15 ^ 10: ", 15^10)

#Left shift(<<): Shifts all bits to the left to the specified number. New bits on right filled with 0. Simply each shift is multiplication by 2 of the number.
print(bin(15))
print("15 Left shifted by 2: ", bin(15<<2))

#Right shift(>>): Shifts all bits to the left to the specified number. New bits on left filled with 0. Simply each shift is division by 2 of the number.
print(bin(15))
print("15 Right shifted by 2: ", bin(15>>2))


#Conditional Statements
c=5

#if-else
if(c>4):
    print(True)
else:
    print(False)

#if-elif-else
if(c>5):
    print("Greator")
elif(c<5):
    print("Lessor")
else:
    print("c==5")

#Shorthand if-else
print("Greator than 4") if c>4 else print("Less than 4")

#Loops

#for loop

for i in range(10):
    if(i==5):
        continue      #Skips the loop when i==5
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in range(1,11):
    print(f"7 X {i}: {7*i}")

#while loop
a=1
while(a<10):
    print(a)
    if(a==4):
        break       #Breaks the loop when a==4
    a+=1


#Strings

a = "Hello this is python code. {}"  
print("Len :", len(a))  
print("Count :", a.count("o"))  
print("Upper :", a.upper())
print("Lower :", a.lower())

print("Find: ", a.find("t", 8)) #find first 't' starting from index 8
# returns index position, -1 if not found

print("Capitalize: ", a.capitalize())  
# capitalize() → makes first character uppercase, rest lowercase

print("Casefold: ", a.casefold())  
# casefold() → aggressive lowercase (used for comparisons)
# Output: hello this is python code. {}

b = "This is Denver"
print("Format: ", a.format(b))  
# format(b) → replaces {} with value of b

print("Center :", a.center(10, "*"))  
# center(width, fillchar) → centers string in given width
# No change because width < string length
# Output: Hello this is python code. {}

c = "Python"
print("Center :", c.center(20, "*"))
# center(20, "*") → makes total length = 20
# adds '*' equally on left and right
# Output: ******Python*******

c = 12
# print(c.is_integer())  ❌ ERROR (int has no is_integer method)

print("Is digit :", str(c).isdigit())  
# isdigit() → checks if all characters are digits
# c is converted to string first
# Output: True


c = "12"
print(c.isnumeric())  
# isnumeric() → checks if string contains all numeric characters
# Output: True

print("Starts with: ", a.startswith("Hello"))
print("Ends with: ",a.endswith("{}"))


a = "          He$lo "
print("Strip: ", a.strip())  
# strip() → removes leading & trailing spaces only
# Output: He$lo

print("Split: ", a.split("$"))  
# split("$") → splits string into list using $ as separator
# Output: ['          He', 'lo ']

print("ljust: ", a.strip().ljust(20, "*"))  
# ljust(width, fillchar) → left-aligns string, fills right side
# Output: He$lo***************

print("rjust: ", a.strip().rjust(20, "*"))  
# rjust(width, fillchar) → right-aligns string, fills left side
# Output: ***************He$lo

a = a.replace("$", "l")  
# replace("$","l") → replaces $ with l

print("Replace: ", a)  
# Output:            Hello 


print("index: ", a.index("l"))  
# index("l") → returns first index of 'l'
# raises error if character not found
# Output: 12


print("rindex: ", a.rindex("l"))  
# rindex("l") → returns last index of 'l'
# Output: 14


g = "1.234"

# isalnum - Returns True if all characters in the string are alphanumeric
print(f"isalnum: {g.isalnum()}") 

# isalpha - Returns True if all characters in the string are in the alphabet
print(f"isalpha: {g.isalpha()}")

# isdecimal - Returns True if all characters in the string are decimals
print(f"isdecimal: {g.isdecimal()}")

# isdigit - Returns True if all characters in the string are digits
print(f"isdigit: {g.isdigit()}")

# isnumeric - Returns True if all characters in the string are numeric
print(f"isnumeric: {g.isnumeric()}")

# islower - Returns True if all cased characters in the string are lowercase
# (Note: The original image comment said 'converts', but .islower() is a check)
print(f"islower: {g.islower()}")

# isupper - Returns True if all characters in the string are upper case
print(f"isupper: {g.isupper()}")

# isspace - Returns True if all characters in the string are whitespaces
print(f"isspace: {g.isspace()}")

# istitle - Returns True if the string follows the rules of a title
print(f"istitle: {g.istitle()}")



#Lists
print("\n\n Lists \n\n")
a=["Hulk","Denver","Professor","Berlin","Hulk"]
print("Len :",len(a))
print("Count :",a.count("Hulk"))
print("Append: ",a.append("Spiderman"))
print("Insert: ",a.insert(1,"Vision"))
print("Remove: ",a.remove("Hulk"))
# print("Pop: ",a.pop("Denver"))
b=[]
b=a.copy()
print("Copy :",b)
b.append("Doremon")
print("Index: ", a.index("Berlin"))
print("Extend: ",a.extend(b))
print("Reverse: ",a.reverse())
print("Sort: ",a.sort())
[print(i) for i in a]    #Shorthand for loop
a.clear()


#Tuples
print("\n\n Tuples \n\n")
a="Denver",     #Comma is necessory formaking single value tuple
b="Den"         #otherwise it will be a string
print(type(a))
print(type(b))

d=("Abc","Def","Ghi","Jkl","Mno","Pqr","Stu","Abc")
print("Slicing",d[1:4])
print("Slicing",d[::2])

print("Type before conversion",type(d))
d=list(d)
print("Type after conversion",type(d))
d=tuple(d)
print("Converting back to tuple ",type(d))

print("Count", d.count("Abc"))
print("Len",len(d))


# Dictionary in Python

print("\n\n Dictionary \n\n")
student = {
    "birth_year": 2003,
    "roll-num": 20
}
print(type(student))           # <class 'dict'>
print("Keys:", student.keys())
print("Values:", student.values())
print("Both values:",student.items())

# get() → safely fetches value using key
# If key doesn't exist, it returns None instead of error
print("Roll num using get():", student.get("roll-num"))

# setdefault(key, value)
# If key EXISTS → returns existing value
# If not→insert key with given value
print(
    "setdefault():",   student.setdefault("Name","Denver"))

# Dictionary now contains "Name"
print("After setdefault:", student)

# update() → modifies existing keys OR adds new ones
student.update({
    "roll-num": 27,      # existing key → value updated
    "Number": 4254627    # new key → added
})

print("After update:", student)

# pop(key) → removes key and returns its value
print("Popped value:", student.pop("Number"))

print("After pop:", student)

# popitem() → removes and returns LAST inserted key-value pair
print("Popitem:", student.popitem())
print("After popitem:", student)
student.clear()
print("After clear:", student)

student[10]=300;  #Change value for the key, but if not present already than add it with the value 

print(student)

del student[10] # Deletes specified key and its value 
#Sets
print("\n\n Sets \n\n")
a={"Captain America", "Hulk", "Thor"}

print("\nAdds at random place ",a.add("Spiderman"))
print("\nPops out random value ",a.pop())
# a.remove("Thor")    #a.dicard("Thor")   pop() removes random value if it removed "Thor" already this line will through error
print("\nRemove particular value ",a)

b=a.copy()
print("\nIs a and b contains atleast 1 different element ",a.isdisjoint(b))
b.add("Iron Man")
print("\nIs all elements of a present in b ",a.issubset(b))
print("\nIs b is superset of a ",b.issuperset(a))

print("\n a before update ",a)
a.update(b)
print("\n a after update ",a)
a.clear()
b.clear()
print("\nClear removes all elements ",a)

a={"Iron Man","Shaktiman", "Superman"}
b={"Hulk","Thor","Spiderman"}

print("\nUnion returns new set: ",a.union(b))

print("\nDifference returns new set: ",a.difference(b))     #symmetric_difference() works same

# a.difference_update(b)        #symmetric_difference_update() works same
# print("\ndifference_update removes all matched elements in a from b and updates a: ",a)   

a.add("Spiderman")
a.intersection_update(b)
print("\nintersection_update only left all matched elements in a from b and updates a : ",a)


#Find common elements in list using set
a=[1,2,3]
b=[2,3,4]

print("Common elemets: ",set(a) & set(b))
