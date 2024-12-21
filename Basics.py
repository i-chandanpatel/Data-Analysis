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


#Arithmetic Operators: "+", "-", "/", "*", "%", Power: "**"
#Comparision Operators: "<", ">", "<=", ">=", "!=", "=="
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
print("Binary of 15 is ", bin(10))

#AND "&" Operator:
    #Works in binary form
     #  0 0 = 0
     #  1 0 = 0
     #  0 1 = 0
     #  1 1 = 1
print("15 & 10: ", 15&10)

#OR "|" Operator:
    #Works in binary form
     #  0 0 = 0
     #  1 0 = 1
     #  0 1 = 1
     #  1 1 = 1
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

#Shorthand
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
a="Hello this is python code. {}"
print("Len :",len(a))
print("Count :",a.count("o"))
print("Upper :", a.upper())
print("Lower :",a.lower())
print("Find: ",a.find("t",8))
print("Capitalize: ",a.capitalize())
print("Casefold: ",a.casefold())
b="This is Denver"
print("Formate: ",a.format(b))
print("Center :",a.center(10,"*"))
c=12
print("Is Integer :",c.is_integer())
print("Is digit :",str(c).isdigit())     #isdigit is a string function not work on integer datatype

c="12"
print(c.isnumeric())

print("Starts with: ", a.startswith("Hello"))
print("Ends with: ",a.endswith("{}"))
a="          He$lo "
print("Strip: ",a.strip())
print("Split: ",a.split("$"))

print("ljust: ",a.strip().ljust(20,"*"))
print("rjust: ",a.strip().rjust(20,"*"))
a=a.replace("$","l")
print("Replace: ",a)
print("index: ",a.index("l"))
print("rindex: ",a.rindex("l"))


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


#Dictionary
print("\n\n Dictionary \n\n")
dict={"birth_year":2003, "roll-num":20}

print(type(dict))
print("Keys: ",dict.keys())
print("Values: ",dict.values())
print("Both values: ",dict.items())
print("Roll num using Get function ",dict.get("roll-num"))
print("setdefault: if key exist than returns val from dictionary if not, than provided value*(Denver): ",dict.setdefault("Name","Denver"))
dict.update({"roll-num": 27,"Number": 4254627})
print("Update: ",dict)
print("Popped: ",dict.pop("Number"))
print("Popitem: ",dict.popitem())
print("Clear: ",dict.clear())


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