from dataset import make_data

df = make_data()
print("Rows before:", len(df))

df = df.dropna(subset=['Customer_ID'])
df = df.reset_index(drop=True)

print("Rows after:", len(df))
print("Missing Customer_ID now:", df['Customer_ID'].isna().sum())
