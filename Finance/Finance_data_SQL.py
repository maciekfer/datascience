import pandas as pd
from google.colab import files

# Załaduj plik ręcznie
uploaded = files.upload()

# Wczytaj załadowany plik CSV do DataFrame
# files.upload() zwraca słownik, więc musisz użyć klucza, aby odczytać nazwę pliku
for file_name in uploaded.keys():
    df = pd.read_csv(file_name)


# Wyświetl pierwsze kilka wierszy
print(df.head())


import matplotlib.pyplot as plt

# Załóżmy, że kolumna nazywa się 'Gender'
# Policz ilość wystąpień mężczyzn i kobiet
gender_counts = df['gender'].value_counts()

# Stwórz wykres kołowy
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'pink'])
plt.title('Rozkład płci')
plt.show()

import matplotlib.pyplot as plt

# Rysowanie wykresu słupkowego
plt.bar(investment_counts.index, investment_counts.values)
plt.xticks(rotation=0)  # Utrzymujemy etykiety w poziomie
plt.xlabel('Inwestycje (Yes/No)')
plt.ylabel('Liczba')
plt.title('Rozkład odpowiedzi na inwestycje')
plt.show()


query1 = """
SELECT 
    Reason_Equity, COUNT(*) AS count 
FROM 
    finance_data 
GROUP BY 
    Reason_Equity 
ORDER BY 
    count DESC 
LIMIT 5;
"""
top_reasons = pd.read_sql_query(query1, conn)
print("Najczęstsze powody wyboru inwestycji:")
print(top_reasons)


query2 = """
SELECT 
    age, Investment_Avenues, COUNT(*) AS count 
FROM 
    finance_data 
GROUP BY 
    age, Investment_Avenues 
ORDER BY 
    age, count DESC;
"""
age_investment = pd.read_sql_query(query2, conn)
print("\nWiek inwestorów a rodzaj inwestycji:")
print(age_investment.head(10))  # Wyświetlenie tylko kilku wierszy


query3 = """
SELECT 
    Investment_Avenues,
    COUNT(*) AS count,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM finance_data)) AS percent
FROM 
    finance_data 
GROUP BY 
    Investment_Avenues;
"""
investment_share = pd.read_sql_query(query3, conn)
print("\nUdział inwestycji w różnych kategoriach:")
print(investment_share)


query4 = """
SELECT 
    AVG(age) AS average_age_using_mutual_funds 
FROM 
    finance_data 
WHERE 
    Mutual_Funds = 'Yes';
"""
average_age = pd.read_sql_query(query4, conn)
print("\nŚredni wiek inwestorów korzystających z funduszy inwestycyjnych:")
print(average_age)


query5 = """
SELECT 
    gender, Objective, COUNT(*) AS count 
FROM 
    finance_data 
GROUP BY 
    gender, Objective 
ORDER BY 
    gender, count DESC;
"""
popular_objectives = pd.read_sql_query(query5, conn)
print("\nNajpopularniejsze cele inwestycyjne według płci:")
print(popular_objectives.head(10))  # Wyświetlenie tylko kilku wierszy
