import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Sprawdzenie dostępnych kolumn w DataFrame
print(df.columns)

# Analiza wpływu 'danceability_%' i 'energy_%' na 'popularity'
correlation_matrix = df[['danceability_%', 'energy_%', 'in_spotify_charts']].corr()
print(correlation_matrix)

# Wizualizacja: Danceability vs Popularność z kolorem według energii
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='danceability_%', y='in_spotify_charts', hue='energy_%', size='energy_%', sizes=(20, 200), alpha=0.5)
plt.title('Danceability vs Popularność (kolorowane według Energii)')
plt.xlabel('Danceability (%)')
plt.ylabel('Popularność w Spotify')
plt.legend(title='Energia (%)', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()
