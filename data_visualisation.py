
"""Data Visualisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14xeeWDERbJ8cWX2ThcMyAFPEj0UuLgC4
"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

# Data for Population Example
years = [1960,1970,1980,1990,2000,2010,2016]
pop = [21.91,28.51,38.67,56.23,66.13,74.57,80.28]

# Line Plot
plt.plot(years, pop)
plt.show()

plt.figure(figsize=(9,6), dpi=100)
plt.plot(years, pop, color="green")
plt.xlabel('Year')
plt.ylabel("Population")
plt.title("Country Population")
plt.yticks([21.91,28.51,38.67,56.23,66.13,74.57,80.28],
           ['21M', '28M', '38M', '56M', '66M', '74M', '80M'])
plt.show()

# Scatter Plot
plt.scatter(years, pop)
plt.show()

popsize = np.array(pop) * 4
plt.scatter(years, pop, s=popsize, color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Country Population')
plt.yticks([21.91,28.51,38.67,56.23,66.13,74.57,80.28],
           ['21M', '28M', '38M', '56M', '66M', '74M', '80M'])
plt.show()

# Bar Chart Example
t1 = [1, 3, 4, 5, 6, 7, 9]
tt1 = [4, 7, 10, 4, 7, 8, 3]

t2 = [2, 4, 6, 8, 10]
tt2 = [5, 6, 2, 6, 2]

plt.bar(t1, tt1, label="Blue Bar", color='b')
plt.bar(t2, tt2, label="Green Bar", color='g')
plt.xlabel('Bar number')
plt.ylabel('Bar height')
plt.title('Bar Chart Example')
plt.legend()
plt.show()

# Histogram Plot Example
cit_name = ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Tabriz', 'Shiraz']
city_pop = [7153309, 2307177, 1947164, 1448075, 1424641, 1249942]

plt.hist(city_pop)
plt.xlabel('Population')
plt.ylabel('City number')
plt.show()

# Pie Chart
plt.pie(city_pop, labels=cit_name, autopct='%1.1f%%')
plt.show()

# Horizontal Bar Chart
height = [5.8, 12.2, 21.5]
bars = ['Gruber & Narayanan (2019)', 'Konig & Conway (2016)', 'Conway et al. (2017)']

plt.barh(bars, height)
plt.xlabel('Distance (KM)')
plt.ylabel('References')
plt.title("Average Daily Distance (KM)")
plt.show()

# Seaborn Visualizations with Pandas

# Reading CSV data
smartphone = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data set/smartphones.csv")

# Swarm Plot
plt.figure(figsize=(13, 8))
sb.swarmplot(x="OS", y="Capacity", data=smartphone, hue="OS", size=20)
plt.show()

# Box Plot
sb.boxplot(x='Company', y='Ram', data=smartphone)
plt.show()
