from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')


slices = [60, 40]
labels = ['Sixty', 'Forty']
colors = ['#ff9999','#66b3ff']

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
# plt.title("Pie Chart Example")
# plt.tight_layout()
# plt.show()


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java' ]

explode = [0, 0 , 0, 0.5, 0]

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', startangle=90, explode=explode, shadow=True, colors=colors)
plt.title("Most Popular Languages in 2024")
plt.tight_layout()
plt.show()