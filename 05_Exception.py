a = int(input("Enter divisor: "))

try:
    # Throwing exception
    if a == 0:
        raise ZeroDivisionError("You cannot divide by zero (raised manually)")

    result = 10 / a
    print("Result:", result)

except ZeroDivisionError as e:
    # Handles division by zero (both real & manually raised)
    print("ZeroDivisionError occurred:", e)

except Exception as e:
    print("Error occurred:", e)

else:
    print("Runs if no error is there")

finally:
    print("Always executes")