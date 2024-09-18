import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from google.colab import files
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytaj plik z pulpitu
uploaded = files.upload()

# Zakładam, że plik nazywa się 'economic_indicators_dataset_2010_2023.csv'
df = pd.read_csv('economic_indicators_dataset_2010_2023.csv')

# Wyświetlenie pierwszych kilku wierszy danych
print(df.head())

# Zakładam, że kolumna 'GDP Growth Rate (%)' jest interesującą cechą, którą chcemy sklasyfikować
# i będziemy tworzyć etykiety na podstawie tej kolumny

# Przykład: tworzenie etykiety w oparciu o przedziały wzrostu GDP
df['Label'] = pd.cut(df['GDP Growth Rate (%)'], bins=5, labels=False)

# Wybór cech i etykiety
X = df[['Inflation Rate (%)', 'GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Interest Rate (%)']]
y = df['Label']

# Normalizacja cech
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Tworzenie i trenowanie modelu
model = GaussianNB()
model.fit(X_train, y_train)

# Dokonywanie predykcji
y_pred = model.predict(X_test)

# Ocena modelu
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Wizualizacja - Macierz konfuzji
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=[f'Class {i}' for i in range(len(conf_matrix))],
            yticklabels=[f'Class {i}' for i in range(len(conf_matrix))])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# Wizualizacja - Wykres rozrzutu cech
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis')
plt.title('Inflation Rate (%) vs GDP Growth Rate (%)')
plt.xlabel('Inflation Rate (%)')
plt.ylabel('GDP Growth Rate (%)')

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 2], X_test[:, 3], c=y_test, cmap='viridis')
plt.title('Unemployment Rate (%) vs Interest Rate (%)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Interest Rate (%)')

plt.tight_layout()
plt.show()
