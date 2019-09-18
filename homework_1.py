# Time Series
# Mini-project
# Author: Vlad Doster
# September 15th, 2019

#############################################################################
# To install dependencies for imports, run pip3 install -r requirements.txt #
#############################################################################

##### Setup (Not important)#####
# Imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels
from scipy import stats
import matplotlib.pyplot as plt  # Needed by pandas plot class
import scipy
import xlrd  # Pandas dependency for reading in excel files
import pandas as pd

# Make seaborn happy
sns.set_style("whitegrid")

# vim variable completion ftw
age = 'age'
weight = 'Weight'
pa = 'political_affiliation'
hs_gpa = 'high_sch_GPA'
col_gpa = 'college_GPA'
veg = 'vegetarian'

#################

# Load in dataset
data_set_path = 'datasets/hw1_data.xlsx'  # Make own variable if need to use later
df = pd.read_excel(data_set_path)

'''
Problem 1

Categorize the variables (measurements) of this data set according to the following levels (ordinal, nominal, ratio and interval).

ordinal variables: None in the dataset
nominal variables: gender, political_affiliation, vegetarian, abortion_legalize, Full Time Student, Mode of transportation
ratio variables: Weight
interval variables: age, high_school_GPA, college_GPA
'''

'''
Problem 2
Use an appropriate graph (Pie chart, box plot, bar graph, histogram) to graph Weight, Political affiliation, and Age.
Interpret the graph.
'''
plt.figure(1)
pa_df = df.groupby(pa).size()
pa_df.plot.pie(explode=(0.05, 0.05, 0.05), autopct='%.2f', startangle=45).set(ylabel='',
                                                                              title='Problem 2- {}'.format(pa))

plt.figure(2)
sns.distplot(df.get(age).values, kde=False, rug=True).set(xlabel=age, ylabel='Frequency',
                                                          title='Problem 2- {}'.format(age))

plt.figure(3)
sns.distplot(df.get(weight).values, kde=False, rug=True).set(xlabel=weight, ylabel='Frequency',
                                                             title='Problem 2- {}'.format(weight))
'''
Problem 3
Find the numerical summary (mean, median, mode, etc) of quantitative variables
'''
print(df.describe(include=[np.number]).to_string())


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return m, m - h, m + h


'''
Problem 4
Compute a 95% confidence interval for the Age variable and interpret your result.
'''
print("\n95% CI for {} ~ {}".format(age, mean_confidence_interval(df.get(age).values)))

'''
Problem 5
Compute the 99\% confidence interval for the college GPA.
'''
print("\n99% CI for {} ~ {}".format(col_gpa, mean_confidence_interval(df.get(col_gpa).values, confidence=0.99)))

'''
Problem 6
Compute the 99\% confidence interval for the college GPA.
'''
plt.figure(4)
sns.scatterplot(data=df[[hs_gpa, col_gpa]]).set_title('Problem 6 - HS GPA & College GPA')
# Interpretation:

'''
Problem 7
Draw a scatter plot for weight and age
'''
plt.figure(5)
sns.scatterplot(data=df[[weight, age]]).set_title('Problem 7')

'''
Problem 8
Investigate relation between HS and college GPA
'''
plt.figure(6)
sns.regplot(x=col_gpa, y=hs_gpa, data=df[[col_gpa, hs_gpa]], x_ci=0.99).set_title('Problem 8')

# Interpretation:
# We can conclude that HS gpa pretty much predicts the college GPA. The coefficent given is 1.028 which means if
# HS gpa goes up by 1, then the college gpa will go up by 1.028 which is almost negligible.

'''
Problem 9
The linear regression fit is defined as $y=\beta_0+\beta_1 x+\epsilon$, where $y$ is the dependent variable, $X$  
is independent variable, and $\epsilon$ is a zero mean white noise.

We want to investigate if there is a linear relation between High School GPA and College GPA.
'''
import statsmodels.api as sm

X = df[[hs_gpa]]
y = df[[col_gpa]]

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print('\n{}'.format(model.summary()))

# From the summary, the relationship seems to be you do as well in college as you do in HS with a small amount doing
# better.

'''
Problem 10
Investigate how accurate is your model by plotting the residuals and qq plot of the error. Comment on your finding. 
'''

# residual plot
plt.figure(8)
statsmodels.api.qqplot(model.resid, fit=True)

# Plot related
plt.show()  # Show plots after all problems solved

# Debug stmts
# print(list(df.columns))
# print(df.head().to_string())
