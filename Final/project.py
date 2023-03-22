import sys
import csv
from os.path import exists as file_exists
import pandas as pd
import matplotlib.pyplot as plt
import re

def main():
    intro()

def intro():

    print("Welcome to SportsWeight! In this program you can enter your personal stats in the sports of your choosing and keep track of your weight.\n ")

    while True:
        intro_option = input("Enter 1 to log in; enter 2 to create an account; enter 3 for a single-use account\n")
        if intro_option == '1':
            login()
            break
        elif intro_option == '2':
            credentials()
            break
        else:
            username = "temp"
            main_menu(username)

def credentials():
    while True:
        username = input("Enter username of 4 characters or more: ")
        create_username(username)
        if create_username(username) == 0:
            break
        else:
            print("Error: your username was not 4 characters or longer")


    while True:
        password = input("Enter a password of 8 characters or more using a combination of numbers and letters: ")
        create_password(password)
        password_complexity(password)
        if create_password(password) == 0 and password_complexity(password) == 0:
            break
        else:
            print("Error: your password was shorter than eight characters or it did not contain a combination of numbers and letters")

    with open("credentials.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    login()

def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row == [username,password]:
                    main_menu(username)
                else:
                    print("Incorrect login credentials")
                    sys.exit()

def create_username(username):
    username = str(username)
    if len(username) < 4:
        return 1
    else:
        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                    if username in row:
                        return 1
        return 0

def create_password(password):
    password =str(password)
    if len(password) < 8:
        return 1
    else:
        return 0

def password_complexity(password):
    if not re.search("[0-9]", password) or not re.search("[a-zA-Z]", password):
        print("Password not complex enough")
        return 1
    else:
        return 0

def main_menu(username):
    print(f"Main menu\nHello {username}")
    username = username
    while True:
        option = input ("Select an option:\n1. Excercise tracker\n2. Weight tracker\n3. Visualize results\n4. Profile\n5. Exit ")

        if option == '1':
            excercise_tracker(username)
            break
        if option == '2':
            weight_tracker(username)

        if option == '3':
            visualize_results(username)
            break
        if option == '4':
            profile(username)
            break
        if option == '5':
            print("Thank you for using Sportsweight")
            option =input("Are you sure you want to exit this program? y/n")
            if "y" in option:
                print("Thank you for using SportsWeight.\n")
                sys.exit()
            else:
                continue

def excercise_tracker(username):
    print(f"Excerces menu\n")

    date_input = input("When did you perform the exercises you wish to input (dd-mm-yyyy) ")

    distance =input("How many KMs did you run? ")

    if file_exists(f"{username}stats.csv"):
        with open(f"{username}stats.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([date_input,distance])

    else:
        with open(f"{username}stats.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(["date","distance"])
            writer.writerow([date_input,distance])

    while True:
        option = input("Return to main menu? y/n \n")

        if 'y' in option:
            return main_menu(username)
        if 'n' in option:
            while True:
                option = input("Would you like to exit the program? y/n \n")
                if 'y' in option:
                    print("Thank you for using SportsWeight.\n")
                    sys.exit(0)
                elif 'n' in option:
                    break

def weight_tracker(username):

    date_input = input("When did you weigh yourself?(dd-mm-yyyy) ")

    weight =input("How much do you weigh? ")

    if file_exists(f"{username}weight.csv"):
        with open(f"{username}stats.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([date_input,weight])

    else:
        with open(f"{username}weight.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(["date","weight"])
            writer.writerow([date_input,weight])

    while True:
        option = input("Return to main menu? y/n \n")

        if 'y' in option:
            return main_menu(username)
        if 'n' in option:
            while True:
                option = input("Would you like to exit the program? y/n \n")
                if 'y' in option:
                    print("Thank you for using SportsWeight.\n")
                    sys.exit(0)
                elif 'n' in option:
                    break


def visualize_results(username):
    username = username

    option =input("Which results would you like to visualize? Enter 1 for running stats; enter 2 for weight stats, enter 3 to return to the main menu ")
    print("visualizes results\n")

    if option =="1":
        if file_exists(f"{username}weight.csv"):
            df = pd.read_csv(f"{username}stats.csv")

            date = df["date"]
            distance = df["distance"]

            plt.plot(date, distance)
            plt.xlabel('date')
            plt.ylabel('KMs of running')

            plt.show()
        else:
            print("Stats not available")

    elif option =="2":
        if file_exists(f"{username}weightstats.csv"):
            df = pd.read_csv(f"{username}weightstats.csv")

            date = df["date"]
            weight = df["weight"]

            plt.plot(date, weight)
            plt.xlabel('Date')
            plt.ylabel('Weight')

            plt.show()
        else:
            print("Stats not available")
    else:
        main_menu(username)

    while True:
        option = input("Return to main menu? y/n \n")
        if 'y' in option:
            return main_menu(username)
        if 'n' in option:
            while True:
                option = input("Would you like to exit the program? y/n \n")
                if 'y' in option:
                    print("Thank you for using SportsWeight.\n")
                    sys.exit(0)
                elif 'n' in option:
                    break

def profile(username):
    print(f"This is your personal profile.\nSelect one of the following options")

    option =input("Enter 1 to view old your inputted profile details; enter 2 to enter profile details ")
    if option == "2":
        with open(f"{username}profile.csv", "w") as file:
            age =input("Enter your age: ")
            weight =input("Enter your weight: ")
            height =input("Enter your height: ")
            bmi = (int(weight))/int(height)
            writer = csv.writer(file)
            writer.writerow(['username,age,weight,weight,bmi'])
            writer.writerow([username,age,height,weight, bmi])

    else:
        if file_exists(f"{username}profile.csv"):
            try:
                df = pd.read_csv(f"{username}profile.csv")

                print(df)
            except:
                print("You do not have any profile stats inputted")
        else:
            print("You do not have any profile stats inputted")

    while True:
        option = input("Return to main menu? y/n \n")

        if 'y' in option:
            return main_menu(username)
        if 'n' in option:
            while True:
                option = input("Would you like to exit the program? y/n \n")
                if 'y' in option:
                    print("Thank you for using SportsWeight.\n")
                    sys.exit(0)
                elif 'n' in option:
                    option =input("Go back to the current screen? y/n ")
                    if 'y' in option:
                        profile(username)



if __name__ == "__main__":
    main()

