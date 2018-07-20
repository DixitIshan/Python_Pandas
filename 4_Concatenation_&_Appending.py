import pandas as pd

# TAKE INTO CONSIDERATION ALL THE MAJOR DIFFERENCES IN ALL THE DATAFRAMES BELOW
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])


# CONCATENATION WORKS WITH LISTS ONLY
concat_1 = pd.concat([df1, df2])
print concat

concat_2 = pd.concat([df1, df2, df3])
print(concat_2)

# APPENDING TWO DIFFERENT DATAFRAMES TO MAKE A NEW DATAFRAME
df4 = df1.append(df2)
print(df4)

# THIS IS SIMILAR TO ADDING A NEW ROW AT THE BOTTOM OF THE WHOLE DATAFRAME(NOT VERY EFFICIENT WAY TO DO SO)
s = pd.Series([40, 90, 65], index = ['HPI', 'Int_rate', 'US_GDP_Thousands'])
df5 = df1.append(s, ignore_index = True)
print(df5)