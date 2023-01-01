import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cityList = list(CITY_DATA.keys())
    while True:
        city = input("Enter required city name: ")
        if (city.strip().lower() == 'chicago') or (city.strip().lower() == 'new york city') or (city.strip().lower() == 'washington'):
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['All', 'January','February','March','April','May','June','July','August','September','October','November','December']
    while True:
        month = input("Enter month: ")
        if month.strip().title() in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekdays = ['All', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    while True:
        day = input("Enter day: ")
        if day.strip().title() in weekdays:
                break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    if month != 'all':
        months = ['All', 'January','February','March','April','May','June','July','August','September','October','November','December']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Common month:', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    rs = df['Start Station'].value_counts()[df['Start Station'].value_counts() == df['Start Station'].value_counts().max()]
    print('Most popular Start station: ',rs)

    # TO DO: display most commonly used end station
    re = df['End Station'].value_counts()[df['End Station'].value_counts() == df['End Station'].value_counts().max()]
    print('Most popular End station: ',re)

    # TO DO: display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum() // 3600
    print('Total Travel time: ',travel_time,'hours')

    # TO DO: display mean travel time
    travel_time = df['Trip Duration'].mean() // 60
    print('Mean Travel time: ',travel_time,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    except KeyError:
        print('No gender information found at this location')   

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        byear = df['Birth Year'].value_counts()[df['Birth Year'].value_counts() == df['Birth Year'].value_counts().max()]
        byear_min = df['Birth Year'].min()
        byear_max = df['Birth Year'].max()
        print('Most common birth year: ',byear, '\n', 'Oldest user is from year: ', byear_min, '\n', 'Youngest user is from year: ', byear_max)
    except KeyError:
        print('No birth date information found at this location')  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()