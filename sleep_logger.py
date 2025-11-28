import pandas as pd
import matplotlib.pyplot as plt
import os

file = "sleep_data.csv"

# Create CSV if not exists
if not os.path.exists(file):
    df = pd.DataFrame(columns=["date","sleep_hours","screen_time_hours","mood","energy_level"])
    df.to_csv(file, index=False)

print("\nSleep Pattern Logger & Analyzer")
print("Type 'add' to enter data")
print("Type 'analyze' to view reports and charts")
print("Type 'exit' to quit\n")

while True:
    command = input("Enter command: ").lower()

    if command == "add":
        date = input("Enter date (YYYY-MM-DD): ")
        sleep = float(input("Enter sleep hours: "))
        screen = float(input("Enter screen time (hours): "))
        mood = int(input("Enter mood (1-10): "))
        energy = int(input("Enter energy level (1-10): "))

        new_data = pd.DataFrame([[date, sleep, screen, mood, energy]],
                                columns=["date","sleep_hours","screen_time_hours","mood","energy_level"])
        new_data.to_csv(file, mode='a', header=False, index=False)
        print("Data Saved!\n")

    elif command == "analyze":
        df = pd.read_csv(file)
        df['date'] = pd.to_datetime(df['date'])
        print("\nCorrelation Matrix:\n")
        print(df.corr())

        # Plot graphs
        plt.figure()
        plt.plot(df['date'], df['sleep_hours'])
        plt.xlabel("Date")
        plt.ylabel("Sleep Hours")
        plt.title("Sleep Duration Over Time")
        plt.show()

        plt.figure()
        plt.scatter(df['screen_time_hours'], df['sleep_hours'])
        plt.xlabel("Screen Time (Hours)")
        plt.ylabel("Sleep Hours")
        plt.title("Screen Time vs Sleep Duration")
        plt.show()

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid Command! Try again.\n")
