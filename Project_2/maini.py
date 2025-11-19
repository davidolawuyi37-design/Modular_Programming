from score_utilis import add_score, remove_score, display_scores
from math_utilis import average_scores

def menu():
    print("\n--- SCORE MANAGER ---")
    print("1. Add Score")
    print("2. Remove Score")
    print("3. Display Scores")
    print("4. Average Score")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        value = int(input("Enter score to add: "))
        print(add_score(value))

    elif choice == "2":
        value = int(input("Enter score to remove: "))
        print(remove_score(value))

    elif choice == "3":
        print(display_scores())

    elif choice == "4":
        print("Average:", average_scores())

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
