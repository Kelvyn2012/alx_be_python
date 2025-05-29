# Ask the user for a task and clean the input
task = input("Enter your task: ").strip().lower()

# Ask for the task's priority level and clean the input
priority_level = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound and clean the input
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Match based on the priority level
match priority_level:
    case "high":
        # If task is time-sensitive
        if time_bound == "yes":
            print(f"🚨 Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"📌 Reminder: '{task}' is a HIGH priority task. Try to complete it as soon as possible.")

    case "medium":
        if time_bound == "yes":
            print(f"⏳ Reminder: '{task}' is a MEDIUM priority task that needs attention today.")
        else:
            print(f"📝 Reminder: '{task}' is a MEDIUM priority task. Plan to complete it soon.")

    case "low":
        if time_bound == "yes":
            print(f"📅 Reminder: '{task}' is a LOW priority task, but it’s time-sensitive. Don’t forget it today!")
        else:
            print(f"📖 Note: '{task}' is a LOW priority task. Consider doing it when you have extra time.")

    case _:
        # Handles anything that’s not high/medium/low
        print(f"⚠️ '{task}' has an unknown priority level. Please check your input.")
