#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=12, minutes=31, seconds=60))


# TODO: print today's date
presentDate = datetime.now()
print("today is:", presentDate)


# TODO: print today's date one year from now
print("One year from now it will be: ", str(presentDate + timedelta(days=365)))


# TODO: create a timedelta that uses more than one argument
print("In three weeks and 4 days from now, it will be: ", str(presentDate + timedelta(weeks=3, days=4)))


# TODO: calculate the date 1 week ago, formatted as a string
pt = datetime.now()
pts = pt.strftime("%Y, %b %d")
print("Today is: ", pts)
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%Y, %b, %d")
print("One week ago the date was: ", s )


### How many days until April Fools' Day?

mavan = date.today()
print(mavan)
dec6 = date(mavan.year, 12, 6)



# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

if dec6 < mavan:
    print("december 6 mar elmult")
else:
    napok_dec6ig = dec6 - mavan
    print("December 1 ", ((dec6 - mavan).days), "mulva lesz")


# TODO: Now calculate the amount of time until April Fool's Day  

