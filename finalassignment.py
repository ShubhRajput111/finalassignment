import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# Read the CSV file
df = pd.read_csv('data/bike_sales.csv')

plt.figure(figsize=(12, 6))
age_profit = df.groupby('Age_Group')['Profit'].mean().sort_values(ascending=False)
age_profit.plot(kind='bar')
plt.title('Average Profit by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Gender Distribution of Orders
plt.figure(figsize=(8, 6))
df['Customer_Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Customer Gender Distribution')
plt.show()

# 3. Year-wise Revenue Trend
plt.figure(figsize=(12, 6))
yearly_revenue = df.groupby('Year')['Revenue'].sum()
yearly_revenue.plot(kind='line', marker='o')
plt.title('Yearly Revenue Trend')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()

# 4. Country-wise Orders Heatmap
plt.figure(figsize=(12, 8))
country_orders = df.pivot_table(
    values='Order_Quantity',
    index='Country',
    columns='Year',
    aggfunc='sum'
).fillna(0)
sns.heatmap(country_orders, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Country-wise Orders by Year')
plt.tight_layout()
plt.show()

# 5. Material-wise Profit Analysis
plt.figure(figsize=(10, 6))
material_profit = df.groupby('Material')['Profit'].mean().sort_values(ascending=False)
material_profit.plot(kind='bar')
plt.title('Average Profit by Material')
plt.xlabel('Material')
plt.ylabel('Average Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Rating Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Rating', bins=20)
plt.title('Distribution of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# 7. Eco-Friendly vs Non-Eco-Friendly Comparison
plt.figure(figsize=(10, 6))
eco_comparison = df.groupby('Eco_Friendly').agg({
        'Profit': 'mean',
        'Revenue': 'mean',
        'Rating': 'mean'
    })
eco_comparison.plot(kind='bar')
plt.title('Eco-Friendly vs Non-Eco-Friendly Products Comparison')
plt.xlabel('Eco-Friendly')
plt.ylabel('Average Values')
plt.legend(title='Metrics')
plt.tight_layout()
plt.show()

# Generate summary statistics
summary_stats = {
    'total_revenue': df['Revenue'].sum(),
    'total_profit': df['Profit'].sum(),
    'total_orders': df['Order_Quantity'].sum(),
    'avg_rating': df['Rating'].mean(),
    'top_country': df.groupby('Country')['Order_Quantity'].sum().idxmax(),
    'most_profitable_age_group': age_profit.index[0],
    'eco_friendly_percentage': (df['Eco_Friendly'] == True).mean() * 100
}
print(summary_stats)

