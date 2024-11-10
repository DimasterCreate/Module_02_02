first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('3')
elif first == second: # Хотел использовать elif first == second or second == third or first == third
    print('2')        # но в примечании сказано стараться избегать операторы or, and
elif first == third:
    print('2')
elif third == second:
    print('2')
else:
    print('0')
