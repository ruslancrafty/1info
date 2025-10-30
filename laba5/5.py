def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for in range(gap, n):
            temp = arr[i]
            j = i
            # вставка элемента arr[i] в отсортированную подчасть
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# пример использования
test_array = [12, 34, 54, 2, 3]
print("Исходный массив:", test_array)
shell_sort(test_array)
print("Отсортированный массив:", test_array)