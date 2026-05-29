from grading_system import choose_grading_system, add_grading_system, edit_grading_system, delete_grading_system
from marks import choose_marks_menu

def main():
    while True:
        print("\nMenu:")
        print("1. Grading Systems")
        print("2. Marks")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            print("\nGrading Systems Menu:")
            print("1. Choose Grading System")
            print("2. Add Grading System")
            print("3. Edit Grading System")
            print("4. Delete Grading System")
            print("5. Back to Main Menu")

            grading_choice = input("Choose an option: ")
            if grading_choice == "1":
                choose_grading_system()
            elif grading_choice == "2":
                add_grading_system()
            elif grading_choice == "3":
                edit_grading_system()
            elif grading_choice == "4":
                delete_grading_system()
            elif grading_choice == "5":
                continue
            else:
                print("Invalid choice. Please try again.")
        elif choice == "2":
            choose_marks_menu()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break