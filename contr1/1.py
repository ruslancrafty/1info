1. Блочная сортировка (Bucket Sort) - bucket_sort.py
python
def bucket_sort(arr):
    """
    Реализация блочной (корзинной) сортировки
    """
    if len(arr) == 0:
        return arr
    
    # 1. Определяем количество корзин и находим min/max значения
    n = len(arr)
    min_val, max_val = min(arr), max(arr)
    
    # Если все элементы одинаковые, возвращаем массив
    if min_val == max_val:
        return arr
    
    # 2. Создаём корзины
    bucket_count = n  # количество корзин = количеству элементов
    buckets = [[] for _ in range(bucket_count)]
    
    # 3. Распределяем элементы по корзинам
    for num in arr:
        # Вычисляем индекс корзины
        index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)
    
    # 4. Сортируем каждую корзину (используем встроенную сортировку)
    for i in range(bucket_count):
        buckets[i].sort()
    
    # 5. Объединяем корзины в результирующий массив
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

# Тестирование алгоритма
if __name__ == "__main__":
    # Пример с равномерно распределёнными данными
    test_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Исходный массив:", test_array)
    
    sorted_array = bucket_sort(test_array)
    print("Отсортированный массив:", sorted_array)
    
    # Пример с целыми числами
    int_array = [29, 25, 3, 49, 9, 37, 21, 43]
    print("\nИсходный массив:", int_array)
    print("Отсортированный массив:", bucket_sort(int_array))
2. Блинная сортировка (Pancake Sort) - pancake_sort.py
python
def flip(arr, i):
    """
    Переворачивает массив от индекса 0 до i
    """
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_index(arr, n):
    """
    Находит индекс максимального элемента в подмассиве [0, n-1]
    """
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """
    Реализация блинной сортировки
    """
    n = len(arr)
    
    # Постепенно уменьшаем размер неотсортированной части
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в неотсортированной части
        max_index = find_max_index(arr, curr_size)
        
        # Если максимальный элемент не на своём месте
        if max_index != curr_size - 1:
            # Переворачиваем так, чтобы максимальный элемент оказался первым
            if max_index != 0:
                flip(arr, max_index)
            
            # Переворачиваем всю неотсортированную часть, 
            # чтобы максимальный элемент оказался в конце
            flip(arr, curr_size - 1)
    
    return arr

# Тестирование алгоритма
if __name__ == "__main__":
    test_array = [23, 10, 20, 11, 12, 6, 7]
    print("Исходный массив:", test_array)
    
    sorted_array = pancake_sort(test_array.copy())
    print("Отсортированный массив:", sorted_array)
    
    # Демонстрация работы переворота
    demo_array = [3, 2, 1, 5, 4]
    print(f"\nДемонстрация переворота:")
    print(f"До переворота: {demo_array}")
    flip(demo_array, 2)  # Переворачиваем первые 3 элемента
    print(f"После переворота первых 3 элементов: {demo_array}")
3. Сортировка бусинами (Bead Sort) - bead_sort.py
python
def bead_sort(arr):
    """
    Реализация сортировки бусинами (гравитационной сортировки)
    Работает только для неотрицательных целых чисел
    """
    if not arr or len(arr) == 0:
        return arr
    
    # Находим максимальный элемент для определения количества "стержней"
    max_val = max(arr)
    
    # Создаём матрицу бусин
    beads = [[0] * len(arr) for _ in range(max_val)]
    
    # 1. Распределяем бусины по стержням
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # 2. Заставляем бусины "упасть" под действием гравитации
    for i in range(max_val):
        # Считаем количество бусин в каждом ряду
        bead_count = sum(beads[i])
        
        # "Сбрасываем" все бусины в ряду
        for j in range(len(arr)):
            beads[i][j] = 0
        
        # Размещаем бусины внизу ряда
        for j in range(len(arr) - bead_count, len(arr)):
            beads[i][j] = 1
    
    # 3. Считываем результат снизу вверх
    result = [0] * len(arr)
    for j in range(len(arr)):
        # Считаем количество бусин в каждом столбце
        for i in range(max_val):
            result[j] += beads[i][j]
    
    return result

