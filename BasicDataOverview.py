## Import the Libraries ##
import pandas as pd
import matplotlib.pyplot as plt
# plot only appears in the jupyter notebook
%matplotlib inline

## Read data into a DataFrame ##
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)
data.head()
data.shape

##Plot the relationship ##
fig, axs = plt.plot(1,3,sharey=True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])
