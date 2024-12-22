import pandas as pd
from src.wrangling.userInterface.visualise.plot_data import plot_smoking_packs_cancer_stage


def _capitalise_input(user_value: str) -> str:
    value_split = user_value.split()
    return " ".join(word.capitalize() for word in value_split)


def patient_long_survival(ethnicity: str, lung_cancer_df: pd.DataFrame):
    """
    Print the top three treatments for patients of a given
    ethnicity.
    This function returns the top three treatmetns where
    survival was greater than 100 months.

    Args:
        ethnicity (str): case-insensitive ethnic group.

        lung_cancer_df (DataFrame): lung cancer Pandas DataFrame.
    """
    ethnicity = _capitalise_input(ethnicity)
    survival_months = 100
    long_term_df = lung_cancer_df.loc[lung_cancer_df.Survival_Months > survival_months, [
        'Treatment', 'Survival_Months', 'Ethnicity']]

    long_term_ethnic_groups = long_term_df.groupby('Ethnicity')

    print(
        f"Top three treatments for {ethnicity} group - Surival > {survival_months} months")
    print(long_term_ethnic_groups.get_group(
        ethnicity).Treatment.value_counts().head(3))


def treatment_white_blood_count(ethnicity: str, treatment: str, lung_cancer_df: pd.DataFrame):
    """
    Print the average white blood cell count for each treatment type
    given a certain ethnicity.

    Args:
        ethnicity (str): case-insensitive ethnic group.
        lung_cancer_df (DataFrame): lung cancer Pandas DataFrame.
    """
    treatments = lung_cancer_df.Treatment.unique().tolist()
    ethnicity = _capitalise_input(ethnicity)
    treatment = _capitalise_input(treatment)

    if treatment not in treatments:
        raise RuntimeError(f"Treatment: '{treatment}' not found.")

    white_blood_df = lung_cancer_df.groupby('Ethnicity')
    ethnic_group_treatment = white_blood_df.get_group(
        ethnicity).groupby('Treatment')

    print(
        f"Average white blood cell count for {treatment} in {ethnicity} ethnic group")

    print(ethnic_group_treatment.get_group(
        treatment).White_Blood_Cell_Count.mean())


def lung_tumor_data(lung_cancer_df: pd.DataFrame, pulse: int, tumor_size_mm: float):
    # Filter by pulse > 90 and tumor size < 15.0, keeping only the columns we need.
    lung_tumor_df = lung_cancer_df.loc[(lung_cancer_df.Blood_Pressure_Pulse > pulse) & (lung_cancer_df.Tumor_Size_mm < tumor_size_mm),
                                       ['Smoking_Pack_Years', 'Treatment', 'Tumor_Location']].reset_index()

    # group by tumor location and treatment type, finding the average smoking packs for each group
    lung_tumor_df = lung_tumor_df.groupby(["Tumor_Location", "Treatment"])\
        .Smoking_Pack_Years.mean()

    print(
        f"Average numnber of smoking packs for patients with pulse over {pulse} and tumor size over {tumor_size_mm} mm")
    print(lung_tumor_df)


def survival_blood_pressure(gender: str, lung_cancer_df: pd.DataFrame):
    """
    Pretty print average survival duration and blood pressure metrics
    for each treatment at each cancer stage, based on gender.

    Args:
        gender (str): user-specified gender
        lung_cancer_df (DataFrame): lung cancer data frame.
    """
    gender = _capitalise_input(gender)
    if gender not in lung_cancer_df.Gender.unique():
        raise RuntimeError(f"Gender: '{gender}' not found")

    ''' Group by gender, treatment, and cancer stage.
    Then, find the average survival duration and blood pressure levels
    for each cancer stage.
    Finally, reset the index to remove the Dataframe levels
    and provide a sequential index.
    '''
    survival_cancer_df = lung_cancer_df.groupby(['Gender', 'Treatment', 'Stage'])[
        ['Survival_Months', 'Blood_Pressure_Diastolic', 'Blood_Pressure_Systolic']].mean().reset_index()

    # filter out rows for specified gender
    survival_cancer_gender_df = survival_cancer_df.loc[survival_cancer_df.Gender == gender, :]

    # drop the gender column
    survival_cancer_gender_df.drop(["Gender"], inplace=True, axis=1)

    print(
        f"average survival duration and blood pressure metrics for {gender}s")
    # pretty print in markdown table style, remove the numerical index column
    print(survival_cancer_gender_df.to_markdown(index=False))


def treatment_for_ethnicity(ethnicity: str, lung_cancer_df: pd.DataFrame) -> tuple:
    """
        Can be used to provide input to a pie chart.

        Args:
        ethnicity (str): user-specified ethnic group
        lung_cancer_df (DataFrame): lung cancer data frame

        Returns:
            A tuple of two lists
            The count of each treatment for a specified ethnic group.
            The names of each treatment.
        """
    ethnicity = _capitalise_input(ethnicity)
    grp = lung_cancer_df.groupby('Ethnicity')
    grp = grp.get_group(ethnicity)

    # create a Series of value counts of each treatment
    grp_treatment_counts = grp.Treatment.value_counts()

    # retrieve the index lables from the Series and put them into a list
    treatment_labels = grp_treatment_counts.index.to_list()
    # get the values of the Series and put into a list
    treatment_count = grp_treatment_counts.to_list()  # grp['count'].to_list()

    return treatment_count, treatment_labels


def smoking_packs_cancer_stage(lung_cancer_df: pd.DataFrame, plot=True):
    """
    Obtain the average smoking packs at each cancer stage
    for each ethnic group.

    Args:
        lung_cancer_df (DataFrame): DataFrame to wrangle.
        plot (bool): switch to determine whether or not to plot the
                     output data.
    """
    # get Stage, Smoking Pack and Ethnicity columns from the lung cancer DataFrame
    smoking_consumption = lung_cancer_df.loc[:, [
        'Stage', 'Smoking_Pack_Years', 'Ethnicity']]

    # in order to determine the average smoking for each cancer stage in each ethnic group
    # the DataFrame must first be grouped by ethnicity and stage columns.
    smoking_consumption = smoking_consumption.groupby(['Ethnicity', 'Stage'])[
        ['Smoking_Pack_Years']].mean()
    smoking_consumption.reset_index(inplace=True)

    grp = smoking_consumption.groupby('Ethnicity')

    x_cancer_stages = smoking_consumption.Stage.unique().tolist()
    ethnicity_labels = smoking_consumption.Ethnicity.unique().tolist()

    if plot:
        y_data = [grp.get_group(ethnicity).Smoking_Pack_Years.to_list()
                  for ethnicity in ethnicity_labels]
        plot_smoking_packs_cancer_stage(
            x_cancer_stages, ethnicity_labels, y_data)
