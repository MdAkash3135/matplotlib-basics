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
