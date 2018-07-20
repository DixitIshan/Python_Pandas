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


#PRINTING THE FIRST 5 ROWS FROM THE DATA
print(df.head())


#PRINTING THE LAST 5 ROWS FROM THE DATA
print(df.tail())


#PRINTING THE SPECIFIC NUMBER OF HEADS AND TAILS:
print(df.head(2))
print(df.tail(2))


#GETTING THE NUMBER OF TOTAL ROWS AND COLUMNS IN THE DATASET
print(df.shape)


#SETTING THE INDEX OF THE DATAFRAME
df.set_index('Day', inplace = True)
print(df)


#DROPPING SPECIFIC COLUMNS. HERE AXIS = 1 STANDS FOR COLUMNS AND AXIS = 0 STANDS FOR ROWS
df.drop(['Day', 'Visitors'], axis = 1, inplace = True)



#KEEPING ONLY SPECIFIC COLUMNS AND DROPPING ALL THE REST

#ACCESSING SPECFIC COLUMNS IN 2 DIFFERENT WAYS
print(df.Bounce_Rate)
print('Bounce_Rate')


#RENAMING SPECIFIC COLUMNS
df.rename(columns = {'Day': 'day', 'Visitors': 'visitors'}, inplace = True)
print(df.columns)


#SORTING A SERIES
x = df.Visitors.sort_values()
print(x)


'''

OR another method to do the same would be like:

x = df['Visitors'].sort_values()
print(x)

'''


#SORTING A DATAFRAME BY THE SERIES
x = df.sort_values('Day')
print(x)


#SORTING ROWS BASED ON CONDITIONS
x = df[df.Day > 2]
print(x)


#SORTING THE ROWS BASED ON MULTIPLE FILTER
x = df[(Day > 2) and (Visitors > 29)]
print(x)

y = df[(Day > 2) or (Visitors > 29)]
print(y)

#PLOTTING GRAPHS WITH MATPLOTLIB
df.plot()
plt.show()
