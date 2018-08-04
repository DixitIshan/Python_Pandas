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


#RESETTING THE INDEX BACK TO DEFAULT
df.index.name = 'Day'
df.reset_index(inplace = True)
print(df)