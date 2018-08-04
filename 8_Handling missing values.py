import pandas as pd

df = pd.read_csv('http://bit.ly/uforeports')


#isnull METHOD RETURNS BOOLEAN FALSE IF THERE EXISTS A VALUE AND A BOOLEAN TRUE IF THERE IS A 'NaN'
df.isnull().tail()


#notnull IS THE EXACT OPPOSITE OF isnull METHOD. IT RETURNS A TRUE IF THERE EXISTS A VALUE AND FALSE IF THERE IS A 'NaN'
df.notnull().tail()


#sum COMBINED WITH isnull METHOD RETURNS A COLUMNWISE SUMMATION OF ALL THE 'NaN's
df.isnull().sum()


#FILTERING THE ROWS WHICH HAS ITS CITY COLUMN VALUE VALUE AS A 'NaN' 
df[df.City.isnull()]


#DROPPING THE ROWS IF ANY OF ITS VALUES ARE MISSING
df.dropna(how = 'any')


#DROPPING THE ROWS IF ALL OF ITS VALUES ARE MISSING
df.dropna(how = 'all')


#DROPPING THE ROWS IF ANY OF ITS 'City/Shape Reported' VALUES ARE MISSING
df.dropna(subset = ['City', 'Shape Reported'], how = 'any')


#FILLING THE VALUES WHICH HAS A NaN
df.fillna(value = 'heregoesthevalueyouwanttofill')