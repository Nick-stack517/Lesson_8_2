def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in i:
            try:
                result += j
            except TypeError:
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммы - {j}')
    return result, incorrect_data


def calculate_average(*numbers):
    if isinstance(*numbers, int):
        print('В numbers записан некорректный тип данных')
        return None
    try:
        local_sum = personal_sum(*numbers)
        # print(local_sum[0])
        # print(len(*numbers))
        # print(local_sum[1])

        return local_sum[0] / (len(*numbers) - local_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 'В numbers записан некорректный тип данных'


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
