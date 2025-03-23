import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File to store fitness data
DATA_FILE = "fitness_data.csv"

# Load existing data or create a new DataFrame
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Date", "Steps", "Calories_Burned", "Distance_km", "Heart_Rate"])

# Function to input fitness data
def input_data():
    print("\n--- Enter Your Fitness Data ---")
    date = input("Enter date (YYYY-MM-DD): ")
    steps = int(input("Enter steps taken: "))
    calories = float(input("Enter calories burned: "))
    distance = float(input("Enter distance traveled (km): "))
    heart_rate = int(input("Enter average heart rate: "))
    
    # Append data to DataFrame
    global df
    df.loc[len(df)] = [date, steps, calories, distance, heart_rate]
    df.to_csv(DATA_FILE, index=False)  # Save data to CSV
    print("Data saved successfully!")

# Function to view all fitness data
def view_data():
    if df.empty:
        print("\nNo data found. Please input some data first.")
    else:
        print("\n--- Your Fitness Data ---")
        print(df)

# Function to visualize steps over time
def plot_steps():
    if df.empty:
        print("\nNo data found. Please input some data first.")
    else:
        plt.figure(figsize=(10, 5))
        plt.plot(df["Date"], df["Steps"], marker='o', color='b', label="Steps")
        plt.xlabel("Date")
        plt.ylabel("Steps")
        plt.title("Daily Steps Over Time")
        plt.grid(True)
        plt.legend()
        plt.show()

# Function to visualize calories burned over time
def plot_calories():
    if df.empty:
        print("\nNo data found. Please input some data first.")
    else:
        plt.figure(figsize=(10, 5))
        plt.plot(df["Date"], df["Calories_Burned"], marker='o', color='r', label="Calories Burned")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.title("Daily Calories Burned Over Time")
        plt.grid(True)
        plt.legend()
        plt.show()

# Main program loop
def main():
    while True:
        print("\n--- Personal Fitness Tracker ---")
        print("1. Input Fitness Data")
        print("2. View All Fitness Data")
        print("3. View Steps Graph")
        print("4. View Calories Burned Graph")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            input_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            plot_steps()
        elif choice == "4":
            plot_calories()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()