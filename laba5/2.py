def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Внутренний цикл проходит по массиву, сравнивая соседние элементы
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# пример использования
test_array = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", test_array)
bubble_sort(test_array)
print("Отсортированный массив:", test_array)