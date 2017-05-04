import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

twitter_data = pd.read_csv('result.csv')
print (twitter_data.corr())

plt.figure()
hist1,edges1 = np.histogram(twitter_data.friends)
plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])

plt.scatter(twitter_data.followers,twitter_data.retwc)