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

