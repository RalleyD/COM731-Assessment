import csv

from .userInterface.table.display_data import display_extracted_data, extract_data
from .userInterface.user_selections import check_for_quit, check_for_quit

patient_headers = []
csv_reader = None


def get_csv_data(data_path: str, file_name: str) -> tuple:
    """
        Provides CSV data and
        a mapping of column headings to index.

        Returns:
            tuple: a list of the CSV data rows
                   a dictionary of column headers mapped
                   to their respective column index.
    """
    patient_headers = None
    csv_reader = None

    if check_for_quit(file_name):
        return None, None
    try:
        with open(data_path+file_name, 'r', encoding='utf8', newline='') as fp:
            ''' turn the csv reader into a list containing the entire dataset
                so that we only have to open the file and use the file object
                once.
            '''
            csv_reader = list(csv.reader(fp.readlines(), delimiter=','))
            ''' using a list allows traversal as many times as needed.
                Since this is no longer an iterator that is consumed once,
                remove the header row from the list
            '''
            patient_headers = csv_reader.pop(0)
            ''' creating a mapping to efficiently look up the column index
                from the header row
            '''
            patient_headers = {v: i for i, v in enumerate(patient_headers)}

            # development purposes only
            print(f"\nDataset headers, {file_name}:")
            print("----------------------------------")
            print("\t\n".join(patient_headers))
    except FileNotFoundError as e:
        print("Ensure the filename has been entered correctly")
        print(e)
    finally:
        return patient_headers, csv_reader


def demographic_info(patient_id: str, csv_reader: list, patient_headers: dict):
    """
        Displays a table of data for a given patient ID.

        Args:
        patient_id (int): patient ID number.
        csv_reader (list): rows of data
        patient_headers (dict): mapping of column headers to their respective
                                column index.
    """
    # contains the specific values from the columns, mapped to their respective key headings.
    demographic_info = {}
    columns = ['Age', 'Gender', 'Smoking_History', 'Ethnicity']

    if check_for_quit(patient_id):
        return

    for record in csv_reader:
        if int(record[patient_headers['Patient_ID']]) == int(patient_id):
            for column in columns:
                ''' look up the row index from the column heading string
                    and assign the value in the row to the dictionary,
                    providing the heading string as a key
                '''
                demographic_info[column] = record[patient_headers[column]]

    if (len(demographic_info) > 0):
        print(f"Demographic info for patient ID: {patient_id}")
        display_extracted_data(columns, [demographic_info])
    else:
        print("Patient ID not found!")


def medical_history(ethnicity: str, csv_reader: list, patient_headers: dict):
    """
        Displays a table of data for a given patient ethnicity.

        Args:
        ethnicity (string): patient ethnicity e.g 'asian'.
        csv_reader (list): rows of data
        patient_headers (dict): mapping of column headers to their respective
                                column index.
    """
    medical_history = []
    columns = ['Family_History', 'Comorbidity_Diabetes',
               'Comorbidity_Kidney_Disease', 'Haemoglobin_Level']

    if check_for_quit(ethnicity):
        return

    for record in csv_reader:
        if ethnicity in record[patient_headers['Ethnicity']].casefold():
            medical_history.append(extract_data(
                columns, record, patient_headers))
    print(f"Records for patients of {ethnicity.capitalize()} ethnicity:")
    display_extracted_data(columns, medical_history, limit_rows=20)


def survival_treatment_details(survival_months: int, csv_reader: list, patient_headers: dict):
    """
        Displays a table of data for a given survival duration (months).

        Args:
        survival_months (int): patient survival.
        csv_reader (list): rows of data
        patient_headers (dict): mapping of column headers to their respective
                                column index.
    """
    long_term = []
    columns = ['Age', 'Tumor_Size_mm', 'Tumor_Location', 'Stage']

    for record in csv_reader:
        if int(record[patient_headers['Survival_Months']]) > survival_months:
            long_term.append(
                extract_data(columns, record, patient_headers)
            )

    print(
        f"Patient records for survival greater than {survival_months} months on treatment:\n")
    display_extracted_data(columns, long_term)


def hypertension_patients(diastolic_target: float, csv_reader: list, patient_headers: dict):
    """
        Displays a table of data for a hypertensive patients.

        Args:
        diastolic_target (float): any patient below this target will be filtered out.
        csv_reader (list): rows of data
        patient_headers (dict): mapping of column headers to their respective
                                column index.
    """
    treatment_records = []
    columns = ['Treatment', 'Insurance_Type',
               'Performance_Status', 'Comorbidity_Chronic_Lung_Disease']

    for record in csv_reader:
        # is the patient hypertensive or blood pressure above 140
        if record[patient_headers['Comorbidity_Hypertension']] or \
                record[patient_headers['Blood_Pressure_Diastolic']] > diastolic_target:
            treatment_records.append(
                extract_data(columns, record, patient_headers)
            )

    print(
        f"Treatment records for patients with diastolic blood pressure above {diastolic_target} target or hypertension:\n")

    display_extracted_data(columns, treatment_records)
