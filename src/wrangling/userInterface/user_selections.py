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


def set_patient_ethnicity():
    ethnicity = ""
    while ethnicity == "":
        ethnicity = input("Enter the patient ethnicity...")
        if ethnicity:
            break
        else:
            print("Please enter a valid input for Ethnicity, e.g 'Asian'")
    return ethnicity.casefold()
