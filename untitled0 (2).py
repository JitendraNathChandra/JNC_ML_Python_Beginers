# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DuZQOCAlbuTVIBra8e5d3FDeaa81MUdd

# Oasis Infobyte Internship 2023
# Task no: 2

#**UNEMPLOYMENT ANALYSIS WITH PYTHON**

## *Name: Jitendra Nath Chandra*
Registration No: OIB/L2/IP11376
"""

#Importing Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

#Importing  plotly

import plotly.graph_objects as go
import plotly.figure_factory as ff
from IPython.display import HTML
import plotly.io as pio
pio.templates

#location of the csv file
loc = "/content/Unemployment in India.csv"

#Load Data and csv means comma separated values, pd converts text to csv ( separated with comma)
data = pd.read_csv( "Unemployment in India.csv")

#head() means 1st 5 rows of the data
data.head()

#if you provide n numbers rows of data then head() <-- 'n' put it
data.head(20)

#Shape --> total number of Rows and Columns

print(data.shape)

#Renameing the column names to remove unwanted spaces
data.columns

# To Change the columns name
#data.columns = ['Region','Data','da','jdssd','fsdff','tsdfs','fsd']

#data.head()

# Describe method: Statistic of our Data ( like- Count, Mean, Std, Min, Max)
data.describe()

X = data[' Estimated Unemployment Rate (%)'].values
#y = data['Estimated Unemployment Rate according to area'].values (column name does not exist check it)

##some more information about the dataframe
data.info

data.isnull

##Given Dataframe contain some null values , we have to remove then from df
data.isna().sum()

data = data.dropna()

data['year'] = pd.DatetimeIndex(data[' Date']).year
data['month'] = pd.DatetimeIndex(data[' Date']).month

data

#Type
df = data.astype({' Estimated Unemployment Rate (%)':'float',' Estimated Employed':'float', ' Estimated Labour Participation Rate (%)':'float'})

#Estimated Unemployment Rate per region
region_unemployment = data.groupby('Region')[' Estimated Unemployment Rate (%)'].mean()
region_unemployment.plot(kind='bar', title='Unemployment Rate per regionEstimated ')

#Estimated Unemployment Rate according to area
Area_unemployment = data.groupby('Area')[' Estimated Unemployment Rate (%)'].mean()
Area_unemployment.plot(kind='bar', title='Estimated Unemployment Rate according to area')

year_unemployment = data.groupby('year')[' Estimated Unemployment Rate (%)'].mean()
year_unemployment.plot(kind='bar',title='Estimated Unemployment Rate per year')

df_2020 = data[data['year'] == 2020]
df_2019 = data[data['year'] == 2019]

#Estimated Unemployment rate per month of year 2020
month_unemployment = df_2020.groupby(['year', 'month'])[' Estimated Unemployment Rate (%)'].mean()
month_unemployment.plot(kind='line' , title='Estimated Unemployment rate per month of year 2020')

month_unemployment = df_2019.groupby(['year', 'month'])[' Estimated Unemployment Rate (%)'].mean()
month_unemployment.plot(kind='line',title='Estimated Unemployment Rate of per month of year 2019')

df = px.data.tips()
fig = px.sunburst(data, path=["Area","Region","year"], values=" Estimated Unemployment Rate (%)",
                   title= 'Unemployment rate in every Area & Region of year 2019 & 2020 ', height=650)
fig.show()



