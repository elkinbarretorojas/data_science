

# 1. Dataset Explanation

The dataset is structured based on vehicle type and includes the models from the year 2015. Vehicles are listed alphabetically in each carline by brand, division, and model. Additionally, each vehicle type has different features, such as engine displacement, Cylinders, Transmission Type, Air Aspiration method, Gears, and release date. 
Moreover, according to the US Department of Energy (2023), the Fuel Economy (FE) and CO2 measures have been defined in the following three ways: 

The subsequent analysis sections will explain the data cleaning techniques used with the software IBM SPPS statistics.

# 2. Research Questions (Hypothesis)

![img.png](Images%2Fimg.png)

# 3. Data Cleaning

## 3.1. Missing Values / Errors
With the help of the option “Frequencies” within the software. The analysis showed zero missing or error values through the 9 numerical variables. 

![img_1.png](Images%2Fimg_1.png)
 
## 3.2. Duplicates Values
Continuing the data cleaning techniques, the “Identify Duplicate Cases” option demonstrated 7 following duplicate cases. Therefore, these cases have been removed from the dataset due, leading to a reduction in the total number of from 728 to 721 cases. 

![img_2.png](Images%2Fimg_2.png)
 
## 3.3. Outliers

![img_3.png](Images%2Fimg_3.png)

The above figure defines 3 outlier’s cases in the Combined Fuel Economy variable. As suggested technique for this scenario, the values were replaced with the respective group’s average fuel economy for each instance. To illustrate, the Fusion Hybrid FWD cars belongs to the Fusion Hybrid carline group. Then, the previous combined FE value of 42 was replaced by 29 (Fusion Hybrid FE average). In addition, it was applied the same technique process to the other 2 instances. After this process, the next figure shows the new boxplot.
 
![img_4.png](Images%2Fimg_4.png)

In summary, after using the cleaning techniques described previously such as missing values, replacing errors, removing duplicates, and substituting outliers. The dataset is prepared to do the appropriate analysis in the following sections.

# 4. Data Analytical Method (Using SPSS software)
The upcoming analytics method beings by conducting a descriptive analysis of the two variables linked to the hypothesis: CO2 and FE. The next are the steps followed by the method.

- Pearson Linear Correlation Coefficient test to define the relationship between City, Highway and Combined variable. The purpose was defined the Combined CO2 and FE as the central variable of the whole analysis. 
- Descriptive Statistics Analysis for both qualitative and quantitative variables.
- Test of normality to know whether the CO2 and FE follow a normal distribution. 
- Pearson Linear Correlation Coefficient test to determine the correlation between the quantitative measures and combined measures.
- Chi-Square to understand the correlation between qualitative and the combined measures.
- Graphical analysis to complement the statistical analysis and understand the car characteristics that drive lowest or highest FE/CO2.
- Accept or Reject Hypothesis and answer the initial research questions.

## 4.1 Pearson Linear Correlation Coefficient
The succeeding table shows the Output of the Pearson Correlation Pearson between Combined Fuel Economy, Citi Fuel Economy, and Highway Fuel Economy.

![img_5.png](Images%2Fimg_5.png)
 
In conclusion, it was demonstrated that City and Highway metrics have a strong linear relationship with the combined Variables. For that reason, from onward will be used the Combined metrics to answer the Research questions to simplify the analysis.

## 4.2 Descriptive Statistics Analysis
	
These statistics will guide an overall understanding of the dataset throughout measure of central tendency and dispersion, or graphical representations, such as histograms, boxplots, scatter plots, used to display the data an discover trends (Stapor, 2020). The following descriptive statistics was performed by using the SPSS software.
 
![img_6.png](Images%2Fimg_6.png)

Given the above, the standard deviation is relatively close to the means of both variables Combined FE and CO2, which results in fewer outliers. This can be cross-checked with the Outliers analysis performed in the previous cleaning section.

Next, the Kurtosis measure output are classified as Platykurtic for both Combined FE (-0.1) and Combined CO2 (1.53). This means, the distribution has short tails and few outliers. On the other hand, the Combined FE Skewness coefficient is nearly symmetrical (0.324) leading the left and right tails contains approximately the same number of observations. However, the Combined CO2 is positively skewed (0.995), that means the data is greater than the median and large numbers are in the right tail.

![img_7.png](Images%2Fimg_7.png)
 
## 4.2 Test of normality

Now, to know what kind of tests are suitable for the dataset, here are the outputs to run a Test of normality in SPSS.

