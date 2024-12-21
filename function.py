### Basic Get Student
def get_student():
    name = input("Name: ")
    home = input("Home: ")
    return name, home

def main():
    name, home = get_student()
    print(f"{name} from {home}")

# - **Purpose**: This basic version collects a student's name and home, then prints it.
# - **Function `get_student()`**: Prompts the user for their name and home, then returns these values as a tuple.
# - **Function `main()`**: Calls `get_student()`, unpacks the returned tuple, and prints the values.

### Get Student Using Tuple
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    home = input("Home: ")
    return (name, home)

# - **Purpose**: Similar to the basic version but explicitly uses a tuple to store the student's name and home.
# - **Function `get_student()`**: Returns a tuple containing the name and home.
# - **Function `main()`**: Calls `get_student()`, accesses the tuple elements using indices, and prints them.

### Get Student Using List
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    home = input("Home: ")
    return [name, home]

# - **Purpose**: Uses a list instead of a tuple to store the student's name and home.
# - **Function `get_student()`**: Returns a list containing the name and home.
# - **Function `main()`**: Calls `get_student()`, accesses the list elements using indices, and prints them.

### Get Student Using Dictionary
def main():
    student = get_student()
    print(f'{student["name"]} from {student["home"]}')

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["home"] = input("Home: ")
    return student

# - **Purpose**: Uses a dictionary to store the student's name and home, making it more readable and flexible.
# - **Function `get_student()`**: Creates a dictionary with keys "name" and "home", and returns it.
# - **Function `main()`**: Calls `get_student()`, accesses the dictionary values using keys, and prints them.


### Conditional Execution
if __name__ == "__main__":
    main()

# - **Purpose**: Ensures that the `main()` function is only executed when the script is run directly, not when it is imported as a module in another script.
# - **Explanation**: The condition `if __name__ == "__main__":` checks if the script is being run directly. If true, it calls the `main()` function.

### Summary
# - **Modular Code**: The conditional execution ensures that the `main()` function runs only when intended, making the code modular and reusable.
