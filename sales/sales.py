from google.colab import files
import pandas as pd

# Załaduj plik CSV
uploaded = files.upload()

# Zakładam, że nazwa pliku to 'dane.csv'
df = pd.read_csv('salesforcourse-4fe2kehu.csv')

# Wyświetl pierwsze 10 wierszy
print(df.head(10))

import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane
df = pd.read_csv('salesforcourse-4fe2kehu.csv')

# 1. Analiza sprzedaży w czasie
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Sprzedaż miesięczna')
plt.xlabel('Miesiąc')
plt.ylabel('Przychód')
plt.xticks(rotation=0)
plt.show()

# 2. Analiza produktów
top_products = df.groupby('Product Category')['Revenue'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='orange')
plt.title('Najlepiej sprzedające się kategorie produktów')
plt.xlabel('Kategoria Produktu')
plt.ylabel('Przychód')
plt.xticks(rotation=45)
plt.show()

# 3. Analiza finansowa
total_cost = df['Cost'].sum()
total_revenue = df['Revenue'].sum()

plt.figure(figsize=(10, 6))
plt.bar(['Całkowity koszt', 'Całkowity przychód'], [total_cost, total_revenue], color=['red', 'green'])
plt.title('Porównanie kosztów i przychodów')
plt.ylabel('Kwota')
plt.show()

# Wyświetl podsumowanie
print(f'Całkowity koszt: {total_cost}')
print(f'Całkowity przychód: {total_revenue}')
print(f'Zysk: {total_revenue - total_cost}')
