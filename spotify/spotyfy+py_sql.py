from google.colab import files
import pandas as pd

# Wczytaj plik
uploaded = files.upload()

# Lista plików - gdy przesłałeś plik np. 'dane.csv'
for filename in uploaded.keys():
    print(f'Wczytano plik: {filename}')

# Zaczytanie pliku CSV do dataframe (zakładamy, że plik to .csv)
df = pd.read_csv(filename)

# Wyświetl pierwsze 5 wierszy pliku
df.head()

import sqlite3
import pandas as pd

# Tworzymy połączenie z bazą danych SQLite
conn = sqlite3.connect(':memory:')  # Bazę danych tworzymy w pamięci (RAM

# Załóżmy, że w pliku `dane.csv` mamy dane już wczytane jako dataframe `df`

# Teraz wczytamy te dane do tabeli SQL
df.to_sql('moje_dane', conn, index=False, if_exists='replace')  # Tworzymy tabelę o nazwie 'moje_dane'

# Sprawdzamy, czy dane zostały poprawnie wczytane
df_sql = pd.read_sql('SELECT * FROM moje_dane', conn)
df_sql.head()

query = 'SELECT * FROM moje_dane'
df_sql_all = pd.read_sql(query, conn)
df_sql_all.head()

query = 'SELECT * FROM moje_dane WHERE released_month >= 5 ORDER BY released_month'
df_sql_filtered = pd.read_sql(query, conn)
df_sql_filtered.head(50)

# Grupowanie po released_month i liczenie liczby rekordów dla każdego miesiąca
grouped_data = df_sql_filtered.groupby('released_month').size().reset_index(name='count')
print(grouped_data)

import matplotlib.pyplot as plt
import seaborn as sns

# Tworzenie wykresu liczby wydanych rekordów w każdym miesiącu
plt.figure(figsize=(10, 6))
sns.countplot(data=df_sql_filtered, x='released_month')
plt.title('Liczba rekordów według miesiąca wydania')
plt.xlabel('Miesiąc wydania')
plt.ylabel('Liczba rekordów')
plt.show()

