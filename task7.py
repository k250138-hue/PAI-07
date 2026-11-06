from dataset import clean_data

df = clean_data()

city_summary = df.groupby('City').agg(
    Total_Customers=('Customer_ID', 'count'),
    Avg_Total_Spent=('Total_Spent', 'mean'),
    Max_Order_Count=('Order_Count', 'max')
).reset_index()

print(city_summary)
