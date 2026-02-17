import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # What percentage of people with advanced education make more than 50K?
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round(
        (df[~higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum hours have salary >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # What country has the highest percentage of people earning >50K?
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()

    country_percent = (country_rich / country_total) * 100

    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(
        country_percent.max(), 1
    )

    # Most popular occupation in India for those earning >50K
    top_IN_occupation = (
        df[
            (df['native-country'] == 'India') &
            (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich %:", higher_education_rich)
        print("Lower education rich %:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
