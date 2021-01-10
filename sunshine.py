import matplotlib.pyplot as plt
import pandas as pd


# import some data to play with
data = pd.read_csv('C:/Users/44792/Desktop/England.txt',sep="\t", header=0)
england_sun = pd.DataFrame(data)

x = england_sun.iloc[:,0]
y = england_sun.iloc[:,17]

fig = plt.figure()
plt.plot(x, y)
plt.ylabel("Annual sunshine duration (hours)")
plt.xlabel("Year")
plt.show()

