# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))


# Print a square pattern of asterisks
for row in range(size):
    print("*" * size)
else:
    print("Please enter a valid positive number.")

