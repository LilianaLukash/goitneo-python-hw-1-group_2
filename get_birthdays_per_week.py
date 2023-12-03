from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримання поточної дати
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця між днем народження та поточним днем
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            birthday_weekday = birthday_this_year.strftime("%A")
            # Якщо день народження випадає на вихідні, переносимо на понеділок
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"
            birthdays[birthday_weekday].append(name)

    # Виведення результату
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 12, 2)}
]


print(get_birthdays_per_week(users))