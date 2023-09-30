from die import Die
import matplotlib.pyplot as plt
import numpy as np


#create two D6.
die_1 = Die()
die_2 = Die()

#make some rolls, store the results in a list.
results = [die_1.roll() + die_2.roll() for roll_number in range(1000)]

#analyze the results
max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_results+1)]

#visualize the results.
x_values = list(range(2, max_results+1))

#plot
fig, ax = plt.subplots()
ax.bar(x_values, frequencies, width=1, edgecolor="white", linewidth=0.7)

plt.show()



