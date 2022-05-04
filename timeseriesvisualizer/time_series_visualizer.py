import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data

df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12,4))
    plt.plot(pd.to_datetime(df['date']), df['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    global df
    # Copy and modify data for monthly bar plot
    df_bar = df.assign(month = pd.DatetimeIndex(df['date']).month_name(), year=pd.DatetimeIndex(df['date']).year)
    df_bar = (df_bar.groupby(['year','month'])['value'].mean()).to_frame().reset_index()
    # Draw bar plot
    fig = plt.figure(figsize=(15,4), linewidth=1.0, tight_layout=True)
    cmap = sns.color_palette("Paired")
    g = sns.catplot(x='year', y='value', hue='month', kind='bar', data=df_bar, palette=cmap, aspect=2, legend=False, margin_titles=True, ci=None)
    fig = g.fig
    plt.legend(['January','February','March', 'April', 'May','June','July','August','September', 'October', 'November',
       'December'],loc='upper left')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df['date'] = pd.to_datetime(df['date'])
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['num'] = pd.DatetimeIndex(df['date']).month
    df_box = df_box.sort_values(by='num', ascending=True)

    # Draw box plots (using Seaborn)
    
    fig, axes = plt.subplots(1,2,figsize=(15,8)) 
    sns.boxplot(ax=axes[0],data=df_box, x='year', y='value')
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[0].set_xlabel('Year')
    axes[1].set_xlabel('Month')
    axes[0].set_ylabel('Page Views')
    axes[1].set_ylabel('Page Views')
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


























 


'''





# In[82]:

'''


