import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 
        'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

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
    while True:
        city=str(input('Choose from Chicago, New York City and Washington. \n')).lower()
        if city not in CITY_DATA.keys():
            print('Please enter a correct value for city')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input('Search by typing in the month or type in all\n')).title()
        if month not in months:
            print('Please enter a correct value for month')
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Search by typing the day or type in all\n')).title()
        if day not in days:
            print('Please enter a correct value for month')
        else:
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
    
    
    # Puts Start Time column in datetime format  #
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month']= df['Start Time'].dt.month
    df['week_days']= df['Start Time'].dt.day_name()

    # filter city data by month
    if month != 'All':
        df = df[df['Start Time'].dt.strftime('%b') == month]

    # filter city data by day
    if day != 'All':
        df = df[df['Start Time'].dt.day_name() == day]
  

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    import datetime as dt
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Creating new columns for df
    df['month']= df['Start Time'].dt.strftime('%b')
    df['week_days']= df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    freq_month = df['month'].mode()
    print('The most common month is: {}'.format(freq_month))
    
    # TO DO: display the most common day of week
    print('The most common day is: {}'.format(df['week_days'].mode()))
    
    # TO DO: display the most common start hour
    print('The most common start hour is: {}'.format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    
    most_frequent_combination = df['Start Station'] + ' and ' + df['End Station']
    print('The most popular combination is: {}'.format(most_frequent_combination.mode()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The user types can be divided into \n {}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('Oops!,Washington has no data for gender')
    else:
        print('The number of genders are \n{}'.format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Oops!,Washington has no data for Birth Year ')
    else:
        print('The Earliest birth year is: {}'.format(df['Birth Year'].min()))
        print('The most recent birth year is: {}'.format(df['Birth Year'].max()))
        print('The most common birth year is: {}'.format(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    choice_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    n = 5
    while (choice_data=='yes'):
        print(df.iloc[start_loc:n])
        start_loc += 5
        n*=2+1
        choice_data = input("Do you wish to view the next five?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
