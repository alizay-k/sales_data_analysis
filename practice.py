import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("cleaned_dataset.csv")
print("Initial Data:")
print(df.head())
print(df.info())

# 2. Data Cleaning
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['quantity'] = df['quantity'].fillna(1)
df['revenue'] = df['revenue'].fillna(df['quantity'] * df['unit_price'])
df.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True, errors='ignore')
df.rename(columns={'id':'serial_no'}, inplace=True)

# 3. Feature Engineering
df['price_per_unit'] = df['revenue'] / df['quantity']
df['order_month'] = df['order_date'].dt.month
df['high_value_order'] = df['revenue'] > 1000

# 4. Analysis
revenue_region = df.groupby("region")['revenue'].sum()
print("\nRevenue per Region:\n", revenue_region)

revenue_category = df.groupby("category")['revenue'].sum()
print("\nRevenue per Category:\n", revenue_category)

top_products = df.groupby("product")['revenue'].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Products:\n", top_products)

average_value = df['revenue'].mean()
print("\nAverage Order Value:", average_value)

electronics = df[df['category']=='Electronics']
region_electronics = electronics.groupby('region')['revenue'].sum()
if not region_electronics.empty:
    top_region = region_electronics.idxmax()
    print("\nTop Region for Electronics:", top_region)
else:
    print("\nNo Electronics data found.")

# 5. Visualizations (Matplotlib)
plt.figure(figsize=(8,5))
plt.bar(revenue_region.index, revenue_region.values, color='skyblue')
plt.title("Total Revenue per Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(6,4))
plt.bar(revenue_category.index, revenue_category.values, color='lightgreen')
plt.title("Total Revenue per Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(6,4))
plt.bar(top_products.index, top_products.values, color='orange')
plt.title("Top 3 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

high_value_count = df[df['high_value_order']].groupby('order_month')['high_value_order'].count()
plt.figure(figsize=(8,5))
plt.bar(high_value_count.index, high_value_count.values, color='red')
plt.title("High Value Orders per Month")
plt.xlabel("Month")
plt.ylabel("Number of High Value Orders")
plt.show()

# 6. Save Cleaned Dataset
df.to_csv('cleaned_dataset.csv', index=False)
