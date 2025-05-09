import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=False):
    # Read data from file
    df = None
    df = pd.read_csv('adult.data.csv')
    #print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = np.array(df['race'].value_counts())
    #print(race_count)

    # What is the average age of men?
    average_age_men = round((df[df['sex']=='Male']['age']).mean(), 1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / df['education'].count() * 100, 1)
    #print(percentage_bachelors)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df[(df.education == 'Masters') | (df.education == 'Bachelors') | (df.education == 'Doctorate')]).shape[0]
    #print(higher_education)
    lower_education = (df[(df.education != 'Masters') & (df.education != 'Bachelors') & (df.education != 'Doctorate')]).shape[0]
    #print(lower_education)

    # percentage with salary >50K
    higher_education_rich = round(((df[ ( (df.education == 'Masters') | (df.education == 'Bachelors') | (df.education == 'Doctorate') ) & (df.salary == '>50K')]).shape[0]) / higher_education * 100, 1)
    #print(higher_education_rich)
    lower_education_rich = round(((df[ ( (df.education != 'Masters') & (df.education != 'Bachelors') & (df.education != 'Doctorate') ) & (df.salary == '>50K')]).shape[0]) / lower_education * 100, 1)
    #print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    min_work_hours = df['hours-per-week'].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers = round((df[ ((df.salary) == '>50K') & (df['hours-per-week'] == min_work_hours) ].shape[0])/ (df[ (df['hours-per-week'] == min_work_hours) ].shape[0]) * 100,)
    #print(num_min_workers)


    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).sort_values(ascending = False).head(1).index[0]


    #print(highest_earning_country)
    
    highest_earning_country_percentage = round((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).sort_values(ascending = False).head(1).iloc[0] , 1)
    #print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    
    for i in range(10):
        print('___________________')

    #print(top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
