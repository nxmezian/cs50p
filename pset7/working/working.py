#takes time formatted in AM/PM and converts it to 24-hour format

import re
import sys


def main():
    time_input =input("Hours: ")
    convert(time_input)

def convert(time_input):

    #searches for input in the format of "9 AM to 5 PM"
    time_check = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)$", time_input, re.IGNORECASE)

    #raises value errors if hours is greater than 12 and/or minutes greater than 60
    try:
        if int(time_check[2]) > 12:
            print("incorrect")
            raise ValueError

        if int(time_check[6]) > 12:
            print("incorrect")
            raise ValueError

    #to convert from AM/PM to 24-hours, a given time in PM needs to be increased by 12, this is not necessary for a time in AM
        first_hour_converted = (int(time_check[2]))
        if time_check[4] == ("PM") or time_check[4] == ("pm"):
            if int(time_check[2]) == 12:
                first_hour_converted = 12
            else:
                first_hour_converted = (first_hour_converted + 12)

        second_hour_converted = int(time_check[6])
        if time_check[8] == ("PM") or time_check[8] == ("pm"):
            if int(time_check[6]) == 12:
                second_hour_converted = 12
            else:
                second_hour_converted = (second_hour_converted + 12)

    #adds both converted times together in a single string
        converted_time = (f"{first_hour_converted:02}:00 to {second_hour_converted:02}:00")
        print(converted_time)
        return converted_time

    except:
        raise ValueError


if __name__ == "__main__":
    main()


