#1. Notebook Preparation

##1.1 importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

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
fig = plt.figure(figsize=(10, 7))
plt.boxplot(data['Combined FE'])
plt.show()

#3  Data Analytical Method


##3.1  Descriptive Statistic Analysis


##3.2  Test of Normality


##3.3  Pearson Linear Correlation Coefficient


##3.4  Chi-Square Test


##3.5  Graphical Analysis of Variables Associated

