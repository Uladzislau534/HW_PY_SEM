

secret_number = 7

attempts = 0

while True:
 
    guess = int(input("Введите число: "))
    
    attempts += 1
    
    if guess < secret_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif guess > secret_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print(f"Вы угадали! Число попыток: {attempts}")
        break
