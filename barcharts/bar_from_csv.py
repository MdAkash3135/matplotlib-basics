import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

plt.style.use('Solarize_Light2')

# with open('/home/hubartech/Documents/ML_AI/matplotlib-basics/datasets/fifa_data.csv', encoding='utf-8-sig') as csvfile:
#     data = csv.DictReader(csvfile)

#     languages_counter = Counter()

csv_data = pd.read_csv('/home/hubartech/Documents/ML_AI/matplotlib-basics/datasets/fifa_data.csv', encoding='utf-8-sig')
data = csv_data['LanguagesWorkedWith']

languages_counter = Counter()

for d in data:
    languages_counter.update(d.split(';'))

print(languages_counter.most_common(1))

languages = []
popularity = []

for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title('Most Popular Programming Languages in 2019')
plt.xlabel('Number of People Who Use')
plt.ylabel('Programming Languages')
plt.tight_layout()
plt.show()
