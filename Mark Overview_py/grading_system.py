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
    system_template = {
        "id": len(grading_systems),
        "creator_id": "",
        "country": "",
        "school": "",
        "grade": "",
        "city": "",
        "parameters": {
            "pluspoints": "",
            "double_compensation": "",
            "grading_scale": "",
            "passing_mark": "",
            "subject_rounding": ""
        }
    }
    print("Adding a new grading system.")
    system_template["creator_id"] = choices["user_data"]["id"]
    system_template["country"] = input("Enter the country of the grading system: ")
    system_template["school"] = input("Enter the name of the school: ")
    system_template["grade"] = input("Enter the grade name: ")
    system_template["city"] = input("Enter the city of the grading system: ")
    system_template["parameters"]["pluspoints"] = input("Are there plus points? (yes/no): ")
    if system_template["parameters"]["pluspoints"].lower() == "yes":
        system_template["parameters"]["pluspoints"] = True
        system_template["parameters"]["double_compensation"] = input("Is there double compensation for plus points? (yes/no): ")
        if system_template["parameters"]["double_compensation"].lower() == "yes":
            system_template["parameters"]["double_compensation"] = True
        else:
            system_template["parameters"]["double_compensation"] = False
    else:
        system_template["parameters"]["pluspoints"] = False
        system_template["parameters"]["double_compensation"] = False
    system_template["parameters"]["grading_scale"] = input("Enter the grading scale (e.g., 1-10, A-F): ")
    system_template["parameters"]["passing_mark"] = float(input("Enter the passing mark: "))
    system_template["parameters"]["subject_rounding"] = float(input("Enter the subject rounding policy: "))

    grading_systems.append(system_template)
    with open(grading_systems_path, "w") as grading_systems_file:
        json.dump({"systems": grading_systems}, grading_systems_file)
    
    choose_to_use = input("Do you want to use this grading system now? (yes/no): ")
    if choose_to_use.lower() == "yes":
        choices["chosen_system"] = system_template
        with open(f"{current_path}/Data/choices.json", "w") as choices_file:
            json.dump(choices, choices_file)

def edit_grading_system():
    created_systems = [system for system in grading_systems if system["creator_id"] == choices["user_data"]["id"]]
    if not created_systems:
        print("You have not created any grading systems to edit.")
        return
    for i, system in enumerate(created_systems):
        print(f"{i + 1}. {system['school']} - {system['grade']} ({system['city']})")
    system_choice = input("Choose a grading system to edit by entering its number: ")
    if system_choice.isdigit() and int(system_choice) - 1 < len(created_systems) and int(system_choice) - 1 >= 0:
        system_choice = int(system_choice) - 1
    else:
        print("Invalid choice. Returning to the grading systems menu.")
        return
    system_to_edit = created_systems[system_choice]
    print("Leave a field blank to keep the current value.")
    new_country = input(f"Enter the new country of the grading system (current: {system_to_edit['country']}): ")
    new_school = input(f"Enter the new name of the school (current: {system_to_edit['school']}): ")
    new_grade = input(f"Enter the new grade name (current: {system_to_edit['grade']}): ")
    new_city = input(f"Enter the new city of the grading system (current: {system_to_edit['city']}): ")
    new_pluspoints = input(f"Are there plus points? (current: {'yes' if system_to_edit['parameters']['pluspoints'] else 'no'}): ")
    if new_pluspoints.lower() == "yes":
        system_to_edit["parameters"]["pluspoints"] = True
        new_double_compensation = input(f"Is there double compensation for plus points? (current: {'yes' if system_to_edit['parameters']['double_compensation'] else 'no'}): ")
        if new_double_compensation.lower() == "yes":
            system_to_edit["parameters"]["double_compensation"] = True
        elif new_double_compensation.lower() == "no":
            system_to_edit["parameters"]["double_compensation"] = False
    elif system_to_edit["parameters"]["pluspoints"]:
        system_to_edit["parameters"]["pluspoints"] = True
        new_double_compensation = input(f"Is there double compensation for plus points? (current: {'yes' if system_to_edit['parameters']['double_compensation'] else 'no'}): ")
        if new_double_compensation.lower() == "yes":
            system_to_edit["parameters"]["double_compensation"] = True
        elif new_double_compensation.lower() == "no":
            system_to_edit["parameters"]["double_compensation"] = False
    else:
        system_to_edit["parameters"]["pluspoints"] = False
        system_to_edit["parameters"]["double_compensation"] = False
    new_grading_scale = input(f"Enter the new grading scale (current: {system_to_edit['parameters']['grading_scale']}): ")
    new_passing_mark = float(input(f"Enter the new passing mark (current: {system_to_edit['parameters']['passing_mark']}): "))
    new_subject_rounding = float(input(f"Enter the new subject rounding policy (current: {system_to_edit['parameters']['subject_rounding']}): "))
    
    if new_country:
        system_to_edit["country"] = new_country
    if new_school:
        system_to_edit["school"] = new_school
    if new_grade:
        system_to_edit["grade"] = new_grade
    if new_city:
        system_to_edit["city"] = new_city
    if new_grading_scale:
        system_to_edit["parameters"]["grading_scale"] = new_grading_scale
    if new_passing_mark:
        system_to_edit["parameters"]["passing_mark"] = new_passing_mark
    if new_subject_rounding:
        system_to_edit["parameters"]["subject_rounding"] = new_subject_rounding
    
    with open(grading_systems_path, "w") as grading_systems_file:
        json.dump({"systems": grading_systems}, grading_systems_file)
    
    choose_to_use = input("Do you want to use this grading system now? (yes/no): ")
    if choose_to_use.lower() == "yes":
        choices["chosen_system"] = system_to_edit
        with open(f"{current_path}/Data/choices.json", "w") as choices_file:
            json.dump(choices, choices_file)

def delete_grading_system():
    created_systems = [system for system in grading_systems if system["creator_id"] == choices["user_data"]["id"]]
    if not created_systems:
        print("You have not created any grading systems to delete.")
        return
    for i, system in enumerate(created_systems):
        print(f"{i + 1}. {system['school']} - {system['grade']} ({system['city']})")
    system_choice = input("Choose a grading system to delete by entering its number: ")
    if system_choice.isdigit() and int(system_choice) - 1 < len(created_systems) and int(system_choice) - 1 >= 0:
        system_choice = int(system_choice) - 1
    else:
        print("Invalid choice. Returning to the grading systems menu.")
        return
    system_to_delete = created_systems[system_choice]
    confirm_delete = input(f"Are you sure you want to delete the grading system '{system_to_delete['school']} - {system_to_delete['grade']} ({system_to_delete['city']})'? (yes/no): ")
    if confirm_delete.lower() == "yes":
        grading_systems.remove(system_to_delete)
        with open(grading_systems_path, "w") as grading_systems_file:
            json.dump({"systems": grading_systems}, grading_systems_file)
        if choices["chosen_system"]["id"] == system_to_delete["id"]:
            choices["chosen_system"] = None
            with open(f"{current_path}/Data/choices.json", "w") as choices_file:
                json.dump(choices, choices_file)
        print("Grading system deleted successfully.")
    else:
        print("Deletion cancelled. Returning to the grading systems menu.")

def cleanup_grading_systems():
    for system in grading_systems:
        if system["id"] != grading_systems.index(system):
            system["id"] = grading_systems.index(system)
    with open(grading_systems_path, "w") as grading_systems_file:
        json.dump({"systems": grading_systems}, grading_systems_file)