def bead_sort_optimized(arr):
    """
    Оптимизированная версия сортировки бусинами
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    
    # Создаём счётчик бусин для каждого уровня
    beads = [0] * max_val
    
    # Распределяем бусины по уровням
    for num in arr:
        for i in range(num):
            beads[i] += 1
    
    # Собираем результат
    result = []
    for level in range(max_val, 0, -1):
        result.append(beads[level - 1])
        for i in range(level - 1):
            if beads[i] > beads[i + 1]:
                beads[i] -= 1
                beads[i + 1] += 1
    
    return result[::-1]

# Тестирование алгоритма
if __name__ == "__main__":
    # Только для неотрицательных целых чисел
    test_array = [3, 1, 4, 1, 5, 2]
    print("Исходный массив:", test_array)
    
    sorted_array = bead_sort(test_array.copy())
    print("Отсортированный массив (базовая версия):", sorted_array)
    
    sorted_opt = bead_sort_optimized(test_array.copy())
    print("Отсортированный массив (оптимизированная):", sorted_opt)
Код для алгоритмов поиска
4. Поиск скачками (Jump Search) - jump_search.py
python
import math

def jump_search(arr, target):
    """
    Реализация поиска скачками в отсортированном массиве
    """
    n = len(arr)
    
    # Если массив пустой
    if n == 0:
        return -1
    
    # Определяем размер прыжка
    step = int(math.sqrt(n))
    
    # 1. Фаза прыжков - находим блок, где может быть элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Элемент не найден
    
    # 2. Фаза линейного поиска в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1  # Элемент не найден
    
    # Проверяем, найден ли элемент
    if arr[prev] == target:
        return prev
    else:
        return -1

# Тестирование алгоритма
if __name__ == "__main__":
    # Массив должен быть отсортирован
    sorted_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    target = 34
    
    print("Отсортированный массив:", sorted_array)
    print(f"Поиск элемента {target}")
    
    result = jump_search(sorted_array, target)
    
    if result != -1:
        print(f"Элемент найден на позиции {result}")
    else:
        print("Элемент не найден")
    
    # Поиск несуществующего элемента
    target2 = 100
    result2 = jump_search(sorted_array, target2)
    print(f"\nПоиск элемента {target2}: {'найден' if result2 != -1 else 'не найден'}")
5. Экспоненциальный поиск (Exponential Search) - exponential_search.py
python
def binary_search(arr, left, right, target):
    """
    Вспомогательная функция бинарного поиска
    """
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def exponential_search(arr, target):
    """
    Реализация экспоненциального поиска в отсортированном массиве
    """
    n = len(arr)
    
    # Если массив пустой
    if n == 0:
        return -1
    
    # 1. Проверяем первый элемент
    if arr[0] == target:
        return 0
    
    # 2. Экспоненциально увеличиваем границы поиска
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # 3. Выполняем бинарный поиск в найденном диапазоне
    left = i // 2
    right = min(i, n - 1)
    
    return binary_search(arr, left, right, target)

# Тестирование алгоритма
if __name__ == "__main__":
    # Массив должен быть отсортирован
    sorted_array = [2, 3, 4, 10, 15, 18, 20, 23, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    target = 45
    
    print("Отсортированный массив:", sorted_array)
    print(f"Поиск элемента {target}")
    
    result = exponential_search(sorted_array, target)
    
    if result != -1:
        print(f"Элемент найден на позиции {result}")
    else:
        print("Элемент не найден")
    
    # Поиск элемента в начале массива
    target2 = 3
    result2 = exponential_search(sorted_array, target2)
    print(f"\nПоиск элемента {target2} в начале массива: позиция {result2}")
6. Тернарный поиск (Ternary Search) - ternary_search.py
python
def ternary_search(arr, target):
    """
    Реализация тернарного поиска в отсортированном массиве
    """
    return ternary_search_recursive(arr, target, 0, len(arr) - 1)

def ternary_search_recursive(arr, target, left, right):
    """
    Рекурсивная версия тернарного поиска
    """
    if left > right:
        return -1
    
    # 1. Делим диапазон на три части
    partition_size = (right - left) // 3
    mid1 = left + partition_size
    mid2 = right - partition_size
    
    # 2. Проверяем граничные точки
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    # 3. Определяем, в какой трети продолжать поиск
    if target < arr[mid1]:
        # Ищем в левой трети
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        # Ищем в правой трети
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        # Ищем в средней трети
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

def ternary_search_iterative(arr, target):
    """
    Итеративная версия тернарного поиска
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        partition_size = (right - left) // 3
        mid1 = left + partition_size
        mid2 = right - partition_size
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Тестирование алгоритма
if __name__ == "__main__":
    # Массив должен быть отсортирован
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    target = 10
    
    print("Отсортированный массив:", sorted_array)
    print(f"Поиск элемента {target}")
    
    # Рекурсивная версия
    result_recursive = ternary_search(sorted_array, target)
    print(f"Рекурсивный поиск: позиция {result_recursive}")
    
    # Итеративная версия
    result_iterative = ternary_search_iterative(sorted_array, target)
    print(f"Итеративный поиск: позиция {result_iterative}")
    
    # Сравнение с бинарным поиском
    import bisect
    binary_result = bisect.bisect_left(sorted_array, target)
    if binary_result < len(sorted_array) and sorted_array[binary_result] == target:
        print(f"Библиотечный бинарный поиск: позиция {binary_result}")