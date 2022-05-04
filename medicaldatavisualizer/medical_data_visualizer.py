import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')
BMI = df['weight']/((df['height']/100)**2)
df.loc[BMI < 25, 'overweight'] = 0
df.loc[BMI > 25, 'overweight'] = 1
df.loc[(df['cholesterol'] == 1), 'cholesterol'] = 0
df.loc[(df['cholesterol'] > 1), 'cholesterol'] = 1
df.loc[(df['gluc'] == 1), 'gluc'] = 0
df.loc[(df['gluc'] > 1), 'gluc'] = 1
def draw_cat_plot():
    df_cat=pd.melt(df,id_vars=['cardio'], value_vars=['active', 'alco','cholesterol', 'gluc', 'overweight', 'smoke'])
    g = sns.catplot(x="variable", hue="value",col="cardio", data=df_cat, kind='count')
    g.set_ylabels('total')
    fig = g.fig
    fig.savefig('catplot.png')
    return fig
def draw_heat_map():
    global df
    # Clean the data
    df_heat = df[~(df["ap_hi"]<df["ap_lo"])&(df.height>=df.height.quantile(0.025))&(df.height<=df.height.quantile(0.975))&(df.weight>=df.weight.quantile(0.025))&(df.weight<=df.weight.quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')
    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    # Set up the matplotlib figure
    fig , ax =  plt.subplots(figsize=(16,10))
    sns.heatmap(corr, annot=True, mask=mask, square=4, fmt=".1f")
    fig.savefig('heatmap.png')
    return fig







