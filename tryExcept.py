try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("Something not :", e)

finally:
    print("Program Done.")