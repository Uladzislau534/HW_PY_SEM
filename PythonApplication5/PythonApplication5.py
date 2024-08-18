

N = int(input("Введите число карточек — N: "))


total_sum = N * (N + 1) // 2


remaining_sum = 0


for _ in range(N - 1):
    card_number = int(input("Введите номер оставшейся карточки: "))
    remaining_sum += card_number


lost_card = total_sum - remaining_sum

print(f"Потерянная карточка: {lost_card}")
