from datetime import datetime, timedelta
from collections import defaultdict

users = ({"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Nick Silver", "birthday": datetime(1980, 12, 31)},
         {"name": "Dmitriy Shpul", "birthday": datetime(1984, 1, 2)},
         {"name": "Olga Wwww", "birthday": datetime(1955, 1, 9)},
         {"name": "Aleks Skorin", "birthday": datetime(1977, 12, 26)})

def get_birthdays_per_week(users):
   
    #today = datetime(2021, 12, 26).date() # тестовая дата с переходом года на неделе
    today = datetime.today().date()
    
    # подготовка индексов по дням недели от текущего дня
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today_index = today.weekday()
    sorted_days = days_of_week[today_index:] + days_of_week[:today_index]
    next_week_birthdays = defaultdict(list)

    # поиск в списке всех именинников на ближайшие 7 дней, включая текущий день    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            next_week_birthdays[birthday_this_year.strftime("%A")].append(name)

    # сортировка дней рождений с учетом условий задачи (перенос с выходных на понедельник,
    # сортировка от сегодняшнего дня по дням недели)   
    sorted_birtdays = {}
    for day in sorted_days:
        if day in next_week_birthdays:  
            if day == "Saturday" or day == "Sunday":
                sorted_birtdays["Monday"] = next_week_birthdays[day]
            else:
                sorted_birtdays[day] = next_week_birthdays[day] 
    
    # Вывод результатов
    if len(sorted_birtdays) == 0:
        print("No one on your list has a birthday this week.")
    else:
        for day, name in sorted_birtdays.items():
            print(f"{day}: {', '.join(name)}")    
    
    return sorted_birtdays

print(get_birthdays_per_week(users))
