import datetime
"""Write a Python program to subtract five days from current date."""
'''
d1 = datetime.date(2023,2,23)
delta1 = datetime.timedelta(5)
print(d1-delta1)
'''
"""Write a Python program to print yesterday, today, tomorrow."""
'''
d2 = datetime.date.today()
delta2 = datetime.timedelta(1)
print("Yesterday: "+ str(d2-delta2)+
"\nToday: "+str(d2)+"\nTomorrow: "+str(d2+delta2))
'''
"""Write a Python program to drop microseconds from datetime."""
''''
d3 = datetime.datetime(2023,2,23,5,6,microsecond=150000)
d3-=datetime.timedelta(microseconds=d3.microsecond)
print(d3)
'''
"""Write a Python program to calculate two date difference in seconds."""
'''
d4 = datetime.datetime(2023,2,22,5,6)
d5 = datetime.datetime(2023,2,23,5,6)
print((d5-d4).total_seconds())
'''

