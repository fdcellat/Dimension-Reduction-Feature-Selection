# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:03:01 2022

@author: T006940
"""

import pandas as pd

import numpy as np
from sklearn.covariance import EllipticEnvelope

# df=pd.read_excel('SAG_SUMMARY_STATS.xlsx')
df7=pd.read_excel('SAG_BULK_DATA Strateji.xlsx')
df8 = df7.groupby("ILCE")["SA - ÖSS Ferdi"].sum()


df=pd.read_excel('sag_basic_stats.xlsx')


df2=df[(df['DIM_ADET'] == 4) & (df['IL'].notnull())]
#burayı istediğin sütuna göre değiştir
#df4=df4[df4['SA - ÖSS Ferdi'].notnull()]
df3=df2[df2['ILCE'].notnull()]
df3=df2[(df2['ILCE'].notnull())&(df2['CINSIYET'].notnull())]



df4=df3[['MUST_ADET','IL','ILCE']]

df4=df4[df4['IL']!='İSTANBUL']
# df4.index=df4['IL']
# df4.drop(columns='IL',inplace=True)


#Outlier histogram ile---------------------------------------------------
import plotly.express as px

fig = px.histogram(df4, x='ILCE',y='MUST_ADET',labels=df4.index)
fig.show()
fig.write_html('mustplot2.html')


import plotly.express as px


fig = px.histogram(df3, x="IL", y="MUST_ADET",  pattern_shape="CINSIYET")
fig.show()
fig.write_html('mustplot3.html')


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df3, x="IL", y="MUST_ADET", marginal_x="histogram", marginal_y="rug",color='CINSIYET')
fig.show()
fig.write_html('mustplot4.html')


#outlier boxplot ile----------------------------------------------------
import seaborn as sns
ax = sns.boxplot(data=df4, palette="Set2")

# import matplotlib.pyplot as plt

# plt.scatter(df4.IL, df4.MUST_ADET, alpha=0.5)
#IQR outlier------------------------------------------------------------------

# calculate Q1 and Q3
Q1 = df4.quantile(0.25)
Q3 = df4.quantile(0.75)

# calculate the IQR
IQR = Q3 - Q1

# filter the dataset with the IQR
IQR_outliers = df4[((df4 < (Q1 - 1.5 * IQR)) |(df4 > (Q3 + 1.5 * IQR))).any(axis=1)]
IQR_outliers

#Z score outlier detection---------------------------------------------------
from scipy import stats
import numpy as np

# Calculate the z-scores
z_scores = stats.zscore(df4['MUST_ADET'])
z_scores

# Convert to absolute values
abs_z_scores = np.abs(z_scores)

# Select data points with a z-scores above or below 3
filtered_entries = (abs_z_scores > 3)

# Filter the dataset
zscore_outlier = df4[filtered_entries]
