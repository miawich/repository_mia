'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''

import csv

with open("Season_Stats.csv") as f:
    data = csv.reader(f)
    data = list(data)

print(data[0])

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
# header = data.pop(0)
# print(header)
# print()
#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
'''
data.sort(key=lambda x: x[-1])

top_ten_player = data[-10:]
print(top_ten_player)
#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
career_points = 0

for item in data:
    if item[2] == 'Kobe Bryant':
        career_points += item[-1]

print(career_points)
print()

#4  What player has the most 3point field goals in a single season. (3pts)
# data.sort(key=lambda x: x[-19])
print(data[-1])

#5  One stat featured in this data set is Win Shares(WS).
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
data.sort(key=lambda x: x[25])

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
'''







