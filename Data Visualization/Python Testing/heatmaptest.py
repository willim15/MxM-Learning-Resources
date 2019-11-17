import numpy as np

# get correlation matrix
corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")


'''
Loop this way instead
'''
# get correlation matrix
test2 = iris.corr()
fig, bx = plt.subplots()
new = bx.imshow(test2.values)

# set labels
ax.set_xticks(np.arange(len(test2.columns)))
ax.set_yticks(np.arange(len(test2.columns)))
ax.set_xticklabels(test2.columns)
ax.set_yticklabels(test2.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(test2.columns)):
    for j in range(len(test2.columns)):
        text = ax.text(j, i, np.around(test2.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")