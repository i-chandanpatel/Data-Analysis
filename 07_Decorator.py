def decorate(func):
    # 'func' receives the function we want to modify
    # need to pass the parameters in wrapper function 
    def wrapper(a, b):
        # Code that runs BEFORE the original function
        print("The addition of your numbers is:")

        # Call the original function
        func(a, b)

        # Code that runs AFTER the original function
        print("Thank you! I hope you liked it.")

    # Return wrapper function (NOT calling it)
    return wrapper


# Method 1 to decorate a function 
# @decorate
# def addition(a, b):
#     print(f"Your total is {a + b}")

# Method 2
def addition(a, b):
    print(f"Your total is {a + b}")
# Manually decorating the function
addition = decorate(addition)


# Calling the wrapped function
addition(10, 20)



# *args -Use to store multiple arguments. args is not mandatory it can be of any name
def add_numbers(*args):
    # args is a tuple of all passed values
    print("Received arguments:", args)

    total = 0
    for num in args:
        total += num

    return total


# **kwargs - Stores multiple keywords arguments. kwargs not mandatory it can be of any name
def print_details(**kwargs):
    # kwargs is a dictionary
    print("Received keyword arguments:", kwargs)

    for key, value in kwargs.items():
        print(f"{key} : {value}")






def decorate(func):
    def wrapper(*args, **kwargs):
        print("The addition of your numbers is:")
        result = func(*args, **kwargs)
        print("Thank you! I hope you liked it.")
        return result

    return wrapper
