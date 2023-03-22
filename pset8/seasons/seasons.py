from datetime import datetime, timedelta

import sys

import inflect

p = inflect.engine()

from datetime import date



def main():
    your_birthday = input("Enter your birthday ")
    get_time(your_birthday)

def get_time(your_birthday):
    try:

        year = int(your_birthday[0:4])
        month = int(your_birthday[5:7])
        day =int(your_birthday[8:10])


        day_today =date.today()


        your_date =date(year, month, day)

        difference = day_today - your_date
        minutes = (difference.days * 24 * 60)

        words = (p.number_to_words(minutes, andword="") + " minutes")
        print(words.capitalize())
        return 0
    except ValueError:
        print("Not a valid date")
        sys.exit (1)

if __name__ == "__main__":
    main()