#1. Notebook Preparation

##1.1 importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##1.2 importing files
df = pd.read_csv('cartype CSV.csv')
data = df

#2. Cleaning Dataset
##2.1 Missing Values / Erros
data.info()

##2.2  Duplicates Values
duplicates_values = data.duplicated()
data.drop_duplicates()
data.describe()

##2.3  Outliers
#Boxplot to visualize data
fig = plt.figure(figsize=(11, 7))
sns.boxplot(y=data['Combined FE'], legend="full")
plt.show()

#Function to detect Outliers in Combined FE Column
outliers = []
def detect_outliers_iqr(data_sample):
    data_sample = sorted(data_sample)
    q1 = np.quantile(data_sample, 0.25)
    q3 = np.quantile(data_sample, 0.75)
    IQR = q3-q1
    lwr_bound = q1-(1.5*IQR)
    upr_bound = q3+(1.5*IQR)
    for i in data_sample:
        if i < lwr_bound or i> upr_bound:
            outliers.append(i)
    return outliers
sample_outliers = detect_outliers_iqr(data['Combined FE'])
print(sample_outliers)

#As suggested technique in this case. The Outliers will be replaced by the mean rather than delete them
median_FE = np.median(data['Combined FE'])
print(median_FE)
for i in sample_outliers:
    c = np.where(data['Combined FE'] == i, 23, data['Combined FE'])

fig = plt.figure(figsize=(11, 7))
sns.boxplot(y=c, legend="full")
plt.show()


#3  Data Analytical Method


##3.1  Descriptive Statistic Analysis


##3.2  Test of Normality


##3.3  Pearson Linear Correlation Coefficient


##3.4  Chi-Square Test


##3.5  Graphical Analysis of Variables Associated


#Export Data
data.to_excel('C:\Other test\cartype\Data.Pandas.xlsx')