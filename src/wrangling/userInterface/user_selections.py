'''
    Defining some constants and variables that
    will be used throughout the system
    at the beginning of the file for easy access.
'''
import os
# constant - directory where the datasets are stored
data_path = "Data/"

data_files = os.listdir(data_path)


def set_user_file():
    print(
        f"The available files to analyse, in the '{data_path[:-1]}' directory:")
    print("{}\t\n".format(*data_files))
    file_name = input(
        "Enter the name of the CSV file from the Data directory...")
    if file_name == "":
        raise Exception("Plase Enter a valid selection")
    return file_name


def set_patient_id():
    try:
        patient_id = int(
            input("Enter patient ID to retrieve demographic information..."), base=10)
    except ValueError:
        print("please enter a valid numerical value for the patient ID")
    return patient_id


def _set_patient_field(field: str):
    user_selection = ""
    while user_selection == "":
        user_selection = input(
            f"Enter the patient {field} or 'quit' ('q') to quit...")
        if user_selection.casefold() in ['q', 'quit']:
            break
        elif user_selection:
            break
        else:
            print(f"Please enter a valid input for {field}")
    return user_selection.casefold()


def set_patient_ethnicity():
    return _set_patient_field("ethnicity")


def set_patient_treatment():
    return _set_patient_field("treatment")


def set_patient_gender():
    return _set_patient_field("gender")
