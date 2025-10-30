def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i  # возвращаем индекс найденного элемента
    return -1  # возвращаем -1, если элемент не найден

# пример использования
test_array = [3, 5, 2, 7, 9, 1, 4]
target_value = 7
result = linear_search(test_array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден на позиции: {result}")
else:
    print(f"Элемент {target_value} не найден в массиве.")