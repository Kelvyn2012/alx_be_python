# daily_reminder.py

# Ask the user for a task
task = input("Enter your task: ")

# Ask for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level. Please review it."

# Use if to check time sensitivity and adjust the message
if time_bound == "yes" and priority in ("high", "medium", "low"):
    message += " that requires immediate attention today!"
elif priority in ("high", "medium", "low"):
    message += ". Consider completing it soon."

# Print the final reminder
print(message)
