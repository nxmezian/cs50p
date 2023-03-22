#orders list of name for Hogwarts letter

import sys

import csv

try:
#check for right amount of cmdln args
    if len(sys.argv) == 3:

#creates dictionary with names and houses of Hogwarts students
            students =[]

#opens csv file, reads from it and appents output to student[]
            with open (sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    #splits first name from last name
                            surname_name = row["name"].split(",")
                            students.append({"first": surname_name[1].lstrip(), "last": surname_name[0], "house": row ["house"]})

#writes to a new csvfile after sorting input from previously inputted csv file
            with open (sys.argv[2], "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
                writer.writerow({"first": "first", "last": "last", "house":"house"})

                for row in students:
                    writer.writerow({"first": row["first"], "last": row["last"], "house":row["house"]})


    elif len(sys.argv) >3:
        print("Too many command-line arguments")
        sys.exit(1)


    else:
        print("Too few command-line arguments")
        sys.exit(1)


except FileNotFoundError:
    print("Could not read invalid_file.csv")
    sys.exit(1)













