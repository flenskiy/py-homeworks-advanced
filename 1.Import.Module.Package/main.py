from datetime import date
from application import salary
from application.db import people

if __name__ == '__main__':
    print('date:', date.today())
    salary.calculate_salary()
    people.get_employees()
