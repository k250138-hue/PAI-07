import pandas as pd
from dataset import make_data

df = make_data()
df = df.dropna(subset=['Customer_ID']).reset_index(drop=True)   # Task 2

df['Join_Date'] = pd.to_datetime(df['Join_Date'])
df['Join_Year'] = df['Join_Date'].dt.year
df['Join_Month'] = df['Join_Date'].dt.month_name()

print(df[['Join_Date', 'Join_Year', 'Join_Month']].head())
print("\nJoin_Date type:", df['Join_Date'].dtype)
