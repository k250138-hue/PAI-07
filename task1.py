from dataset import make_data

df = make_data()

print("Shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values in each column:")
print(df.isna().sum())
