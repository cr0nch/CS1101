"""This program prints 9 blank lines by calling a function that prints 3 blank lines three times (3 * 3).
It then calls a function to clear the screen (printing 25 blank lines.
It will print to the screen to let the user now whenthese operations begin and finish.
These operations are displayed for assessment purposes."""


# Returns three newline (blank line) characters.
def three_lines():
    return "\n\n\n"

# Prints nine blank lines by calling three_lines function multiple times.
def nine_lines():
    print("Printing nine blank lines...")
    print(three_lines() * 3, end='') # end='' prevents an extra newline being printed automatically.
    print("... Nine blank lines printed!")

# Prints 25 blank lines. 24 explicitly printed, the 25th line is inserted automatically by the print function.
def clear_screen():
    print("Clearing screen...")
    print("\n" * 24)
    print('... Screen cleared!')

# Call function to print nine blank lines.
nine_lines()

# Call function to clear screen.
clear_screen()