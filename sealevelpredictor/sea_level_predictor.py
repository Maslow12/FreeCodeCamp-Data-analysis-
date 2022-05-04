import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    x,y = df['Year'],df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    df_years = [d for d in range(1880,2051)]
    pred = [round(intercept+d*slope,7) for d in df_years]
    df_2 = df[(df['Year']>1999) & (df['Year']<2050)]
    x_2,y_2 = df_2['Year'], df_2['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_2, y_2)
    df_years_2 = [d for d in range(2000,2051)]
    pred_2 = [round(intercept2+d*slope2,7) for d in df_years_2]
    fig, ax = plt.subplots()
    fig.set_figheight(12)
    fig.set_figwidth(10)
    ax.scatter(x,y)
    ax.plot(df_years,pred, 'r', label='Prediction to year 2050')
    ax.plot(df_years_2,pred_2, 'r')
    plt.tight_layout()
    ax.set(xlabel='Year', ylabel='Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()



