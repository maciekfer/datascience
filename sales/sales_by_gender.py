import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytaj dane
df = pd.read_csv('salesforcourse-4fe2kehu.csv')

# Obliczanie przychodu
df['Revenue'] = df['Quantity'] * df['Unit Price']

# Segmentacja klientów
customer_segments = df.groupby(['Customer Gender', 'Customer Age']).agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()

# Wykres segmentacji klientów
plt.figure(figsize=(12, 6))
sns.barplot(data=customer_segments, x='Customer Age', y='Revenue', hue='Customer Gender')
plt.title('Przychody według segmentów klientów')
plt.xlabel('Wiek klienta')
plt.ylabel('Przychód')
plt.legend(title='Płeć')
plt.xticks(rotation=45)
plt.show()
