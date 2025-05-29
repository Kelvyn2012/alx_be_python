# Ask the user to enter the task, convert it to lowercase, and remove extra spaces
task = input("Enter your task: ").lower().strip()

# Ask for the priority level, clean it for consistency
priority_level = input("Priority (high/medium/low): ").lower().strip()

# Ask if the task is time-sensitive, clean input
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Use a match-case block to decide the response based on time sensitivity
match time_bound:
    # If the task is time-bound (i.e., urgent)
    case _ if time_bound == "yes":
        print(f"Reminder: {task} is a {priority_level} priority task that requires immediate attention today!")

    # If the task is not time-bound
    case _:
        print(f"{task} is a {priority_level} priority task. Consider completing it when you have free time.")
