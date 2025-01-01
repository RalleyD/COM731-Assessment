import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_treatment_proportion_for_ethnicity(ethnicity: str, treatment_count_series: pd.Series):
    """
        Plot a pie chart of the proportion of treatments
        for a given ethnic group.

        Args:
            ethnicity (str): user-specified ethnic group
            treatment_count_series (Series): a series of treatment counts
                                             indexed by treatment type
    """

    # retrieve the index lables from the Series and put them into a list
    treatment_labels = treatment_count_series.index.to_list()
    # get the values of the Series and put into a list
    treatment_count = treatment_count_series.to_list()

    # create a figure
    plt.figure(figsize=(10, 6))

    # plot a pie chart
    plt.pie(treatment_count, labels=treatment_labels, autopct='%1.1f%%')

    # set a plot title and legend
    plt.title(f"Pie Chart: Cancer treatment for {ethnicity} ethnic group")
    plt.legend(loc="upper left", bbox_to_anchor=(0.9, 1))

    # show the chart
    plt.show()


def plot_smoking_packs_cancer_stage(ethnic_grp_cancer_stage_df: pd.DataFrame):
    """
    Create a line chat to plot the trend of average smoking packs against
    cancer stage.
    Loops through every list in y_data to plot on the same chart.

    Args:
        ethnic_grp_cancer_stage_df (DataFrame): mean smoking pack years
                                                for each cancer stage and
                                                ethnic group
    """
    plt.figure(figsize=(20, 10))
    for ethnicity, group in ethnic_grp_cancer_stage_df.groupby('Ethnicity'):
        plt.plot(group['Stage'], group['Smoking_Pack_Years'],
                 label=ethnicity)

    plt.xlabel("Cancer Stage")
    plt.ylabel("Average (mean) Smoking Pack Years")
    plt.title(
        "Ethnic Group Average Smoking Pack Consumption Accross Each Cancer Stage")
    plt.legend()
    plt.show()


def plot_blood_pressure_treatment(treatment_blood_pressure_df: pd.DataFrame):
    """
    plot the average blood pressure readings
    gathered from each treatment
    onto a bar chart.

    Args:
        blood_pressure_data (DataFrame): columns, mean blood pressure readings.
                                         rows, treatment.
    """

    x_treatment = treatment_blood_pressure_df.index.to_list()
    # in order to divide a bar into three, a numpy array is required to offset the bar
    x_axis = np.arange(len(x_treatment))

    plt.figure(figsize=(10, 8))

    blood_pressure_bars = []
    blood_pressure_bars.append(plt.bar(
        x_axis-0.3, treatment_blood_pressure_df['Blood_Pressure_Systolic'], width=0.3,
        label=treatment_blood_pressure_df['Blood_Pressure_Systolic'].name))

    blood_pressure_bars.append(plt.bar(
        x_axis, treatment_blood_pressure_df['Blood_Pressure_Diastolic'], width=0.3,
        label=treatment_blood_pressure_df['Blood_Pressure_Diastolic'].name))

    blood_pressure_bars.append(plt.bar(
        x_axis+0.3, treatment_blood_pressure_df['Blood_Pressure_Pulse'], width=0.3,
        label=treatment_blood_pressure_df['Blood_Pressure_Pulse'].name))

    for bar in blood_pressure_bars:
        plt.bar_label(bar, fmt="%.2f")

    plt.xticks(x_axis, x_treatment)
    plt.xlabel("Treatment Type")
    plt.ylabel("Blood Pressure")
    plt.ylim((70, 140))
    plt.legend()
    plt.title("Average Blood Pressure For Each Treatment Type")
    plt.show()


def plot_insurer_treatment_data(axis_data: dict):
    """
    Plot a bar chart of counts of different treatment for each insurer

    Args:
        axis_data (dict): extracted data, expected format:
                            {'chemo': (list),
                            'surgery': (list),
                            'radiotherapy': (list),
                            'targeted': (list),
                            'x_axis': np.arange(len(labels)),
                            'labels': (list)}
    """
    plt.figure(figsize=(15, 10))

    treatment_bars = []
    bar_width = 0.2
    treatment_bars.append(
        plt.bar(axis_data['x_axis']-0.4, axis_data['chemo'], width=bar_width, label='Chemotherapy'))
    treatment_bars.append(
        plt.bar(axis_data['x_axis']-0.2, axis_data['surgery'], width=bar_width, label='Surgery'))
    treatment_bars.append(plt.bar(axis_data['x_axis'], axis_data['radiotherapy'],
                          width=bar_width, label="Radiotherapy"))
    treatment_bars.append(plt.bar(
        axis_data['x_axis']+0.2, axis_data['targeted'], width=bar_width, label="Targeted Therapy"))

    for bar in treatment_bars:
        plt.bar_label(bar)
    plt.xticks(axis_data['x_axis'], axis_data['labels'])
    plt.xlabel("Insurance Type")
    plt.ylabel("Treatment Counts")
    plt.ylim(bottom=1000)
    plt.legend()
    plt.title("Treatment Counts For Each Insurance Type")
    plt.show()
