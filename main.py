import pandas as pd

# Дані для DataFrame (можна взяти з лабораторної роботи та доповнити)
data = {
    'Ім\'я': ['Олександр', 'Марія', 'Олег', 'Олена', 'Вікторія'],
    'Вік': [25, 30, 22, 35, 28],
    'Місто': ['Київ', 'Львів', 'Одеса', 'Київ', 'Львів'],
    'Зарплата': [5000, 6000, 4500, 7000, 5200]
}

# Створення DataFrame
df = pd.DataFrame(data)

# Виведення DataFrame
print("Первинний DataFrame:")
print(df)

# === Операції агрегації ===
# Середня зарплата по містах
avg_salary_by_city = df.groupby('Місто')['Зарплата'].mean()
print("\nСередня зарплата по містах:")
print(avg_salary_by_city)

# Максимальний вік по містах
max_age_by_city = df.groupby('Місто')['Вік'].max()
print("\nМаксимальний вік по містах:")
print(max_age_by_city)

# === Операції групування ===
# Підрахунок кількості людей у кожному місті
people_count_by_city = df.groupby('Місто').size()
print("\nКількість людей у кожному місті:")
print(people_count_by_city)

# Групування за іменами та підрахунок загальної зарплати кожної людини
total_salary_by_name = df.groupby('Ім\'я')['Зарплата'].sum()
print("\nЗагальна зарплата кожної людини:")
print(total_salary_by_name)
