def insertion_sort(arr):
    # Проходим по каждому элементу начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]  # текущий элемент, который вставляем
        j = i - 1  # индекс предыдущего элемента
        # Смещаем элементы, которые больше key, вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # вставляем ключ на правильное место
    return arr

# пример использования
test_array = [12, 11, 13, 5, 6]
print("Исходный массив:", test_array)
insertion_sort(test_array)
print("Отсортированный массив:", test_array)