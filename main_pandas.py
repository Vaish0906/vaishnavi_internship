import pandas as pd

df = pd.read_csv("Laliga.csv")
#df = pd.read_csv("Laliga.csv", na_values = ['-'])
df.Third = df.Third.astype(int)

#df.replace(to_replace = '-', value = 0)
print(df['Third'].dtype)
print(df['Third'][12])
print(df['Third'][1]+df['Third'][12])

#--------------------question2--------------------------
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

df['Winning Percentage'] = df['GamesWon']/df['GamesPlayed']
df['Winning Percentage'].multiply(100)

df.loc[df['Winning Percentage'].idxmax()]

#-------------QUESTION 6------------------  

"""6.	Group teams based on their “Best position” and print the sum of their points for all positions (5 points)
Eg: Best Position                Points 
        1                              25000
        2                              7000    
  
"""
df = df.groupby('Best position')
#df.get_group(1)

for i in range[1:21]:
if df.['Best position'][i] = 1:
  result = df.get_group(i)
  print()

