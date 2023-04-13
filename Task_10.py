# Сколько минимум монет перевернуть, чтобы они были одной стороной.
n = int(input('Количество монет: '))
orel = 0
reshka = 0
import random
for i in range(n):
    x = random.randint(0, 1)
    print(x, end=' ')
    if x == 0:
        orel += 1
    else:
        reshka += 1
print()
print('Перевернуть необходимо: ', end='')
if orel < reshka:
    print(orel)
else:
    print(reshka)
