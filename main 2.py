import pandas as pd
import matplotlib.pyplot as plt

# Читання CSV файлу з використанням велодоріжок
df = pd.read_csv('bike_data.csv')  # Замініть 'bike_data.csv' на шлях до вашого файлу

# Виведення перших кількох рядків для аналізу
print("Перші 5 рядків даних:")
print(df.head())

# Перетворення стовпця 'Date' у формат дати
df['Date'] = pd.to_datetime(df['Date'])

# Додавання стовпців для року, місяця, дня тижня
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day_of_Week'] = df['Date'].dt.day_name()

# === Агрегація та групування ===

# Групування за місяцями та підрахунок середньої кількості велосипедистів за місяць
avg_bike_by_month = df.groupby('Month')['Compte'].mean()

print("\nСередня кількість велосипедистів за кожен місяць:")
print(avg_bike_by_month)

# Візуалізація середньої кількості велосипедистів за місяць
avg_bike_by_month.plot(kind='bar', color='skyblue')
plt.title('Середня кількість велосипедистів за місяць')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

# Групування за днями тижня та підрахунок середньої кількості велосипедистів
avg_bike_by_day = df.groupby('Day_of_Week')['Compte'].mean()

print("\nСередня кількість велосипедистів за день тижня:")
print(avg_bike_by_day)

# Візуалізація середньої кількості велосипедистів за день тижня
avg_bike_by_day.plot(kind='bar', color='green')
plt.title('Середня кількість велосипедистів за день тижня')
plt.xlabel('День тижня')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
