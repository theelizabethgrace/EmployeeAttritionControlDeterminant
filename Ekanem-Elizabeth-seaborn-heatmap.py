import numpy as np
import pandas as pd
from scipy import stats
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gapminder-FiveYearData.csv")
print(df)
df2 = df.pivot_table(index='continent', columns='year', values='lifeExp')
print(df2)

sns.heatmap(df2).get_figure().savefig("heatmap1.png")
