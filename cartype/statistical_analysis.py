#1. Notebook Preparation

##1.1 importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import statsmodels.api as sm
import math
import stats
from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import chisquare

##1.2 importing files
df = pd.read_csv('cartype CSV.csv')
data = df

#2. Cleaning Dataset
##2.1 Missing Values / Erros
data.info()

##2.2  Duplicates Values
duplicate_rows_df = data[data.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)
data = data.drop_duplicates()
data.count()

##2.3 Dropping irrelevant Columns
data = data.drop(['Mfr Name', 'Model Year'], axis=1)

##2.6  Dropping Null Values
print(data.isnull().sum())

##2.5  Outliers
#Boxplot to visualize data
fig = plt.figure(figsize=(11, 7))
sns.boxplot(y=data['Combined FE'], legend="full")
#plt.show()

#Function to detect Outliers in Combined FE Column
outliers = []
data['Combined FE'] = sorted(data['Combined FE'])
q1 = np.quantile(data['Combined FE'], 0.25)
q3 = np.quantile(data['Combined FE'], 0.75)
IQR = q3-q1
lwr_bound = q1-(1.5*IQR)
upr_bound = q3+(1.5*IQR)

for i in data['Combined FE']:
    if i < lwr_bound or i> upr_bound:
        outliers.append(i)

print(outliers)

#As suggested technique in this case. The Outliers will be replaced by the mean rather than delete them
median_FE = np.median(data['Combined FE'])
print(median_FE)
for i in outliers:
    data['Combined FE'] = np.where(data['Combined FE'] == i, 23, data['Combined FE'])

fig = plt.figure(figsize=(11, 7))
sns.boxplot(y=data['Combined FE'], legend="full")
plt.show()

#3  Data Analytical Method
##3.1  Descriptive Statistic Analysis
print(data['Combined FE'].describe())

##3.2  Test of Normality
##Create a Histogram
plt.hist(data['Combined FE'], edgecolor='black',bins=20)
#plt.show()
#From de Grpah we could be a Normal distribution data

##Create a Q-Q pLot
sm.qqplot(data['Combined FE'], line='45')
#plt.show()
#We can see the data is not normal distributed

##Perform Shapiro-Wilk Test
print(shapiro(data['Combined FE']))
#As the P-value is less than 0.05. Then we reject the null hypothesis since we dont have sufficient evidence to say that sample does not come from a normal distribution

##Perform Kolmogorov Test
print(kstest(data['Combined FE'], 'norm'))
#Since the p-value is less than .05, we reject the null hypothesis of the Kolmogorov-Smirnov test. This means we have sufficient evidence to say that the sample data does not come from a normal distribution.

##3.3  Pearson Linear Correlation Coefficient
#Using Heatmap to analyse correlations

plt.figure(figsize=(10,5))
data_numerical = data.drop(['Division', 'Carline', 'Transmission', 'Air Aspiration Method', 'Transmission Description', 'Drive Desc', 'Carline Class Desc', 'Release Date'], axis=1)
c= data_numerical.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
plt.show()

#Strong negative correlation between Combined FE with Engine Displacement, No of Cylinders, and Combined FE.
#Weak negative correlation between Combined FE and No Gears.
#Strong positive correlation between Combined CO2 and Engine Displacement and No of Cylinders.
#Weak positive correlation between Combined FE and No Gears

##3.4  Chi-Square Test
#Using test for categorical data and find correlations
result = chisquare(f_obs=data['Combined FE'])
print(result)

##3.5  Graphical Analysis of Variables Associated


#Export Data
#data.to_excel('C:\Other test\cartype\Data.Pandas.xlsx')