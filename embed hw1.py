#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Part. 1
import csv
import pandas as pd

#=======================================
# Part. 2
# Read cwb weather data

cwb_filename = 'sample_input.csv'
data = []
output = []
header = []
indexName = []

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
    df =list(filter(lambda item: item['station_id'] == mID, data))
    #display(df.head())

    print(df)
    for item in df:
        print('\n')
        if item['WDSD']=='-99.000' or item['WDSD']== '-999.000':
            item['WDSD']= '0'
    for item in df:
        if df.index(item)==0:
            mintmp = item['WDSD']
            maxtmp = item['WDSD']
        elif item['WDSD']<mintmp:
            mintmp = item['WDSD']
        elif item['WDSD']>maxtmp:
            maxtmp = item['WDSD']
    
    mRange = float(maxtmp) - float(mintmp)
    output.append([mID, mRange])

    
#     for i in range(0, 13):
#         if(df[i][4]==-99.000):
#             indexName.append(i)
#             df[i][4]=0       
    
print(output)


# In[ ]:





# In[ ]:




