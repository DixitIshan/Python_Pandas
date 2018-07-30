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

#SORTING A SERIES
x = df.Visitors.sort_values()
print(x)


'''

OR another method to do the same would be:

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