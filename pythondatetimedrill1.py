
# Python version 2.7.13
# Author: Gavin Bramley
# Python Drill datetime
# Based on the current time in Portland find out if the New York City
# and London branches are open or closed.

import datetime

now=datetime.datetime.today()


NYCtime = now + datetime.timedelta (hours=3)
LONDONtime = now + datetime.timedelta (hours=8)

if (NYCtime.hour >=9 and NYCtime.hour <= 21):
    print ('The New York Office is Open')
else:
    print ('The New York Office is Closed')

if (LONDONtime.hour >=9 and LONDONtime.hour <=21):
    print ('The London Office is Open')
else:
    print ('The London Office is Closed')