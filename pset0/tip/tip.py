#calculates tip for a meal based on a given tip percentage

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    dollars_to_float(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    percent_to_float(percent)
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = str(dollars)
    dollars = dollars.replace("$", "")
    dollars  = float(dollars)
    return(dollars)


def percent_to_float(percentage):
    percentage = str(percentage)
    percentage =percentage.replace("%", "")
    percentage = float(percentage)
    return percentage

main()
