import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and both high andlow temperatures from this file.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))
  
#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#low graph syle is blue
fig, ax = plt.subplots()
ax.plot(dates, lows, c='blue')

# Open program with instructions on how to use the menu
print("Welcome to the Sitka Weather Program!")
print("Use the menu to navigate through different options.")

# Promt user if they want to see highs, lows, or exit the program
while True:
    print("\nMenu:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1' or choice == 'high':
        # Plot the high temperatures.
        plt.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == '2' or choice == 'low':
        # Plot the low temperatures.
        plt.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == '3' or choice == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select an option from the menu.")

plt.show()