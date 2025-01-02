import os

# constant - directory where the datasets are stored
data_path = "Data/"
# list all files in the dataset directory
data_files = os.listdir(data_path)


def set_user_file():
    """
    Select the .csv file from the user's input

    Returns:
        string: file name (with extension)
    """
    # list all files in the dataset directory
    data_files = os.listdir(data_path)
    print(
        f"The available files to analyse, in the '{data_path[:-1]}' directory:")
    print("\t\n".join(data_files))
    while True:
        file_name = input(
            "Enter the name of the CSV file from the Data directory or 'quit' ('q') to quit...")
        if check_for_quit(file_name):
            break
        elif file_name:
            break
        else:
            print("Please enter a valid filename including the '.csv' extension")
    return file_name


def _set_patient_field(field: str):
    """
    Helper function.

    Validates and sets the user specified input.
    Used for checking the input against the data record.

    Args:
        field (string): 

    Returns:
        string: caseless patient field for comparison
    """
    user_selection = ""
    while user_selection == "":
        user_selection = input(
            f"Enter the patient {field} or 'quit' ('q') to quit...")
        if check_for_quit(user_selection):
            break
        elif user_selection:
            break
        else:
            print(f"Please enter a valid input for {field}")
    return user_selection.casefold()


def set_patient_id():
    """
    Validate and set the user's patient ID input

    Returns:
        string: patient ID
    """
    while True:
        id = _set_patient_field('patient_id')
        if not check_for_quit(id):
            try:
                id = int(id, base=10)
            except ValueError:
                print("Enter a valid numerical value for patient ID")
            else:
                break
        else:
            break
    return id


def set_patient_ethnicity():
    """
    Wraps _set_patient_field to validate and return the user input.

    Returns:
        string: caseless patient ethnicity for comparison
    """
    return _set_patient_field("ethnicity")


def set_patient_treatment():
    """
    Wraps _set_patient_field to validate and return the user input.

    Returns:
        string: caseless patient treatment for comparison
    """
    return _set_patient_field("treatment")


def set_patient_gender():
    """
    Wraps _set_patient_field to validate and return the user input.

    Returns:
        string: caseless patient gender for comparison
    """
    return _set_patient_field("gender")


def check_for_quit(input: str) -> bool:
    """
    Checks if the user wants to quit

    Args:
        input (string): user input

    Returns:
        bool: true if the user wants to quit
              otherwise false.
    """
    if type(input) is str:
        if input.casefold() in ['q', 'quit']:
            return True
        else:
            return False
