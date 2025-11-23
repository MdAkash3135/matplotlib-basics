import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,5,6]
plt.plot([1,2,3], [4,5,6])
plt.show()


x = [1,2,3]
y = [4,5,6]
plt.plot(x,y)
plt.title("Our first Graph", fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 20})
plt.xlabel("X Axis ! ")
plt.ylabel("Y axis")
plt.show()


x = [1,2,3]
y = [4,5,6]
plt.plot(x,y)
plt.title("Our first Graph", fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 20})
plt.xlabel("X Axis ! ")
plt.ylabel("Y axis")

plt.xticks(x)
plt.yticks(y)

plt.show()



x = [1,2,3]
y = [2,4,6]

plt.figure(figsize= (5,3), dpi=100)
plt.plot(x,y, label='3x', color='r', marker='.')

# plt.title("Our first Graph", fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 20})
 

plt.xlabel("X Axis ! ")
plt.ylabel("Y axis")

plt.xticks(x)
plt.yticks(y)

### Line number 2  

x2 = np.arange(0, 4.5, 0.5)
plt.plot(x2, x2**2)

plt.legend()

plt.savefig('akash.png')

plt.show()



### Bar Graphs

labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values)

bars[0].set_hatch('/')
bars[2].set_hatch('*')
bars[1].set_hatch('O')

patterns = ['/', '*', 'O']

for bar in bars:
  bar.set_hatch(patterns.pop(0))

plt.figure(figsize=(6,4))
plt.show()

#Real World Example
gas = pd.read_csv('gas_prices.csv')


plt.title("Gas price Over country's")
plt.plot(gas.Year, gas.USA, 'b.-',  label='USA')
plt.plot(gas.Year, gas.Japan, 'r.-', label='Japan')
plt.plot(gas.Year, gas['South Korea'], 'c.-' ,label='South Korea')



for gas_obj in gas:
  if gas_obj != 'Year':
    plt.plot(gas.Year, gas[gas_obj])

plt.xticks(gas.Year[:: 3])

plt.yticks([0, 1, 2 , 3 ,4 ,5])

plt.xlabel("Year")

plt.ylabel("US Dollars")

plt.legend()

plt.show()