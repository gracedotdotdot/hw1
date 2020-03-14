#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Part. 1
import csv
import pandas as pd

#=======================================
# Part. 2
# Read cwb weather data

cwb_filename = '106000122.csv'
data = []
output = []
header = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)
#=======================================
# Part. 3
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.


idName = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
for mID in idName:
    df =pd.DataFrame(list(filter(lambda item: item['station_id'] == mID, data)))
    display(df.head())
    
    indexNames = df[df['WDSD']==-99.000].index
    df.drop(indexNames, inplace= True)
    indexNames = df[df['WDSD']==-999.000].index
    df.drop(indexNames, inplace= True)

    mMin = float(df['WDSD'].min())
    mMax = float(df['WDSD'].max())
    mRange = mMax - mMin
    output.append([mID,mRange])

print(output)


# In[ ]:





# In[ ]:




