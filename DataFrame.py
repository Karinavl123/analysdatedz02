import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

csv_file = 'film.csv'
df = pd.read_csv(csv_file, encoding='cp1252')


plt.hist(df['Rate IMDB'], bins=20, color='blue', alpha=0.7)
plt.title('Розподіл рейтингу IMDB')
plt.xlabel('Рейтинг IMDB')
plt.ylabel('Кількість фільмів')
plt.grid(True)

plt.show()



plt.hist(df['Rate Metacritic'], bins=20, color='green', alpha=0.7)
plt.title('Розподіл рейтингу Metacritic')
plt.xlabel('Рейтинг Metacritic')
plt.ylabel('Кількість фільмів')
plt.grid(True)

plt.show()



# Розрахунок середнього значення для рейтингу IMDB

print("-----------------------------------------------")

average_imdb_rating = df['Rate IMDB'].mean()
print(f"Середній рейтинг IMDB: {average_imdb_rating}")

# Розрахунок стандартного відхилення для рейтингу IMDB
std_deviation_imdb = df['Rate IMDB'].std()
print(f"Стандартне відхилення рейтингу IMDB: {std_deviation_imdb}")

# Розрахунок середнього значення для рейтингу Metacritic
average_metacritic_rating = df['Rate Metacritic'].mean()
print(f"Середній рейтинг Metacritic: {average_metacritic_rating}")

# Розрахунок стандартного відхилення для рейтингу Metacritic
std_deviation_metacritic = df['Rate Metacritic'].std()
print(f"Стандартне відхилення рейтингу Metacritic: {std_deviation_metacritic}")

print("-----------------------------------------------")
# Знайдення фільму з найвищим рейтингом на IMDB
highest_imdb_rating_movie = df.loc[df['Rate IMDB'].idxmax()]
print("Фільм з найвищим рейтингом на IMDB:")
print(highest_imdb_rating_movie)

# Знайдення фільму з найнижчим рейтингом на IMDB
lowest_imdb_rating_movie = df.loc[df['Rate IMDB'].idxmin()]
print("\nФільм з найнижчим рейтингом на IMDB:")
print(lowest_imdb_rating_movie)

print("-----------------------------------------------")

# Знайдення фільму з найвищим рейтингом на Metacritic
highest_metacritic_rating_movie = df.loc[df['Rate Metacritic'].idxmax()]
print("\nФільм з найвищим рейтингом на Metacritic:")
print(highest_metacritic_rating_movie)

# Знайдення фільму з найнижчим рейтингом на Metacritic
lowest_metacritic_rating_movie = df.loc[df['Rate Metacritic'].idxmin()]
print("\nФільм з найнижчим рейтингом на Metacritic:")
print(lowest_metacritic_rating_movie)

print("-----------------------------------------------")



# Розмір вибірки
sample_size = len(df)  # Здійсніть обчислення на основі реального розміру вибірки

# Рівень надійності 95%
confidence_level_95 = 0.95

# Рівень надійності 99%
confidence_level_99 = 0.99

# Стандартне відхилення для рейтингу IMDB
std_deviation_imdb = df['Rate IMDB'].std()

# Стандартне відхилення для рейтингу Metacritic
std_deviation_metacritic = df['Rate Metacritic'].std()

# Знайдіть критичні значення t для 95% та 99% рівнів надійності
t_critical_95 = stats.t.ppf(1 - (1 - confidence_level_95) / 2, sample_size - 1)
t_critical_99 = stats.t.ppf(1 - (1 - confidence_level_99) / 2, sample_size - 1)

# Розрахунок інтервалів довіри для середнього рейтингу IMDB та Metacritic
confidence_interval_imdb_95 = (average_imdb_rating - (t_critical_95 * std_deviation_imdb / (sample_size ** 0.5)),
                              average_imdb_rating + (t_critical_95 * std_deviation_imdb / (sample_size ** 0.5)))

