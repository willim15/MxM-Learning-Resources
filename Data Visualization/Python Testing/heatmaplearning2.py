import matplotlib.pyplot as plt
import pandas as pd

'''
Visualizing models, decision boundaries and prediction results may give hints whether the model is indeed a good fit 
or it is a poor fit for the data. For example, it is high bias to ignore the nature of our data if use a straight line to fit a circular scatter of dots.
'''

#Reading along with heatmap notes
nums = [99, 1, 3, 5, 7,33, 23,684, 13, 3 ,0, 4]
pd.Series(nums).hist(bins=30)
# <matplotlib.axes._subplots.AxesSubplot object at 0x10d340d90>
# returns object in memory
plt.show()
