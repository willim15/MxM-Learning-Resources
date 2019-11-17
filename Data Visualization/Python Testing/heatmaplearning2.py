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


'''
It turns out that generating a heat map of all the feature variables — feature variables as row headers and column headers, 
and the variable vs itself on the diagonal— is extremely powerful way to visualize relationships between variables in high dimensional space.
For example, a correlation matrix with heat map coloring. 

A covariance matrix with heat map coloring. Even a massive confusion matrix with coloring.
Think less about the traditional use of heat map, but more like color is another dimension that can visually summarize the underlining data.

https://medium.com/data-science-bootcamp/data-visualization-in-machine-learning-beyond-the-basics-baf2cbea8989
'''


#TODO: 
#https://blog.exploratory.io/quick-introduction-to-heatmap-c21a9f9e4644