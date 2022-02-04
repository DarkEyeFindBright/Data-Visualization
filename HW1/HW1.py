import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import seaborn as sns

df = pd.read_excel('table-1.xls')
print(df)
plt.rcParams['figure.figsize'] = (12.0, 8.0)
violate_crime = df.loc[10:19, ['Year', 'Violent\ncrime']]
print(violate_crime)
fig, ax = plt.subplots()
ax.bar(violate_crime['Year'], violate_crime['Violent\ncrime'].div(1000), width=1, edgecolor="white", linewidth=0.7)
plt.xlabel('Year')
plt.ylabel('Number(In thousands)')
plt.title('Number of Violent Crime In United States from 2007-2016')
x_major_locator = MultipleLocator(1)
ax.xaxis.set_major_locator(x_major_locator)
plt.savefig('1.jpg')

fig, ax = plt.subplots()
data_2016 = df[19:]
data_2016 = data_2016[
    ['Violent\ncrime', 'Murder and\nnonnegligent\nmanslaughter', 'Property\ncrime', 'Rape\n(legacy\ndefinition)',
     'Robbery', 'Aggravated\nassault', 'Burglary', 'Larceny-\ntheft',
     'Motor\nvehicle\ntheft']]
data_2016 = data_2016.values.tolist()
ax.pie(data_2016[0],
       labels=['Violent Crime', 'Murder and nonnegligent manslaughter', 'Property crime', 'Rape (legacy definition)',
               'Robbery', 'Aggravated assault', 'Burglary', 'Larceny-theft',
               'Motor vehicle theft'], explode=(0, 0.2, 0, 0.2, 0.2, 0, 0, 0, 0), autopct='%.2f%%')
ax.legend(loc=2, bbox_to_anchor=(0.9, 0.2), borderaxespad=0.)
plt.title('Percentage of all types of crime in the United States in 2016')
plt.savefig('2.jpg')

plt.rcParams['figure.figsize'] = (12.0, 10.0)
fig, ax = plt.subplots()
Rape = df.loc[10:19, ['Rape\n(legacy\ndefinition)']]
Muder = df.loc[10:19, ['Murder and\nnonnegligent\nmanslaughter']]
robbery = df.loc[10:19, ['Robbery']]
year = df.loc[10:19, ['Year']]
ax.plot(year,Rape,color="deeppink",linewidth=2,linestyle=':',label='Rape (legacy definition)', marker='o')
ax.plot(year,Muder,color="darkblue",linewidth=1,linestyle='--',label='Murder and nonnegligent manslaughter', marker='+')
ax.plot(year,robbery,color="goldenrod",linewidth=1.5,linestyle='-',label='Robbery', marker='*')
ax.xaxis.set_major_locator(x_major_locator)
plt.title('Number of three types of crimes in the United States from 2007 to 2016')
plt.xlabel('Year')
plt.ylabel('Number')
plt.legend(loc=2, bbox_to_anchor=(0.75, -0.03))
plt.savefig('3.jpg')