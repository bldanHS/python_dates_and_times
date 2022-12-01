#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("today is ", today)


    # TODO: print out the date's individual components
    print("date components:", today.year, today.month, today.day)

    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("todays weekday: ", today.weekday())
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("Today is:", days[today.weekday()])

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("Today's exact date is: ",today)

    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("Today's time is: ", t)

 

  
if __name__ == "__main__":
    main()
  