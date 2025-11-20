class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # удельная стоимость
    
    def __repr__(self):
        return f"(вес={self.weight}, стоимость={self.value})"

def fractional_knapsack(items, capacity):
    # Сортируем предметы по убыванию удельной стоимости
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    selected_items = []
    remaining_capacity = capacity
    
    for item in items:
        if remaining_capacity <= 0:
            break
            
        # Берем предмет целиком, если он помещается
        if item.weight <= remaining_capacity:
            fraction = 1.0
            taken_weight = item.weight
            total_value += item.value
        else:
            # Берем дробную часть предмета
            fraction = remaining_capacity / item.weight
            taken_weight = remaining_capacity
            total_value += item.value * fraction
        
        selected_items.append({
            'item': item,
            'fraction': fraction,
            'taken_weight': taken_weight,
            'taken_value': item.value * fraction
        })
        
        remaining_capacity -= taken_weight
    
    return total_value, selected_items

def input_items():
    """Функция для ручного ввода предметов"""
    items = []
    
    print("\n=== ВВОД ПРЕДМЕТОВ ===")
    print("Введите данные для каждого предмета (вес и стоимость)")
    print("Для завершения ввода введите '0' для веса")
    
    i = 1
    while True:
        print(f"\n--- Предмет {i} ---")
        try:
            weight = float(input("Введите вес предмета: "))
            if weight == 0:
                break
                
            if weight < 0:
                print("Вес не может быть отрицательным. Попробуйте снова.")
                continue
                
            value = float(input("Введите стоимость предмета: "))
            if value < 0:
                print("Стоимость не может быть отрицательной. Попробуйте снова.")
                continue
                
            items.append(Item(weight, value))
            i += 1
            
        except ValueError:
            print("Ошибка! Введите числовое значение.")
    
    return items

def input_capacity():
    """Функция для ввода вместимости рюкзака"""
    while True:
        try:
            capacity = float(input("\nВведите вместимость рюкзака: "))
            if capacity <= 0:
                print("Вместимость должна быть положительной. Попробуйте снова.")
                continue
            return capacity
        except ValueError:
            print("Ошибка! Введите числовое значение.")

def main():
    print("=== РЮКЗАК С ДРОБНЫМИ ПРЕДМЕТАМИ ===")
    print("Алгоритм решения задачи о рюкзаке с дробными предметами")
    
    # Ручной ввод данных
    items = input_items()
    
    if not items:
        print("Не введено ни одного предмета. Программа завершена.")
        return
    
    capacity = input_capacity()
    
    # Вывод введенных данных
    print("\n=== ВВЕДЕННЫЕ ДАННЫЕ ===")
    print("Предметы:")
    for i, item in enumerate(items, 1):
        print(f"Предмет {i}: {item}, удельная стоимость: {item.ratio:.2f}")
    
    print(f"Вместимость рюкзака: {capacity}")
    
    # Решаем задачу
    max_value, selected = fractional_knapsack(items, capacity)
    
    # Вывод результатов
    print("\n=== РЕЗУЛЬТАТЫ ===")
    print(f"Максимальная стоимость: {max_value:.2f}")
    print("\nВыбранные предметы:")
    
    if not selected:
        print("Ни один предмет не поместился в рюкзак")
    else:
        for i, selection in enumerate(selected, 1):
            item = selection['item']
            fraction = selection['fraction']
            taken_weight = selection['taken_weight']
            taken_value = selection['taken_value']
            
            if fraction == 1.0:
                print(f"{i}. {item} - взят целиком")
            else:
                print(f"{i}. {item} - взято {fraction:.2f} части (вес: {taken_weight:.2f})")
            
            print(f"   Внесенный вклад: {taken_value:.2f}")
    
    # Статистика
    print(f"\n=== СТАТИСТИКА ===")
    print(f"Использовано вместимости: {capacity - (capacity - sum(s['taken_weight'] for s in selected)):.2f} из {capacity}")
    print(f"Эффективность: {(max_value / capacity * 100):.2f}% стоимости на единицу веса")

if __name__ == "__main__":
    main()
