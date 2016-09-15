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

# ~Simple Linear Regression~ #

## Method 1 : Statsmodels  ##

import statsmodels.formula.api as smf
lm = smf.ols('Sales ~ TV',data = data).fit()
lm.params


X_new = pd.DataFrame({'TV':[50]}) #Statasmodels always use dataframe type as the predicted 
X_new.head()
lm.predict(X_new)

X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
X_new.head()

preds = lm.predict(X_new)
preds

# plot the observed data
data.plot(kind='scatter',x='TV',y='Sales')
# plot the least square line
plt.plot(X_new,preds,c='red',linewidth=2)

lm.conf_int()
lm.pvalues

# how well the model fit- R-squared
lm.rsquared

# ~Multiple Linear Regression~ #
lm = smf.ols(formula = 'Sales ~ TV + Radio + Newspaper' ,data=data).fit()
lm.params
lm.summary()

## Method 2 : Scikit-Learn  ##
feature_cols = ['TV','Radio','Newspaper']
x = data[feature_cols]
y = data.Sales

# sklearn path: import, instantiate, fit
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x,y)

print lm.intercept_
print lm.coef_

zip(feature_cols,lm.coef_)

lm.predict([100,25,25])

lm.score(x,y)





