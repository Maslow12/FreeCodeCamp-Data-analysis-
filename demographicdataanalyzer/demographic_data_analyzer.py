import pandas as pd 
def import_file(url,extension,filename='file',directory='')->str():
    import requests
    import os
    r = requests.get(url, allow_redirects=True)
    f = f'{filename}.{extension}'
    if directory == '':
        save_path = os.getcwd()
    else:
        save_path = directory
    open(f, 'wb').write(r.content)
    folder = os.path.join(save_path, f)
    return folder

url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/master/adult.data.csv'
import_file(url,extension='csv')
df = pd.read_csv('file.csv')

def calculate_demographic_data(print_data=True):
    # # Many people of each race are represented in this dataset
    race_count = df['race'].value_counts()
    # # Average age of men:
    average_age_men = df[df['sex'] == 'Male']
    average_age_men = round(average_age_men['age'].mean(),1)
    # # Percentage of people who have a Bachelor's degree:
    percentage_bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((percentage_bachelors.shape[0]/df.shape[0])*100,1)
    # # Percentage of people with advanced education make more than 50K:
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    higher_education_rich = round((higher_education_rich.shape[0]/higher_education.shape[0])*100,1)
    # # Percentage of people without advanced education make more than 50K:
    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K'] 
    lower_education_rich = round((lower_education_rich.shape[0]/lower_education.shape[0])*100,1)
    # #  Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()
    # # Percentage of the people who work the minimum number of hours per week have a salary of more than 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = (rich_percentage.shape[0]/num_min_workers.shape[0])*100
    # # Country has the highest percentage of people that earn >50K and what is that percentage
    highest_earning_country = df[df['salary'] =='>50K']
    highest_earning_country_percentage = round(((highest_earning_country['native-country'].value_counts()*100)/(df['native-country'].value_counts())).max(),1)
    highest_earning_country = ((highest_earning_country['native-country'].value_counts()*100)/(df['native-country'].value_counts())).sort_values(ascending=False).index[0]
    # # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[df['native-country'] == 'India']
    top_IN_occupation = top_IN_occupation['occupation'].value_counts().index[0]
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
calculate_demographic_data(print_data=True)
    


