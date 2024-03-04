from scipy import stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defining a function to plot histograms, density plots, and Q-Q plots
def plot_distribution(column_name):
    # Remove NaN values for plotting
    data = df[column_name].dropna()
    
    # Set up the matplotlib figure
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))

    # Histogram
    sns.histplot(data, kde=False, ax=axs[0, 0])
    axs[0, 0].set_title(f'Histogram of {column_name}')

    # Density Plot
    sns.kdeplot(data, ax=axs[0, 1])
    axs[0, 1].set_title(f'Density Plot of {column_name}')

    # Q-Q plot
    stats.probplot(data, dist="norm", plot=axs[1, 0])
    axs[1, 0].set_title(f'Q-Q Plot of {column_name}')

    # Boxplot
    sns.boxplot(x=data, ax=axs[1, 1])
    axs[1, 1].set_title(f'Boxplot of {column_name}')

    plt.tight_layout()
    plt.show()