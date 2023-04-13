# Угадать два числа по их сумме и произведению.
sum = int(input('Сумма: '))
prod = int(input('Произведение: '))
flag = False
for i in range(sum):
    for j in range(prod):
        if sum == i + j and prod == i * j:
            print(f'Числа: {i} и {j}')
            flag = True
if flag == False:
    print('Условие невыполнимо!')
