import random

def gen_sorted_arrays(n):
    if not isinstance(n, int):
        raise TypeError(f"Параметр n должен быть целым, натуральным числом! n: {n}")
    if n < 0 or n == 0:
        raise ValueError(f"Праметр n не является натуральным! n: {n}")

    arrays = []
    # генерируем случайные, неповторяющиеся длины n-массивов
    # и заполняем массивы случайными числами
    for size in random.sample(range(1, n * 2), n):
        arrays.append(random.choices(range(0, size ** 2), k=size))

    even_arrays = []
    odd_arrays = []

    # Массивы с четным порядковым номером отсортировать по возрастанию, 
    # с нечетным порядковым номером - по убыванию. 
    for i in range(n):
        if i % 2 == 0:
            even_arrays.append(sorted(arrays[i]))
        else:
            odd_arrays.append(sorted(arrays[i], reverse=True))
    # возвращаем массив массивов
    return even_arrays + odd_arrays
# Пример использования
result = gen_sorted_arrays(8)
print(result)