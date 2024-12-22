
def display_extracted_data(columns: list, records: list, limit_rows=50):
    """
    Print the data extract in a pretty, tablular style

    Args:
        columns (list): string names of the columns within
                        the records passed to the function.

        records (list): a list of dictionaries containing 
                        the relevant data to be displayed
    """
    # Base case - if no records where found, tell the user
    if len(records) == 0:
        print("No records found!")
        return

    ''' find the longest header name which will be used to
        specific the header width for all columns. '''
    column_width = max([len(col) for col in columns])
    separator = '|'
    formatted_cols = [separator]
    for col in columns:
        # left-align by, at most, the maximum desired column width
        formatted_cols.append(f" {col:<{column_width}} |")

    # This tightly joins each header to the adjacent separator.
    header_row = "".join(formatted_cols)
    # underline the table header and print both
    print(f"{header_row}\n{'-' * len(header_row)}")

    item_cols = ['|']
    count = 0
    limit_reached = False
    for record in records:
        if limit_reached:
            break
        for value in record.values():
            item_cols.append(f" {value:<{column_width}} |")
            count += 1
            if count == len(columns):
                # place the next set of data on the next line
                item_cols.append('\n')
                item_cols.append(separator)
                limit_rows -= 1
                count = 0
            if limit_rows == 0:
                limit_reached = True
                break

    # get rid of the trailing separator which appears on a new line at the end of the table
    item_cols.pop(-1)
    # display each row of data, formatted to align to the table display
    print("".join(item_cols))


def extract_data(columns: list, record: list, patient_headers: dict) -> list:
    """
    Extract the relevant data from a row into a dictionary
    that looks like:
        {column_header: data_value, ...}

    This saves on code repetition when storing the specific
    data to be analysed in a new data structure.

    Args:
        columns (list): the specific columns to extract
                        from the row.
        record (list): a single row of data.
        patient_headers(dict): mapping of heading names to
                               column index.

    Returns:
        dict: of values mapped to keys from the specified columns.
    """
    records = {}
    for column in columns:
        records.update(
            {
                column: record[patient_headers[column]]
            }
        )
    return records
