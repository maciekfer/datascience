# Najpierw instalujemy niezbędne biblioteki
import pandas as pd
from google.colab import files
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Załadowanie pliku
uploaded = files.upload()

# 2. Wczytanie pliku CSV do ramki danych
# Zakładam, że plik to CSV; w przeciwnym razie trzeba dostosować format wczytywania
file_name = list(uploaded.keys())[0]  # Pobiera nazwę pierwszego załadowanego pliku
data = pd.read_csv(file_name)

# 3. Wyświetlenie pierwszych kilku wierszy dla weryfikacji
print("Pierwsze 5 wierszy datasetu:")
print(data.head())

# 4. Liczenie metod HTTP
method_counter = Counter(data['method'])

# 5. Liczenie ścieżek
path_counter = Counter(data['path'])

# 6. Zliczanie znaków specjalnych (o ile są to liczby w odpowiednich kolumnach)
special_char_columns = ['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'percentages', 'semicolons']
special_char_stats = {col: data[col].sum() for col in special_char_columns}

# 7. Wyniki

# Metody HTTP
print("\nMetody HTTP:")
for method, count in method_counter.items():
    print(f"{method}: {count}")

# Ścieżki URL
print("\nŚcieżki URL:")
for path, count in path_counter.items():
    print(f"{path}: {count}")

# Statystyki znaków specjalnych
print("\nStatystyki znaków specjalnych:")
for char, count in special_char_stats.items():
    print(f"{char}: {count}")

# Wizualizacja metod HTTP
plt.figure(figsize=(10, 6))
sns.barplot(x=list(method_counter.keys()), y=list(method_counter.values()))
plt.title("Liczba wystąpień metod HTTP")
plt.xlabel("Metoda HTTP")
plt.ylabel("Liczba wystąpień")
plt.xticks(rotation=45)
plt.show()

# Wizualizacja ścieżek URL
top_paths = path_counter.most_common(10)  # Pobieramy 10 najczęściej występujących ścieżek
paths, counts = zip(*top_paths)  # Rozdzielamy ścieżki i ich liczniki

plt.figure(figsize=(12, 6))
sns.barplot(x=list(counts), y=list(paths))
plt.title("10 najczęściej występujących ścieżek URL")
plt.xlabel("Liczba wystąpień")
plt.ylabel("Ścieżka URL")
plt.show()
