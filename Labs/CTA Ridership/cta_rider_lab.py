'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''
import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(len(data))
headers = data.pop(0)
print(headers)

data.sort(key=lambda x: int(x[0]))

last_ten = data[-11:]
years = [int(x[0]) for x in last_ten]
rail = [int(x[3]) for x in last_ten]
bus = [int(x[1]) for x in last_ten]
total = [int(x[4]) for x in last_ten]

plt.figure(1, tight_layout=True)
plt.plot(years, rail, color='pink', label='Train')
plt.plot(years, bus, color='blue', label='Bus')
plt.plot(years, total, color='darkgreen', label='Total')

plt.title('CTA Annual Boarding Totals from 2008 to 2018: Train, Bus, and Total')
plt.xlabel('Years')
plt.ylabel('Yearly Total Boardings')

plt.legend()
plt.show()

# HYPOTHESES:
# one thing i would think about is that in 2008 the recession had just hit,
# so it was more affordable to take CTA than own a car
# maybe the city has become more centralized so more people are walk, but it's more likely there are more cars
# when is the more used transport going to switch to trains?
# i guess buses are more popular because they can take you to more exact locations and maybe run more frequently
