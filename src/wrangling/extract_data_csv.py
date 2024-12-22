import csv

from .userInterface.table.display_data import display_extracted_data, extract_data


patient_headers = []
csv_reader = None


def get_csv_data(data_path, file_name):
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
            print("dataset headers:")
            print(f"{*patient_headers.keys(),}")

            return patient_headers, csv_reader

    except FileNotFoundError as e:
        print("Ensure the filename has been entered correctly")
        print(e)


def demographic_info(patient_id: int, csv_reader: list, patient_headers: dict):
    # contains the specific values from the columns, mapped to their respective key headings.
    demographic_info = {}
    columns = ['Age', 'Gender', 'Smoking_History', 'Ethnicity']

    for record in csv_reader:
        if int(record[patient_headers['Patient_ID']]) == patient_id:
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


def medical_history(ethnicity: int, csv_reader: list, patient_headers: dict):
    medical_history = []
    columns = ['Family_History', 'Comorbidity_Diabetes',
               'Comorbidity_Kidney_Disease', 'Haemoglobin_Level']

    for record in csv_reader:
        if ethnicity in record[patient_headers['Ethnicity']].casefold():
            medical_history.append(extract_data(
                columns, record, patient_headers))
    print(f"Records for patients of {ethnicity.capitalize()} ethnicity:")
    display_extracted_data(columns, medical_history, limit_rows=20)


def survival_treatment_details(survival_months: int, csv_reader: list, patient_headers: dict):
    # survival_period_months = 100
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
