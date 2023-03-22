#calculates if it's breakfast time, lunch time or dinner time based on the current tiem
def main():
    time = (input("What time is it? "))
    convert(time)



#takes a time as input and returns if it's time for breakfast, lunch or dinner (or none of these)
def convert(time):

    hours, minutes = time.split(":")

    hours =int(hours)

    if (hours >= 7 and hours <=8):
        print("breakfast time")
    elif (hours >= 12 and hours <= 13):
        print("lunch time")
    elif (hours >= 18 and hours <= 19):
        print("dinner time")

    minutes = int(minutes)

    minutes2 = int(minutes)

    minutes2 = ((minutes2 * 1.67))

    minutes2 =int(minutes2)

    hours2= str(hours)
    minutes2 = str(minutes2)

    if (minutes == 30):
        return (hours2+".5")
    else:
        return (hours2+"."+minutes2)

if __name__ =="__main__":
    main()





