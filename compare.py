"""
This program takes two numbers as user input and compares them to see if 'a' is less than, more than or equal to 'b'
"""

# Compare function compares two number and returns result.
def compare(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    elif a > b:
        return 1

# Compare test values and print results
print(compare(5, 2))
print(compare(2, 5))
print(compare(3, 3))

# Get user input (two numbers) and compare them then print results to screen.
print(compare(input("Enter first number: "), input("Enter second number: ")))
