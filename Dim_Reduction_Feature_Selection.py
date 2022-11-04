# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:19:16 2022

@author: T006940
"""


import numpy as np
import pandas as pd

from sklearn.feature_selection import VarianceThreshold


df = pd.read_excel (r'SEGBMODUL.xlsx',sheet_name = 'kar')

df.describe()


####-----varyans threshold ile veriyi azaltma------------------#######
qconstant_filter = VarianceThreshold(threshold=0.10)
qconstant_filter.fit(df_drop)
len(df_drop.columns[qconstant_filter.get_support()])
qconstant_columns = [column for column in df_drop.columns
                    if column not in df_drop.columns[qconstant_filter.get_support()]]

print(len(qconstant_columns))

for column in qconstant_columns:
    print(column)

qconstant_columns_to_remove = [i.strip() for i in qconstant_columns]

df_drop = df_drop.drop(qconstant_columns_to_remove, axis=1)
df_drop.shape



####-----#eksik verileri görüp datadan çıkarabiliriz--------#####
df_drop.isna().sum()

###----korelasyonu yüksek verileri görüp çıkarabiliriz---####
import seaborn as sns
print(df_drop.corr())
sns.heatmap(df_drop.corr(),)

#####-----0 değeri olan verileri görüp çıkarabiliriz----######

for column_name in df_drop.columns:
    column = df_drop[column_name]
    # Get the count of Zeros in column 
    count = (column == 0).sum()
    print('Count of zeros in column ', column_name, ' is : ', count)