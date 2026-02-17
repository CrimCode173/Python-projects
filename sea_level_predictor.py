import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # 3. First line of best fit (all data)
    x_all = df['Year']
    y_all = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x_all, y_all)
    # Extend line to 2050
    x_pred_all = pd.Series(range(df['Year'].min(), 2051))
    y_pred_all = intercept + slope * x_pred_all
    ax.plot(x_pred_all, y_pred_all, 'r', label='Fit: 1880-2014')

    # 4. Second line of best fit (year >= 2000)
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_recent, y_recent)
    # Extend line to 2050
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = intercept2 + slope2 * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, 'green', label='Fit: 2000-2014')

    # 5. Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # 6. Save figure
    fig.savefig('sea_level_plot.png')
    return fig
