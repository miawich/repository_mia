# Folium train map

# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))


# If you have extra time, try to put some html into the popup.

import folium
import csv
from folium.plugins.beautify_icon import BeautifyIcon

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

brown = folium.plugins.BeautifyIcon
print(data.pop(0))
print(data[1])
location = [eval(x[-1]) for x in data]
names = [str(x[2]) for x in data]

line_color = []
red = [str(x[8]) for x in data]
for i in range(len(red)):
    if red[i] == 'true':
        line_color.append('red')
blue = [str(x[9]) for x in data]
for i in range(len(blue)):
    if blue[i] == 'true':
        line_color.append('blue')
green = [str(x[10]) for x in data]
for i in range(len(green)):
    if green[i] == 'true':
        line_color.append('green')
brown = [str(x[11]) for x in data]
for i in range(len(brown)):
    if brown[i] == 'true':
        line_color.append('#964b00')
purple = [str(x[12]) for x in data]
for i in range(len(purple)):
    if purple[i] == 'true':
        line_color.append('purple')
purp2 = [str(x[13]) for x in data]
for i in range(len(purp2)):
    if purp2[i] == 'true':
        line_color.append('purple')
yellow = [str(x[14]) for x in data]
for i in range(len(yellow)):
    if yellow[i] == 'true':
        line_color.append('yellow')
pink = [str(x[15]) for x in data]
for i in range(len(pink)):
    if pink[i] == 'true':
        line_color.append('pink')
orange = [str(x[-16]) for x in data]
for i in range(len(orange)):
    if orange[i] == 'true':
        line_color.append('orange')

print(line_color)

train_map = folium.Map(location=[41.880443, -87.644107], zoom_start=10.4)

for i in range(len(data)):
    folium.Marker(location=location[i],
                  popup=names[i],
                  icon=folium.plugins.BeautifyIcon(border_color=line_color[i])
                  .add_to(train_map))
train_map.save('train_map.html')
