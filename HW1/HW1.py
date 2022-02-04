import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df = pd.read_excel('table-1.xls')
print(df)

violate_crime = df[['Year', 'Violent crime']]

figsize = 11, 9
figure, ax = plt.subplots(figsize=figsize)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax = plt.bar(df['Year'], df['Violent crime'])
plt.show()
if __name__ == '__main__':
    print()
