Бинарная куча
class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
    
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0

# Тестирование
heap = BinaryHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
print("Min:", heap.get_min())  # 1
print("Extract min:", heap.extract_min())  # 1
print("New min:", heap.get_min())  # 3
...................................................
куча фибоначи

class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.marked = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.node_count = 0
    
    def is_empty(self):
        return self.min_node is None
    
    def insert(self, key):
        new_node = FibonacciNode(key)
        
        if self.min_node is None:
            self.min_node = new_node
        else:
            # Добавляем новый узел в корневой список слева от min_node
            new_node.left = self.min_node.left
            new_node.right = self.min_node
            self.min_node.left.right = new_node
            self.min_node.left = new_node
            
            if key < self.min_node.key:
                self.min_node = new_node
        
        self.node_count += 1
        return new_node
    
    def get_min(self):
        return self.min_node.key if self.min_node else None
    
    def extract_min(self):
        if self.min_node is None:
            return None
        
        min_node = self.min_node
        min_key = min_node.key
        
        # Добавляем детей min_node в корневой список
        if min_node.child:
            child = min_node.child
            first_child = child
            while True:
                next_child = child.right
                # Добавляем ребенка в корневой список
                child.left.right = child.right
                child.right.left = child.left
                child.left = self.min_node.left
                child.right = self.min_node
                self.min_node.left.right = child
                self.min_node.left = child
                child.parent = None
                
                if next_child == first_child:
                    break
                child = next_child
        
        # Удаляем min_node из корневого списка
        min_node.left.right = min_node.right
        min_node.right.left = min_node.left
        
        if min_node == min_node.right:
            self.min_node = None
        else:
            self.min_node = min_node.right
            self._consolidate()
        
        self.node_count -= 1
        return min_key
    
    def _consolidate(self):
        if self.min_node is None:
            return
        
        # Создаем массив для деревьев разных степеней
        degree_table = [None] * (self.node_count.bit_length() + 1)
        
        nodes = []
        current = self.min_node
        first = current
        
        # Собираем все корневые узлы
        while True:
            nodes.append(current)
            current = current.right
            if current == first:
                break
        
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                
                self._link(other, node)
                degree_table[degree] = None
                degree += 1
            
            degree_table[degree] = node
        
        # Восстанавливаем min_node
        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                    node.left = node
                    node.right = node
                else:
                    # Добавляем node в корневой список
                    node.left = self.min_node.left
                    node.right = self.min_node
                    self.min_node.left.right = node
                    self.min_node.left = node
                    
                    if node.key < self.min_node.key:
                        self.min_node = node
    
    def _link(self, child, parent):
        # Удаляем child из корневого списка
        child.left.right = child.right
        child.right.left = child.left
        
        # Делаем child дочерним для parent
        child.parent = parent
        if parent.child is None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            child.left = parent.child.left
            child.right = parent.child
            parent.child.left.right = child
            parent.child.left = child
        
        parent.degree += 1
        child.marked = False
    
    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key must be smaller than current key")
        
        node.key = new_key
        parent = node.parent
        
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        
        if node.key < self.min_node.key:
            self.min_node = node
    
    def _cut(self, node, parent):
        # Удаляем node из списка детей parent
        if node.right == node:
            parent.child = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if parent.child == node:
                parent.child = node.right
        
        parent.degree -= 1
        
        # Добавляем node в корневой список
        node.left = self.min_node.left
        node.right = self.min_node
        self.min_node.left.right = node
        self.min_node.left = node
        
        node.parent = None
        node.marked = False
    
    def _cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)
    
    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

# Тестирование

fib_heap = FibonacciHeap()
nodes = []
nodes.append(fib_heap.insert(10))
nodes.append(fib_heap.insert(5))
nodes.append(fib_heap.insert(20))
nodes.append(fib_heap.insert(3))
nodes.append(fib_heap.insert(8))

print("Min:", fib_heap.get_min())  # 3
print("Extract min:", fib_heap.extract_min())  # 3
print("New min:", fib_heap.get_min())  # 5

fib_heap.decrease_key(nodes[1], 2)  # Уменьшаем ключ с 5 до 2
print("After decrease key, min:", fib_heap.get_min())  # 2

.............................
Хеш-таблица
class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        if self.count / self.size > 0.7:
            self._resize()
        
        index = self._hash(key)
        new_node = HashNode(key, value)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node
        self.count += 1
    
    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key {key} not found")
    
    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return
            prev = current
            current = current.next
        raise KeyError(f"Key {key} not found")
    
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        
        for node in old_table:
            current = node
            while current:
                self.put(current.key, current.value)
                current = current.next

# Тестирование
ht = HashTable()
ht.put("apple", 1)
ht.put("banana", 2)
ht.put("cherry", 3)
print("Get apple:", ht.get("apple"))  # 1
ht.remove("banana")

