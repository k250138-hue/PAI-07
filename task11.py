from dataset import clean_data

df = clean_data()

print("Insight 1: revenue and average spend by city")
print(df.groupby('City')['Total_Spent'].agg(['count', 'sum', 'mean']).round(2))

print("\nInsight 2: revenue by category")
print(df.groupby('Category')['Total_Spent'].sum().round(2))

print("\nInsight 3: VIP vs non-VIP")
print(df.groupby('Is_VIP')[['Total_Spent', 'Order_Count']].mean().round(2))
print("VIP customers:", df['Is_VIP'].sum(), "out of", len(df))

print("\nWritten insights:")
print("- Lahore earns the most revenue (about Rs. 1.06M) because it has the most customers (41),")
print("  while Karachi has the highest average spend per customer (Rs. 27,379).")
print("- Books (about Rs. 1.00M) and Electronics (about Rs. 997K) lead revenue; Home is lowest (about Rs. 614K).")
print("- VIPs spend and order about the same as non-VIPs (Rs. 24,798 vs Rs. 24,839; 16.11 vs 16.04 orders),")
print("  so VIP status is not separating high spenders in this data.")
