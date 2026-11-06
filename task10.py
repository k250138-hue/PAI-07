from dataset import clean_data

df = clean_data()

vips = df[df['Is_VIP'] == True]
karachi_avg = vips[vips['City'] == 'Karachi']['Order_Count'].mean()
lahore_avg = vips[vips['City'] == 'Lahore']['Order_Count'].mean()

print("Karachi VIP average Order_Count:", round(karachi_avg, 2))
print("Lahore VIP average Order_Count:", round(lahore_avg, 2))

if karachi_avg > lahore_avg:
    print("Karachi VIPs place more orders on average.")
else:
    print("Lahore VIPs place more orders on average.")
