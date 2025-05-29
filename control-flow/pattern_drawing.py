# pattern_drawing.py

# Ask the user to enter the size of the pattern
user_input = input("Enter the size of the pattern: ")

# Check if the input is a valid positive integer
if user_input.isdigit() and int(user_input) > 0:
    size = int(user_input)
    row = 0

    # Use a while loop to go through each row
    while row < size:
        # Use a for loop to print each asterisk in the row
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1
else:
    print("Please enter a valid positive integer.")
