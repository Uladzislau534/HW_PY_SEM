

total_tasks = 0
called_wife = False


for hour in range(1, 9):
    tasks = int(input(f"{hour}-й час\nСколько задач решит Максим? "))
    total_tasks += tasks
    
    call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    
    if call == 1:
        called_wife = True

print(f"Максим выполнил {total_tasks} задач.")

if called_wife:
    print("Нужно зайти в магазин.")
