from datetime import date

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(f'Сегодня {date.today()}')
    print(f'У {get_employees()} будет зарплата {calculate_salary()}!')