# AI FOR EVERYDAY LIFE
# simple simulation

def budgeting_assistant():
    print("\n--- Budgeting Assistant ---")

    money = float(input("How much money do you have? "))

    expenses = []
    number = int(input("How many expenses do you have? "))

    for i in range(number):
        expense = float(input("Enter expense: "))
        expenses.append(expense)

    total = 0

    for expense in expenses:
        total = total + expense

    remaining = money - total

    print("Total expenses:", total)
    print("Money remaining:", remaining)

    if remaining >= 0:
        print("You are within your budget.")
    else:
        print("You have spent more than your budget.")


def study_companion():
    print("\n--- Study Companion ---")

    subjects = ["Python", "Math", "English", "Computer Science"]

    subject = input("What subject do you want to study? ")

    if subject in subjects:
        print("You can study", subject)
        topic = input("Enter the topic you want to study: ")
        print("Your study topic is:", topic)
        print("Study for 30 minutes and take a short break.")
    else:
        print("That subject is not in your study list.")


def productivity_planner():
    print("\n--- Productivity Planner ---")

    tasks = []

    number = int(input("How many tasks do you have? "))

    for i in range(number):
        task = input("Enter a task: ")
        tasks.append(task)

    if len(tasks) == 0:
        print("You have no tasks.")
    else:
        print("\nYour tasks are:")

        for task in tasks:
            print("-", task)


def wellness_guide():
    print("\n--- Wellness Guide ---")

    feeling = input("How are you feeling today? ")

    if feeling == "good":
        print("Great! Keep up your healthy routine.")
    else:
        print("You could take a short break, drink some water, or get some rest.")


# MAIN PROGRAM

print("AI FOR EVERYDAY LIFE")
print("1. Budgeting Assistant")
print("2. Study Companion")
print("3. Productivity Planner")
print("4. Wellness Guide")

choice = input("Choose an option: ")

if choice == "1":
    budgeting_assistant()

elif choice == "2":
    study_companion()

elif choice == "3":
    productivity_planner()

elif choice == "4":
    wellness_guide()

else:
    print("Invalid choice.")

print("\nProgram finished.")
