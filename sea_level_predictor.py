import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit for all data
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = np.arange(df["Year"].min(), 2051)
    sea_level_all = res_all.intercept + res_all.slope * years_all
    ax.plot(years_all, sea_level_all, color="red")

    # 4. Line of best fit for data from year 2000 onward
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = np.arange(2000, 2051)
    sea_level_2000 = res_2000.intercept + res_2000.slope * years_2000
    ax.plot(years_2000, sea_level_2000, color="green")

    # 5. Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # 6. Save and return figure
    fig.savefig("sea_level_plot.png")
    return fig
