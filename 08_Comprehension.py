# Ternery Operator
a = 10
b = 20

# if a > b:
#     max_value = a
# else:
#     max_value = b
# print(max_value)

# Same code with Ternery
max_value = a if a > b else b
print(max_value)



# LIST COMPREHENSION
# Create a list of squares of numbers from 1 to 5

list_comp = [i * i for i in range(1, 6)]
print("List Comprehension:", list_comp)
# Output → [1, 4, 9, 16, 25]



# DICTIONARY COMPREHENSION
# Create a dictionary where:
# key   = number
# value = square of number

dict_comp = {i: i * i for i in range(1, 6)}
print("Dictionary Comprehension:", dict_comp)
# Output → {1: 1, 4: 16, 2: 4, 3: 9, 5: 25}



# SET COMPREHENSION
# Create a set of squares (unique values only)

nums = [1, 2, 2, 3, 3, 4, 5]

set_comp = {i * i for i in nums}
print("Set Comprehension:", set_comp)
# Output → {1, 4, 9, 16, 25}