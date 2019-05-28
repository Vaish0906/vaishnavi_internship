import pandas as pd

# -------question1--------------------

df = pd.read_csv("Laliga.csv")
#df = pd.read_csv("Laliga.csv", na_values = ['-'])
df.replace(to_replace = '-',value = 0)
print(df['Third'][12])
print(df['Third'][3]+df['Third'][12])

#-------------------- question2--------------------------

for i in df['Debut'] and j in df['Since/Last']:
  if i >=1930 and j <=1980:
    print(df['Team'])  


#---------question 3 ---------------------

df.loc[df['Points'].idxmax()]
#df.loc[df['Value'].idxmax()]

#---------question 4 ----------------

def Goal_diff_count():
  df['Goal_Differences'] = df['GoalsFor'] - df['GoalsAgainst']
  return df['Teams','Goal_Differences']

if 

#----------question 5--------------------


df.loc[df['WinningPercentage'].idxmax()]
