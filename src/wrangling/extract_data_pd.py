import pandas as pd


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
