#tabulates the content of a given csv file

import sys

from tabulate import tabulate

import csv

#input name of csv via cmdln arg, tabulate and print

try:
    if len(sys.argv) >2:
        print("Too many command-lines arguments")
        raise 1

    if sys.argv[1].endswith(".csv"):
        reader =csv.reader(open(sys.argv[1], "r"))

        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    else:
        print("Not a CSV file")
        raise 1

except IndexError:
    print("Too few command-line arguments")
    raise 1

except FileNotFoundError:
    print("File does not exist")
    raise 1
