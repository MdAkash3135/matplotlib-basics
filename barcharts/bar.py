from matplotlib import pyplot as plt
import numpy as np
print(plt.style.available)

# plt.xkcd()  # use xkcd style




plt.style.use('Solarize_Light2')
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_ages = np.arange(len(dev_x))

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [50000, 51000, 52000, 53000, 54437, 55373, 83160, 84928, 87317, 88748, 83752]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62316, 64928, 67317, 68748, 68748]

plt.bar(x_ages, dev_y, label = "All Developers")
plt.bar(x_ages + 0.25, py_dev_y, width=0.25, label = "Python Developers")
plt.bar(x_ages + 0.50, js_dev_y, width=0.25, label = "JavaScript Developers")

plt.xticks(x_ages, dev_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.legend()
plt.show()