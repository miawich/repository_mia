import csv
import matplotlib.pyplot as plt
import numpy as np

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)


header = data.pop(0)
print(header)

# scatter of firearms per 100 against homicides per 100k

homicide_100k = []
firearms_100 = []
countries = []
similar = ["Canada", "England and Wales", "Japan", "South Korea", "France", "Germany", "Ireland", "Singapore", "Hungary",
           "Taiwan", "Israel", "Belgium", "Finland", "Switzerland", "Netherlands", "United States"]

data = [x for x in data if x[0] in similar]

for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        countries.append(name)
    except:
        print(country[0], "data is inadequate")


plt.figure("Homicides per Firearm Worldwide", figsize=(10, 6))
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homicides per 100k population")
plt.xlabel("firearms per 100 people")
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(firearms_100[i], homicide_100k[i]))
plt.show()