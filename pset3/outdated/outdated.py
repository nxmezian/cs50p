import string

#prompts user for a date in month-day-year format and returns it in year-month-day format

#take date as input, reject if not in month-day-year

months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#takes dd-mm-yyyy

while True:

    try:
            date =input("Date: ").replace(",", "")

            date_new = date.split("/")
            if int(date_new[0]) <0 or int(date_new[0]) >12:
                continue
            if int(date_new[1]) <0 or int(date_new[1]) >31:
                continue
            print(date_new[2],"-",(f'{int(date_new[0]):02}'),"-",(f"{int(date_new[1]):02}"), sep="")
            break

    except (IndexError, ValueError, TypeError):
        continue

