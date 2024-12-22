import matplotlib.pyplot as plt
import pandas as pd


def plot_treatment_proportion_for_ethnicity(ethnicity: str, treatment_count: list, treatment_labels: list):
    """
        Plot a pie chart of the proportion of treatments
        for a given ethnic group.

        Args:
            ethnicity (str): user-specified ethnic group
            treatment_count (list): value count of each treatment
            treatment_labels (list): the name of each treatment
    """
    # create a figure
    plt.figure(figsize=(10, 6))

    # plot a pie chart
    plt.pie(treatment_count, labels=treatment_labels, autopct='%1.1f%%')

    # set a plot title and legend
    plt.title(f"Pie Chart: Cancer treatment for {ethnicity} ethnic group")
    plt.legend(loc="upper left", bbox_to_anchor=(0.9, 1))

    # show the chart
    plt.show()


def plot_smoking_packs_cancer_stage(x_labels: list, y_labels: list, y_data: list):
    """
    Create a line chat to plot the trend of average smoking packs against
    cancer stage.
    Loops through every list in y_data to plot on the same chart.

    Args:
        x_labels (list): ticks or values for x axis.
        y_labels (list): legend for y axis data
        y_data (list): of lists containng the output data to plot.
    """
    plt.figure(figsize=(20, 10))
    for ethnicity, y in zip(y_labels, y_data):
        # y_mean_smoking_pack_years = y_axis_data.get_group(
        #     ethnicity).Smoking_Pack_Years.to_list()
        plt.plot(x_labels, y, label=ethnicity)

    plt.xlabel("Cancer Stage")
    plt.ylabel("Average (mean) Smoking Pack Years")
    plt.title(
        "Ethnic Group Average Smoking Pack Consumption Accross Each Cancer Stage")
    plt.legend()
    plt.show()