![img_8.png](Images%2Fimg_8.png)

The results were conducted in two types of tests, Kolmogorov-Smirnov, and Shapiro-Wilk. Since the dataset contains 721 observations, both tests are suggested to assess normality. We can see from the above in both cases that the data differs significantly from a normal distribution as the Sig. value of both test es less than 0.05. In simpler terms, we have significance evidence to reject the Null-Hypothesis suggesting that the data for both variables follow a normal distribution.

![img_9.png](Images%2Fimg_9.png)
 
To conclude, for both variables Combined FE and CO2, these small deviations from a perfect normal distribution would not prevent us from using parametric or non-parametric statistical methods.

## 4.3 Pearson Linear Correlation Coefficient

![img_10.png](Images%2Fimg_10.png)

The above results demonstrated that the Correlation is statistically significant (p<0.01) between both Combined variables with the other three independent variables (Engine Displacement, No Cylinders, No Gears). Furthermore, this relation can be explained as following:

-	Strong negative correlation between Combined FE with Engine Displacement, No of Cylinders, and Combined FE.
-	Weak negative correlation between Combined FE and No Gears.
-	Strong positive correlation between Combined CO2 and Engine Displacement and No of Cylinders.
-	Weak positive correlation between Combined FE and No Gears

## 4.4 Chi-Square Test

After performing the previous test with the quantitative variable. This process will continue evaluating the qualitative variables with e Chi-Square Test. The variables of the dataset are Division, Carline, Transmission, Air Aspiration Method, Drive Desc, and Carline Class. The next table is the output of the test for the variable Combined FE and division.
 
![img_11.png](Images%2Fimg_11.png)

From the previous example, we had significant evidence to reject the null hypothesis, and demonstrate the correlation between Combined FE and Division variables. The previous statement was concluded since the p-value is less than 0.001. Additionally, we used the same process with the other qualitative variables, and we conclude the Combined FE and CO2 have an association with Division, Carline, Transmission, Air Aspiration Method, Drive Desc, and Carline Class variables. 

## 4.3 Graphical Analysis of Variables Associated

From the results of the Pearson Linear Coefficient and Chi-Square Tests, we discovered the quantitative and qualitative variables with a strong correlation with the FE and CO2 variables. To complement the analysis, we will perform a graphical analysis of those variables.

![img_12.png](Images%2Fimg_12.png)

Looking at the above figure, the Luxuries brand such as Bugatti, Lamborghini and Aston Martin are the lowest fuel economy type of car (Liters/100km). In other words, the cars that consume less litters for each 100 kilometres.

![img_13.png](Images%2Fimg_13.png)

Contrary, from the above figure we can define from the CO2 mean of the dataset that the non-luxury brands are the most environmentally friendly such as Fiat, Mini, and Mazda. Tu put it in another way, the cars that emit fewer amount of CO2 by Kilometre.

In conclusion, after cleaning the dataset, choosing the correct variable, assessing by descriptive statistics analysis, evaluating the data with normal distribution, and performing correlation analysis for both quantitative and qualitative variables. We can reject both Null hypotheses formulated at the beginning of this section and accept the Alternative Hypothesis.

## 4.3 Graphical Analysis of Variables Associated

![img_14.png](Images%2Fimg_14.png)

From the above conclusion, we can say there is a correlation between Fuel Economy and CO2 emissions, with the following car characteristics: Division, Engine Displacement, No. Cylinders, Transmission, No Gears, Drive Desc, and Carline Class. Finally, we can answer the research questions formulated in the context.
What type of car provides the most fuel economy? The type of car that proves the lowest Combined FE (L/100k) can be defined with the following characteristics:

-	Luxury Brands (Bugatti, Lamborghini, Aston Martin)
-	High Engine Displacement (6 to 8)
-	Highest Number of Cylinders (12, 16)
-	Automatic Transmission
-	Supercharged Air Aspiration Method
-	Part -Time 4 Wheel drive
-	Van

What type of car is environmentally friendly?  The type of cars with the lowest CO2 emission (g/km) is:
-	Non-Luxury Brands (FIAT, Mazda, Mini)
-	Low Engine displacement (1 to 2)
-	Low Number of cylinders (3, 4)
-	Manual Transmission
-	Naturally Air Aspiration Method
-	2-Wheel drive

In addition, as the Combined CO2 and Combined FE2 have a negative strong correlation, generally the type of car that has highest Fuel Economy is the less environmentally friendly.