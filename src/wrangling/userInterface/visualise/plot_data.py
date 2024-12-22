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


def plot_blood_pressure_treatment(blood_pressure_data: dict):
    """
    plot the average blood pressure readings
    gathered from each treatment
    onto a bar chart.

    Args:
        blood_pressure_data (dict): expects the following:
                                    {'systolic': (list),
                                     'diastolic': (list),
                                     'pulse': (list),
                                     'x_axis' (np.arrange(len(df.index))),
                                     'treatment': (list)}
    """
    plt.figure(figsize=(10, 8))

    blood_pressure_bars = []
    blood_pressure_bars.append(plt.bar(
        blood_pressure_data['x_axis']-0.3, blood_pressure_data['systolic'], width=0.3, label='Systolic'))
    blood_pressure_bars.append(plt.bar(
        blood_pressure_data['x_axis'], blood_pressure_data['diastolic'], width=0.3, label='Diastolic'))
    blood_pressure_bars.append(plt.bar(
        blood_pressure_data['x_axis']+0.3, blood_pressure_data['pulse'], width=0.3, label="Pulse"))

    for bar in blood_pressure_bars:
        plt.bar_label(bar, fmt="%.2f")
    plt.xticks(blood_pressure_data['x_axis'], blood_pressure_data['treatment'])
    plt.xlabel("Treatment Type")
    plt.ylabel("Blood Pressure")
    plt.ylim((70, 140))
    plt.legend()
    plt.title("Average Blood Pressure For Each Treatment Type")
    plt.show()
