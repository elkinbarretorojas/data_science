#Importing files
import numpy as np
import pandas as pd
df = pd.read_csv('cartype CSV.csv')
data = df

#Preaparation and Cleaning Dataset

#Find Missing Values / Erros
#data.info()
#No null numbers found

#Find Duplicates Values
print(data.describe())

