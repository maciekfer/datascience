import matplotlib.pyplot as plt

# Przykładowe dane do porównania
countries = df['Country'].unique()
gdp_per_capita = df.groupby('Country')['GDP per Capita (in USD)'].mean()
life_expectancy = df.groupby('Country')['Life Expectancy (Years)'].mean()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Wykres GDP per Capita
ax[0].bar(countries, gdp_per_capita, color='skyblue')
ax[0].set_title('GDP per Capita (in USD)')
ax[0].set_xlabel('Country')
ax[0].set_ylabel('GDP per Capita (in USD)')

# Wykres Life Expectancy
ax[1].bar(countries, life_expectancy, color='lightgreen')
ax[1].set_title('Life Expectancy (Years)')
ax[1].set_xlabel('Country')
ax[1].set_ylabel('Life Expectancy (Years)')

plt.tight_layout()
plt.show()
