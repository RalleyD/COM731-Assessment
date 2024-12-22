import matplotlib.pyplot as plt


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
