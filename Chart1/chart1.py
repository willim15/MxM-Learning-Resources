import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('HotStuff.csv')
plt.imshow(df, cmap='hot', interpolation = 'nearest')
plt.show()