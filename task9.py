from dataset import clean_data

df = clean_data()

chosen = df[df['Category'].isin(['Electronics', 'Clothing'])]
top5 = chosen.sort_values('Total_Spent', ascending=False).head(5)

print(top5[['Customer_ID', 'City', 'Category', 'Total_Spent']])
