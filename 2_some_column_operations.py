import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {
'Day':[1,2,3,4,5,6],
'Visitors':[43,34,65,56,29,76],
'Bounce_Rate':[65,67,78,65,45,52]
}


#TURNING THE DICTIONARY TO DATAFRAME:
df = pd.DataFrame(web_stats)

#DROPPING SPECIFIC COLUMNS. HERE AXIS = 1 STANDS FOR COLUMNS AND AXIS = 0 STANDS FOR ROWS
df.drop(['Day', 'Visitors'], axis = 1, inplace = True)


#ACCESSING SPECFIC COLUMNS IN 2 DIFFERENT WAYS
print(df.Bounce_Rate)
print('Bounce_Rate')


#RENAMING SPECIFIC COLUMNS
df.rename(columns = {'Day': 'day', 'Visitors': 'visitors'}, inplace = True)
print(df.columns)