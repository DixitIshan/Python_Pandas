import pandas as pd

import pandas as pd
df1 = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
df2 = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})

#MERGING OF 2 DATAFRAMES ON 'HPI' COLUMN
first_merge = pd.merge(df1, df2, on = 'id')
print(first_merge)


#MERGING ON 2 DIFFERENT COLUMNS
second_merge = pd.merge(df1, df2, on = ['id', 'subject_id'])
print(second_merge)

# MERGE USING 'HOW' ARGUMENT
"""
THERE ARE 4 TYPES OF MERGING METHOD USING 'HOW' ARGUMENT
1) LEFT OUTER
2) RIGHT OUTER
3) FULL OUTER
$) INNER
"""

left_merge = pd.merge(df1, df2, on = 'subject_id', how = 'left')
print(left_merge)

right_merge = pd.merge(df1, df2, on = 'subject_id', how = 'right')
print(right_merge)

outer_merge = pd.merge(df1, df2, on = 'subject_id', how = 'outer')
print(outer_merge)

inner_merge = pd.merge(df1, df2, on = 'subject_id', how = 'inner')
print(inner_merge)

# JOINING WILL BE PERFORMED ON INDEX. JOIN OPERATION HONORS THE OBJECT ON WHICH IT IS CALLED. SO, A.JOIN(B) IS NOT EQUAL TO B.JOIN(A).

df1.set_index('subject_id', inplace=True)
df3.set_index('subject_id', inplace=True)
right_joined = df1.join(df3, how="right")
print(right_joined)

right_joined = df1.join(df3, how="left")
print(left_joined)

right_joined = df1.join(df3, how="inner")
print(inner_joined)

right_joined = df1.join(df3, how="outer")
print(outer_joined)