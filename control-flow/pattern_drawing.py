# pattern_drawing.py

# Prompt the user for the pattern size
user_input = input("Enter the size of the pattern: ")

# Check if the input is a valid positive integer
if user_input.isdigit() and int(user_input) > 0:
    size = int(user_input)
    
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1
else:
    print("Please enter a valid positive integer.")
