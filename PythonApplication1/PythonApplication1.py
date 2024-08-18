
positive_count = 0
negative_count = 0

while True:
 
    number = int(input("Введите число: "))
    
    if number == 0:
        break
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print(f"Кол-во положительных чисел: {positive_count}")
print(f"Кол-во отрицательных чисел: {negative_count}")

