from dataset import make_data

df = make_data()
df = df.dropna(subset=['Customer_ID']).reset_index(drop=True)   # Task 2
df['Total_Spent'] = df['Total_Spent'].fillna(df['Total_Spent'].mean())   # Task 3

df['Avg_Order_Value'] = df['Total_Spent'] / df['Order_Count']

print(df[['Customer_ID', 'Total_Spent', 'Order_Count', 'Avg_Order_Value']].head())
