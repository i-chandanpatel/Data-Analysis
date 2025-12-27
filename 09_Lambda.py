# A lambda expression is a small anonymous function written in one line.

# Normal code
# def add(a, b):
#     return a + b
# print(add(10, 20))

# Using lambda
# Syntax- lambda args : expression
# As lambda expression is anonymous function need to store it in a variable and with the help of that variable we are able to call it
add = lambda a, b: a + b
print(add(10, 20))