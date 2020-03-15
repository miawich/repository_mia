# 03/12/20: plotting with matplotlib
import matplotlib.pyplot as plt

plt.figure(1)

plt.plot([1, 2, 3, 3])  # plots y against the index x
plt.plot([1, 2, 3, 4], [12, 8, 2, 1])  # [x points], [y points]
plt.show()

plt.figure(2)

x_points = [x for x in range(1, 11)]
y_points = [y ** 2 for y in x_points]

plt.plot(x_points, y_points, color='green', marker='*', linestyle='--', alpha=1)
plt.show()

# TALUNK (title, axis,lines, units, numbers, key)
plt.title("howdy im depressed now")
plt.xlabel("days of quarantine", color='brown')
plt.axis([0, 11, 0, 110])

plt.show()