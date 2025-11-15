
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

def main():
    # Входные данные
    items = [
        Item(2, 10),
        Item(3, 20),
        Item(4, 15),
        Item(5, 25)
    ]
    capacity = 8
    
    print("Исходные предметы:")
    for i, item in enumerate(items, 1):
        print(f"Предмет {i}: {item}, удельная стоимость: {item.ratio:.2f}")
    
    print(f"\nВместимость рюкзака: {capacity}")
    
    # Решаем задачу
    max_value, selected = fractional_knapsack(items, capacity)
    
    print(f"\nМаксимальная стоимость: {max_value:.2f}")
    print("\nНабор предметов:")
    for i, selection in enumerate(selected, 1):
        item = selection['item']
        fraction = selection['fraction']
        taken_weight = selection['taken_weight']
        taken_value = selection['taken_value']
        
        if fraction == 1.0:
            print(f"Предмет {i}: {item} - взят целиком")
        else:
            print(f"Предмет {i}: {item} - взято {fraction:.2f} части (вес: {taken_weight:.2f})")
        
        print(f"  Внесенный вклад: {taken_value:.2f}")

if __name__ == "__main__":

    main()

Исходные предметы:
Предмет 1: (вес=2, стоимость=10), удельная стоимость: 5.00
Предмет 2: (вес=3, стоимость=20), удельная стоимость: 6.67
Предмет 3: (вес=4, стоимость=15), удельная стоимость: 3.75
Предмет 4: (вес=5, стоимость=25), удельная стоимость: 5.00

Вместимость рюкзака: 8

Максимальная стоимость: 36.67

Набор предметов:
Предмет 1: (вес=3, стоимость=20) - взят целиком
  Внесенный вклад: 20.00
Предмет 2: (вес=2, стоимость=10) - взят целиком
  Внесенный вклад: 10.00
Предмет 3: (вес=5, стоимость=25) - взято 0.60 части (вес: 3.00)
  Внесенный вклад: 15.00
