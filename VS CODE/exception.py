# x = int(input("Enter the Number: "))
# y = int(input("Enter the number: "))
# try:
#     z = x / y
#     print("The result is:", z)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter numeric values.")
# except Exception as e:
#     print("Error:", e)
#     print("An unexpected error occurred.")
# finally:
#     print("Execution completed.")

# print("This is the end of the program.")

x = int(input("Enter the Number: "))
y = int(input("Enter the number: "))
try:
    z = x / y
    print("The result is:", z)
except Exception as e:
    print("Error:", e.__class__)
    print("An unexpected error occurred.")
finally:
    print("Execution completed.")

print("This is the end of the program.")


