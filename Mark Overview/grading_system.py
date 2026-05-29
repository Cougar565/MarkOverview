import os
import json

# This code is responsible for allowing the user to choose a grading system based on country, level, or city. It reads the available grading systems from a JSON file and saves the user's choice for later use in calculations.
current_path = os.path.dirname(os.path.abspath(__file__))
grading_systems_path = f"{current_path}/Data/grading_systems.json"
choices_path = f"{current_path}/Data/choices.json"

with open(grading_systems_path, "r") as grading_systems_file:
    grading_systems = json.load(grading_systems_file)["systems"]
with open(choices_path, "r") as choices_file:
    choices = json.load(choices_file)

def choose_grading_system():
    system_country = input("Enter the country of the grading system: ")
    valid_systems = [system for system in grading_systems if system["country"].lower() == system_country.lower()]
    if not valid_systems:
        print("No grading systems found for the specified country. Defaulting to the first grading system.")
        valid_systems = grading_systems
    for i, system in enumerate(valid_systems):
        print(f"{i + 1}. {system['school']} - {system['grade']} ({system['city']})")
    system_choice = input("Choose a grading system by entering its number or search for a level: ")
    if not system_choice:
        print("PPlease enter value. Defaulting to the first grading system.")
        system_choice = 0
    elif system_choice.isdigit():
        system_choice = int(system_choice) - 1
    else:
        valid_systems = [system for system in valid_systems if system_choice.lower() in system["grade"].lower()]
        if not valid_systems:
            print("No grading systems found for the specified level. Defaulting to the first grading system.")
            system_choice = 0
        for i, system in enumerate(valid_systems):
            if system_choice.lower() in system["grade"].lower():
                print(f"{i + 1}. {system['school']} - {system['grade']} ({system['city']})")
        system_choice = input("Choose a grading system by entering its number or search for a city: ")
        if system_choice.isdigit():
            system_choice = int(system_choice) - 1
        else:
            valid_systems = [system for system in valid_systems if system_choice.lower() in system["city"].lower()]
            if not valid_systems:
                print("No grading systems found for the specified city. Defaulting to the first grading system.")
                system_choice = 0
            for i, system in enumerate(valid_systems):
                if system_choice.lower() in system["city"].lower():
                    print(f"{i + 1}. {system['school']} - {system['grade']} ({system['city']})")
            system_choice = input("Choose a grading system by entering its number: ")
            if system_choice.isdigit():
                system_choice = int(system_choice) - 1
            else:
                print("Invalid choice. Defaulting to the first grading system.")
                system_choice = 0
    if system_choice < 0 or system_choice >= len(valid_systems):
        print("Invalid choice. Defaulting to the first grading system.")
        system_choice = 0
    chosen_system = valid_systems[system_choice]

    choices["chosen_system"] = chosen_system
    
    with open(f"{current_path}/Data/choices.json", "w") as choices_file:
        json.dump(choices, choices_file)

def add_grading_system():
    print("Adding a new grading system is not implemented yet.")

def edit_grading_system():
    print("Editing an existing grading system is not implemented yet.")

def delete_grading_system():
    print("Deleting a grading system is not implemented yet.")