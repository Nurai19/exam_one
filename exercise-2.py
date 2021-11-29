while True:
    deposit_sum = int(input('Введите сумму депозита: '))
    final_sum = int(input('Введите желаемую конечную сумму: '))
    year_procent = int(input('Введите годовой процент: '))

    if deposit_sum <= 0 or final_sum <= 0 or year_procent <= 0:
        print('Введена неверные данные')
        continue
    else:
        print(f'Количество месяцев: {(final_sum - deposit_sum) / (deposit_sum /100*year_procent)}')
        break
