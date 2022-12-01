import calendar
from datetime import datetime



def countDays(givenYear, givenMonth, givenDay):
    numberOfDays = 0

    listOfWeeks = calendar.monthcalendar(givenYear, givenMonth)
    for week in listOfWeeks:
        if(week[givenDay] != 0):
            numberOfDays += 1
    return numberOfDays
    print(14)






go = True
while(go):
    print("---------------------------")
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    for i, e in enumerate(days):
        print(i, e)
    print("Which day you want to count? press the number of day: (type exit to quit)")

    inputday = input("chosen day's number: ")
    if(inputday == "exit"):
        break
    myday = int(inputday)
    inputyear = input("Chosen year: ")
    myyear = int(inputyear)
    inputmonth = input("Chosen month: ")
    mymonth = int(inputmonth)

    endnumber = countDays(myyear,mymonth,myday)
    print("The number of days in the specified year and month is ", str(endnumber))

