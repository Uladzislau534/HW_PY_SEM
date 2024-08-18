

total_salary = 0

for month in range(1, 13):
    salary = float(input(f"Введите зарплату за месяц {month}: "))
 
    total_salary += salary


average_salary = total_salary / 12

print(f"Средняя зарплата за год: {average_salary:.2f}")
