from dataset import make_data

df = make_data()
df = df.dropna(subset=['Customer_ID']).reset_index(drop=True)   # Task 2
df['Total_Spent'] = df['Total_Spent'].fillna(df['Total_Spent'].mean())   # Task 3
df['Avg_Order_Value'] = df['Total_Spent'] / df['Order_Count']   # Task 5

df['High_Value_Customer'] = df['Avg_Order_Value'] > 2500

print(df[['Customer_ID', 'Avg_Order_Value', 'High_Value_Customer']].head())
print("\nCounts:")
print(df['High_Value_Customer'].value_counts())
