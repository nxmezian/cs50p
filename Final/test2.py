import csv

username = 'minglefleur'
password = 'abcdef'

x = (f"{username}:{password}")

with open("credentials.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        usernames = []
        for row in reader:
            usernames.append(row)
            print(usernames)
        if (f"{username}:{password}") == username[0]:
            print("Login succesful")