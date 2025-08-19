
import pandas as pd
df=pd.read_csv(r'ACM day2\goldenboot.csv')

print(df.head())


print(df.info())
print(df.describe())
top_scorers=df[df['Goals']>=40]
print(top_scorers)


mean=df['Goals'].mean()

print('Average goals scored:\n',mean)
maxgoal=df['Goals'].max()
print('Maximum goals scored:\n',maxgoal)

mingoal=df['Goals'].min()
print('Minimum goals scored:\n',mingoal)
club_counts=df['Club'].value_counts()
top_club=club_counts.idxmax()
print('Club with most winners:\n',top_club)


youngest=df[df['Age']==df['Age'].min()]
print('Youngest winner: \n',youngest['Player'])
oldest=df[df['Age']==df['Age'].max()]
print('Oldest winner:\n',oldest['Player'].values[0])
least_goals=df[df['Goals']==df['Goals'].min()]
print('Winner with least goals:\n',least_goals[['Player','Goals']].values[0])
most_goals=df[df['Goals']==df['Goals'].max()]
print('Winner with most goals:\n',most_goals[['Player','Goals']].values[0])

top_scorers=df[df['Goals']>=40]
print('Players with 40+ goals\n',top_scorers)