# File main 


from myConvexhull import getMaxPoint
from myConvexhull import myConvexHull
import myConvexhull
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
data = datasets.load_iris()


df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)


#visualisasi hasil ConvexHull
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])


for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = myConvexhull.myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    xval = [0 for i in range(len(hull)+1)]
    yval = [0 for i in range(len(hull)+1)]
    if (i >= 1):
        hull.pop(len(hull)-1)
        xval.pop(1)
        yval.pop(1)
    for j in range(len(hull)):
        xval[j] = hull[j][0]
        yval[j] = hull[j][1]
    xval[len(hull)] = xval[0]
    yval[len(hull)] = yval[0]
    plt.plot(xval, yval, colors[i])
plt.show()

