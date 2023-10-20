from faker import Faker
import random
import csv


# Ініціалізація Faker
fake = Faker()

# Генерація даних
data = []
for _ in range(1000):
    movie = {
        "Назва фільму": fake.text(max_nb_chars=50),
        "Рік випуску": fake.random_int(min=1950, max=2023),
        "Рейтинг IMDB": round(random.uniform(1, 10), 1),
        "Рейтинг Metacritic": round(random.uniform(1, 100), 1),
        "Бюджет": round(random.uniform(1000000, 100000000), 2),
        "Касові збори": round(random.uniform(1000000, 500000000), 2),
    }
    data.append(movie)

# Визначення назви файлу CSV
csv_file = 'film.csv'

# Збереження даних у CSV файл
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ["Назва фільму", "Рік випуску", "Рейтинг IMDB", "Рейтинг Metacritic", "Бюджет", "Касові збори"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Запишіть заголовки у файл
    writer.writeheader()

    # Запишіть дані про фільми
    for movie in data:
        writer.writerow(movie)

print(f"Дані збережено у файлі: {csv_file}")