confidence_interval_imdb_99 = (average_imdb_rating - (t_critical_99 * std_deviation_imdb / (sample_size ** 0.5)),
                              average_imdb_rating + (t_critical_99 * std_deviation_imdb / (sample_size ** 0.5)))

confidence_interval_metacritic_95 = (average_metacritic_rating - (t_critical_95 * std_deviation_metacritic / (sample_size ** 0.5)),
                              average_metacritic_rating + (t_critical_95 * std_deviation_metacritic / (sample_size ** 0.5)))

confidence_interval_metacritic_99 = (average_metacritic_rating - (t_critical_99 * std_deviation_metacritic / (sample_size ** 0.5)),
                              average_metacritic_rating + (t_critical_99 * std_deviation_metacritic / (sample_size ** 0.5)))

# Виведення результатів
print(f"Інтервал довіри для середнього рейтингу IMDB на рівні надійності 95%: {confidence_interval_imdb_95}")
print(f"Інтервал довіри для середнього рейтингу IMDB на рівні надійності 99%: {confidence_interval_imdb_99}")

print(f"Інтервал довіри для середнього рейтингу Metacritic на рівні надійності 95%: {confidence_interval_metacritic_95}")
print(f"Інтервал довіри для середнього рейтингу Metacritic на рівні надійності 99%: {confidence_interval_metacritic_99}")

print("-----------------------------------------------")

# Ваші дані про рейтинги IMDB та Metacritic
ratings_imdb = df['Rate IMDB']
ratings_metacritic = df['Rate Metacritic']

# Виконайте t-тест для залежних вибірок
t_stat, p_value = stats.ttest_rel(ratings_imdb, ratings_metacritic)

# Виведіть результат тесту
print(f"t-статистика: {t_stat}")
print(f"p-значення: {p_value}")

# Перевірка на статистичну значущість (наприклад, при рівні значущості 0.05)
alpha = 0.05
if p_value < alpha:
    print("Є статистично значуща різниця між рейтингами IMDB та Metacritic.")
else:
    print("Різниця між рейтингами IMDB та Metacritic не є статистично значущою.")

# Графік розподілу бюджету
plt.figure(figsize=(10, 6))
plt.hist(df['Budget'], bins=200, color='blue', alpha=0.7)
plt.xlabel('Бюджет (в доларах)')
plt.ylabel('Кількість фільмів')
plt.title('Розподіл бюджету фільмів')
plt.grid(True)
plt.show()

# Графік розподілу касових зборів
plt.figure(figsize=(10, 6))
plt.hist(df["Cashier's fees"], bins=200, color='green', alpha=0.7)
plt.xlabel('Касові збори (в доларах)')
plt.ylabel('Кількість фільмів')
plt.title('Розподіл касових зборів фільмів')
plt.grid(True)
plt.show()

print("-----------------------------------------------")

# Обчислення основних статистичних показників для бюджету
budget_mean = df['Budget'].mean()
budget_std = df['Budget'].std()
budget_min = df['Budget'].min()
budget_max = df['Budget'].max()

# Обчислення основних статистичних показників для касових зборів
revenue_mean = df["Cashier's fees"].mean()
revenue_std = df["Cashier's fees"].std()
revenue_min = df["Cashier's fees"].min()
revenue_max = df["Cashier's fees"].max()

# Виведення результатів
print("Статистика для бюджету фільмів:")
print(f"Середнє значення: {budget_mean}")
print(f"Стандартне відхилення: {budget_std}")
print(f"Мінімальне значення: {budget_min}")
print(f"Максимальне значення: {budget_max}")

print("\nСтатистика для касових зборів фільмів:")
print(f"Середнє значення: {revenue_mean}")
print(f"Стандартне відхилення: {revenue_std}")
print(f"Мінімальне значення: {revenue_min}")
print(f"Максимальне значення: {revenue_max}")
