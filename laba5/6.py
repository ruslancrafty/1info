def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # выбор опорного элемента, например, последний
    pivot = arr[-1]
    left = []
    right = []
    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    # рекурсивная сортировка частей и объединение
    return quick_sort(left) + [pivot] + quick_sort(right)

# пример использования
test_array = [10, 7, 8, 9, 1, 5]
print("Исходный массив:", test_array)
sorted_array = quick_sort(test_array)
print("Отсортированный массив:", sorted_array)