import matplotlib.pyplot as plt
import csv

with open("Libraries_-_2019_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(len(data))
headers = data.pop(0)
print(headers)

data.sort(key=lambda x: int(x[-1]))
print(data)

library_names = [x[0] for x in data]
print(library_names)

monthly_data = [x[4:-1] for x in data]
print(monthly_data)

print()

my_library = monthly_data[library_names.index('Lincoln Park')]
my_library = [int(x) for x in my_library]
print(my_library)

plt.figure(1, tight_layout=True)
month_numbers = [x for x in range(12)]
month_names = headers[4:-1]

# plt.plot(month_numbers, my_library)
plt.bar(month_numbers, my_library, color='darkgreen', edgecolor='hotpink')
plt.xticks(month_numbers, month_names, rotation=45)  # replaces shown values on the graph axis
plt.axis([-1, 12, 0, 16000])
plt.title("Lincoln Park Library Visitors 2019", fontsize=20)
plt.ylabel("number of visitors")


# plot every library in chicago year to data visitors on a bar graph
plt.figure(2, tight_layout=True, figsize=(14, 6))
# get library totals
ytd_totals = [int(x[-1]) for x in data]
print(ytd_totals)
library_numbers = [x for x in range(len(library_names))]

plt.barh(library_numbers, ytd_totals, color='green')
plt.yticks(library_numbers, library_names, fontsize=6)
plt.title("annual library visitors")
plt.xlabel("total visitors")
plt.show()
