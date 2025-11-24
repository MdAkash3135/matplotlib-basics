from matplotlib import pyplot as plt

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [50000, 51000, 52000, 53000, 53437, 76373, 82316, 84928, 87317, 88748, 83752]

plt.plot(dev_x, dev_y, '--' , color='#444444' , label = "All Developers")
plt.plot(dev_x, py_dev_y,'b', color = "#9a675a" ,label = "Python Developers")



plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")


plt.legend(["All Developers", "Python Developers"])

plt.show()