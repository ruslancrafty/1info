def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # нашли элемент
        elif arr[mid] < target:
            left = mid + 1  # ищем в правой части
        else:
            right = mid - 1  # ищем в левой части
    return -1  # не нашли

# пример использования
sorted_array = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(sorted_array, target_value)

if result -1:
    print(f"Элемент {target_value} найден на позиции {result}")
else:
    print(f"Элемент {target_value} не")