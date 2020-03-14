# Part. 1
import csv
import pandas as pd

#=======================================
# Part. 2
# Read cwb weather data

cwb_filename = '106000122.csv'
data = []
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
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

dfObj = pd.DataFrame(target_data)
print(target_data)
display(dfOBj.head())

indexNames = dfObj[dfObj[WDSD]== -99.000].index
dfObj.drops(indexNames, inplace= True)
# print(dfObj)
display(dfOBj.head())

# Retrive ten data points from the beginning.
# target_data = data[:10]
#=======================================
# Part. 4
# Print result


#========================================