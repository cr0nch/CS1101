"""
This is a basic calculator. It takes two number and an operation from the user, computes them and prints out the results.
"""

# Gets number from user. Completes some 'sanitation' to ensure it is valid.
def get_number(message):
    while True:
        try:
            # Attempt casting user input to int until user enters a valid whole number.
            a = int(input(message))
            # Make sure number is above 0
            if a > 0:
                return a;
            else:
                print("Invalid input. Both numbers must be positive whole numbers and cannot be 0\n")
                # Catch an error if it can't be converted to an int. E.g. if user enters a word or symbols.
        except ValueError:
            print("Invalid input: You must enter a whole number.\n")

# Display welcome message to the user.
print("\nThank you for trying my calculator. This calculator will take two numbers and perform a calculation on them.\n"
      "It can add, subtract, divide and multiply!\n\n"
      "** Both numbers must be positive whole numbers and neither can be 0 **\n")

# Get the first number from the user and convert to int.
a = get_number("Please enter the first number: ")

print("Thank you. The first number is", a)

# Get operation from user.
op = input("What operation would you like to perform?\n"
           "\t1 - Add\n"
           "\t2 - Subtract\n"
           "\t3 - Multiply\n"
           "\t4 - Divide\n"
           "Please enter an option:")

# Check operation is valid
while op != "1" and op != "2" and op != "3" and op != "4":
    print("\nInvalid operation: Please select '1', '2', '3' or '4'.")
    op = input("What operation would you like to perform?\n"
               "\t1 - Add"
               "\t2 - Subtract"
               "\t3 - Multiply"
               "\t4 - Divide\n"
               "Please enter an option:")

    # Get the second number from the user and convert to int.
b = get_number("Please enter the second number: ")

print("\nThank you. Calculating your result...")

# Perform the specified operation on the two numbers and display the results.
if op == "1":
    print(a, "+", b, " = ", a + b)

elif op == "2":
    print(a, "-", b, " = ", a - b)

elif op == "3":
    print(a, "x", b, " = ", a * b)

elif op == "4":
    print(a, "/", b, " = ", a / b)



