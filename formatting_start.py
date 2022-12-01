#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now()


    
    #### Date Formatting ####
    print(now.strftime("The current year and month is: %Y" ))
    print(now.strftime("%B, %d, %a"))
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month (number)


    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("The local date is: %x"))
    print(now.strftime("The local time is: %X"))
    print(now.strftime("The local date and time is: %c"))



    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("The local time is: %I:%M:%S "))
    print(now.strftime("The local time is: %H:%M %p"))
  


if __name__ == "__main__":
    main()
