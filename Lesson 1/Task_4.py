def bank(summ, years, perc):
    if perc > 1:
        perc = perc / 100

    result = summ + years * perc * summ
    return result


new_summ = int(input('Введите сумму: '))
new_years = int(input('Срок депозита: '))
new_perc = int(input('Процентов годовых: '))

print(bank(new_summ, new_years, new_perc))
