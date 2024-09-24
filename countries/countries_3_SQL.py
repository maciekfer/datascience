import pandas as pd
from google.colab import files
import pandasql as ps

# Wczytanie danych
uploaded = files.upload()
df = pd.read_csv('country_comparison_large_dataset.csv')

# Sprawdzenie nazw kolumn
print("Nazwy kolumn w DataFrame:")
print(df.columns)

# Przykład użycia SQL do manipulacji danymi

# 1. Tworzenie widoku z uśrednionymi danymi
query_view = """
SELECT
    Country,
    AVG(`GDP (in Trillions USD)` / `Population (in Millions)`) AS Avg_GDP_Per_Capita,
    MAX(`Life Expectancy (Years)`) AS Max_Life_Expectancy,
    MIN(`Population (in Millions)`) AS Min_Population
FROM df
GROUP BY Country;
"""
df_summary = ps.sqldf(query_view, locals())

print("Widok z uśrednionymi danymi:")
print(df_summary.head())

# 2. Analiza danych z JOIN
query_join = """
SELECT
    A.Country,
    A.Year,
    A.`GDP (in Trillions USD)`,
    A.`Population (in Millions)`,
    B.Avg_GDP_Per_Capita
FROM df A
JOIN (SELECT
          Country,
          AVG(`GDP (in Trillions USD)` / `Population (in Millions)`) AS Avg_GDP_Per_Capita
      FROM df
      GROUP BY Country) B
ON A.Country = B.Country
WHERE A.`GDP (in Trillions USD)` / A.`Population (in Millions)` > B.Avg_GDP_Per_Capita;
"""
df_joined = ps.sqldf(query_join, locals())

print("\nDane po JOIN:")
print(df_joined.head())

# 3. Agregacja danych według roku
query_aggregation = """
SELECT
    Year,
    AVG(`GDP (in Trillions USD)` / `Population (in Millions)`) AS Avg_GDP_Per_Capita,
    SUM(`Population (in Millions)`) AS Total_Population
FROM df
GROUP BY Year
ORDER BY Year;
"""
df_aggregated = ps.sqldf(query_aggregation, locals())

print("\nDane agregowane według roku:")
print(df_aggregated.head())

# 4. Analiza okresowa (zmiana PKB)
query_periodic = """
SELECT
    Country,
    Year,
    `GDP (in Trillions USD)` - LAG(`GDP (in Trillions USD)`, 1) OVER (PARTITION BY Country ORDER BY Year) AS GDP_Change
FROM df;
"""
df_periodic = ps.sqldf(query_periodic, locals())

print("\nAnaliza okresowa (zmiana PKB):")
print(df_periodic.head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Używamy już załadowanego DataFrame df

# Sprawdzenie nazw kolumn
print("Nazwy kolumn w DataFrame:")
print(df.columns)

# 1. Wykres punktowy (scatter plot) GDP per Capita vs Life Expectancy
plt.figure(figsize=(12, 6))
sns.scatterplot(x='GDP per Capita (in USD)', y='Life Expectancy (Years)', data=df, hue='Country', palette='Set1', s=100, alpha=0.7)
plt.title('GDP per Capita vs Life Expectancy')
plt.xlabel('GDP per Capita (in USD)')
plt.ylabel('Life Expectancy (Years)')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(True)
plt.show()

# 2. Wykres słupkowy (bar plot) Urban Population % z podziałem na kraje
plt.figure(figsize=(14, 7))
sns.barplot(x='Country', y='Urban Population (%)', data=df, palette='viridis')
plt.title('Urban Population % by Country')
plt.xlabel('Country')
plt.ylabel('Urban Population (%)')
plt.xticks(rotation=45)  # Rotacja etykiet osi x dla lepszej czytelności
plt.grid(axis='y')
plt.show()
