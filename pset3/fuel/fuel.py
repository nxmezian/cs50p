#takes current amount of car fuel as a fraction and returns E, F or a percentage
while True:
    try:
        while True:
            fraction = (input("input fraction "))
            x, y = fraction.split("/")
            if int(x) <= int(y): break


        if (int(int(x)/int(y)*100)) >= 99:
                print("F")
                break

        elif (int(x)/int(y)*100) <=1:
                print("E")
                break
        else:
                print(round(float(float(x)/float(y)*100)), "%", sep="")
                break

    except (ValueError, ZeroDivisionError):
        print("try again")





