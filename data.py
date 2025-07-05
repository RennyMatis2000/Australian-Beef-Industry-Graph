# Import standard Python functions needed to support this module
from random import randint, choice, seed, shuffle
from turtle import textinput
from re import sub

# Define the months of the year when reports are made
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def raw_data(given_seed):
    chosen_seed = given_seed
    # Set the random number seed and inform the user
    print(f'Using seed {chosen_seed} \n')
    seed(chosen_seed)

    # Define an initial value (which could be interpreted as that
    # for December in the previous year) biased towards the middle
    # of the range
    current_level = choice([-2, -1, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2])
    # Initialise the data set
    reports = []

    # Create the monthly reports
    for month in months:
        # Choose which way to change the level, biased towards
        # staying about the same
        change = choice([-2, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2])
        # Update the current level
        current_level = current_level + change
        # Sometimes reports get lost in the mail (about
        # once every three years on average)
        missing = (randint(1, 36) == 1)
        # Add this month's report to the data set (provided it
        # wasn't lost)
        if not missing:
            reports.append([month, current_level])
    # Unfortunately the reports arrive in an unpredictable order
    shuffle(reports)

    # Print the whole data set to the shell window, laid out
    # one month per line
    print("The monthly reports to be visualised are:\n")
    print(str(reports).replace(' [', '\n [') + '\n')
    # Return the data set to the caller
    return reports

