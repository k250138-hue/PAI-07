from dataset import make_data

df = make_data()
df = df.dropna(subset=['Customer_ID']).reset_index(drop=True)   # Task 2

median_age = df['Age'].median()
mean_spent = df['Total_Spent'].mean()
print("Median age:", median_age)
print("Mean spent:", round(mean_spent, 2))

df['Age'] = df['Age'].fillna(median_age)
df['Total_Spent'] = df['Total_Spent'].fillna(mean_spent)

print("\nMissing values after filling:")
print(df[['Age', 'Total_Spent']].isna().sum())
