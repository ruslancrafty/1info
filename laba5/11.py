def fibonacci_search(arr, target):
    n = len(arr)
    # Генерируем числа Фибоначчи до тех пор, пока они не станут больше или равны размеру массива
    fibMMm2 = 0  # F(m-2)
    fibMMm1 = 1  # F(m-1)
    fibM = fibMMm2 + fibMMm1  # F(m)

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1

    while fibM > 1:
        # Предполагаемая позиция
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i  # найден

    # проверка последнего элемента
    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1  # не найден

# пример использования
array = [10, 22, 35, 40, 50, 80, 82, 85, 90, 100]
target = 85
index = fibonacci_search(array, target)
if index != -1:
    print(f"Элемент {target} найден на позиции: {index}")
else:
    print("Элемент не найден")