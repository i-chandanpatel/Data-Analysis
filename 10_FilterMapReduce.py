from functools import reduce

# Original list
numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Step 2: Double each even number
doubled_numbers = list(map(lambda x: x * 2, even_numbers))

# Step 3: Reduce to sum
total_sum = reduce(lambda a, b: a + b, doubled_numbers)

print("Even numbers:", even_numbers)
print("Doubled numbers:", doubled_numbers)
print("Final sum:", total_sum)

