1. Бинарная куча
java
public class BinaryHeap {
    private int[] heap;
    private int size;
    private int capacity;
    
    public BinaryHeap(int capacity) {
        this.capacity = capacity;
        this.heap = new int[capacity];
        this.size = 0;
    }
    
    private int parent(int i) { return (i - 1) / 2; }
    private int left(int i) { return 2 * i + 1; }
    private int right(int i) { return 2 * i + 2; }
    
    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
    
    private void heapifyUp(int i) {
        while (i > 0 && heap[i] < heap[parent(i)]) {
            swap(i, parent(i));
            i = parent(i);
        }
    }
    
    private void heapifyDown(int i) {
        int smallest = i;
        int left = left(i);
        int right = right(i);
        
        if (left < size && heap[left] < heap[smallest])
            smallest = left;
        if (right < size && heap[right] < heap[smallest])
            smallest = right;
        
        if (smallest != i) {
            swap(i, smallest);
            heapifyDown(smallest);
        }
    }
    
    public void insert(int key) {
        if (size == capacity) {
            System.out.println("Heap is full");
            return;
        }
        
        heap[size] = key;
        heapifyUp(size);
        size++;
    }
    
    public int extractMin() {
        if (size == 0) throw new IllegalStateException("Heap is empty");
        
        int min = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);
        return min;
    }
    
    public int getMin() {
        if (size == 0) throw new IllegalStateException("Heap is empty");
        return heap[0];
    }
    
    public boolean isEmpty() { return size == 0; }
    public int size() { return size; }

    // Тестирование
    public static void main(String[] args) {
        BinaryHeap heap = new BinaryHeap(10);
        heap.insert(5);
        heap.insert(3);
        heap.insert(8);
        heap.insert(1);
        
        System.out.println("Min: " + heap.getMin());  // 1
        System.out.println("Extract min: " + heap.extractMin());  // 1
        System.out.println("New min: " + heap.getMin());  // 3
    }
}
2.куча фибоначи
  public class FibonacciHeap<T extends Comparable<T>> {
    private static class Node<T> {
        T key;
        int degree = 0;
        Node<T> parent;
        Node<T> child;
        Node<T> left = this;
        Node<T> right = this;
        boolean marked = false;
        
        Node(T key) {
            this.key = key;
        }
    }
    
    private Node<T> minNode;
    private int size;
    
    public boolean isEmpty() {
        return minNode == null;
    }
    
    public Node<T> insert(T key) {
        Node<T> newNode = new Node<>(key);
        
        if (minNode == null) {
            minNode = newNode;
        } else {
            // Add to root list
            newNode.left = minNode.left;
            newNode.right = minNode;
            minNode.left.right = newNode;
            minNode.left = newNode;
            
            if (key.compareTo(minNode.key) < 0) {
                minNode = newNode;
            }
        }
        
        size++;
        return newNode;
    }
    
    public T getMin() {
        if (minNode == null) throw new IllegalStateException("Heap is empty");
        return minNode.key;
    }
    
    public T extractMin() {
        if (minNode == null) throw new IllegalStateException("Heap is empty");
        
        Node<T> min = minNode;
        T minKey = min.key;
        
        // Add children to root list
        if (min.child != null) {
            Node<T> child = min.child;
            Node<T> firstChild = child;
            do {
                Node<T> nextChild = child.right;
                // Remove from child list
                child.left.right = child.right;
                child.right.left = child.left;
                // Add to root list
                child.left = minNode.left;
                child.right = minNode;
                minNode.left.right = child;
                minNode.left = child;
                child.parent = null;
                child = nextChild;
            } while (child != firstChild);
        }
        
        // Remove min from root list
        min.left.right = min.right;
        min.right.left = min.left;
        
        if (min == min.right) {
            minNode = null;
        } else {
            minNode = min.right;
            consolidate();
        }
        
        size--;
        return minKey;
    }
    
    private void consolidate() {
        if (minNode == null) return;
        
        int maxDegree = (int) (Math.log(size) / Math.log(2)) + 1;
        @SuppressWarnings("unchecked")
        Node<T>[] degreeTable = new Node[maxDegree + 1];
        
        java.util.ArrayList<Node<T>> roots = new java.util.ArrayList<>();
        Node<T> current = minNode;
        Node<T> first = current;
        
        do {
            roots.add(current);
            current = current.right;
        } while (current != first);
        
        for (Node<T> node : roots) {
            int degree = node.degree;
            while (degreeTable[degree] != null) {
                Node<T> other = degreeTable[degree];
                if (node.key.compareTo(other.key) > 0) {
                    Node<T> temp = node;
                    node = other;
                    other = temp;
                }
                
                link(other, node);
                degreeTable[degree] = null;
                degree++;
            }
            degreeTable[degree] = node;
        }
        
        minNode = null;
        for (Node<T> node : degreeTable) {
            if (node != null) {
                if (minNode == null) {
                    minNode = node;
                    node.left = node;
                    node.right = node;
                } else {
                    node.left = minNode.left;
                    node.right = minNode;
                    minNode.left.right = node;
                    minNode.left = node;
                    
                    if (node.key.compareTo(minNode.key) < 0) {
                        minNode = node;
                    }
                }
            }
        }
    }
    
    private void link(Node<T> child, Node<T> parent) {
        // Remove child from root list
        child.left.right = child.right;
        child.right.left = child.left;
        
        // Make child a child of parent
        child.parent = parent;
        if (parent.child == null) {
            parent.child = child;
            child.right = child;
            child.left = child;
        } else {
            child.left = parent.child.left;
            child.right = parent.child;
            parent.child.left.right = child;
            parent.child.left = child;
        }
        
        parent.degree++;
        child.marked = false;
    }
    
    public void decreaseKey(Node<T> node, T newKey) {
        if (newKey.compareTo(node.key) > 0) {
            throw new IllegalArgumentException("New key must be smaller");
        }
        
        node.key = newKey;
        Node<T> parent = node.parent;
        
        if (parent != null && node.key.compareTo(parent.key) < 0) {
            cut(node, parent);
            cascadingCut(parent);
        }
        
        if (node.key.compareTo(minNode.key) < 0) {
            minNode = node;
        }
    }
    
    private void cut(Node<T> node, Node<T> parent) {
        // Remove node from parent's child list
        if (node.right == node) {
            parent.child = null;
        } else {
            node.left.right = node.right;
            node.right.left = node.left;
            if (parent.child == node) {
                parent.child = node.right;
            }
        }
        
        parent.degree--;
        
        // Add node to root list
        node.left = minNode.left;
        node.right = minNode;
        minNode.left.right = node;
        minNode.left = node;
        
        node.parent = null;
        node.marked = false;
    }
    
    private void cascadingCut(Node<T> node) {
        Node<T> parent = node.parent;
        if (parent != null) {
            if (!node.marked) {
                node.marked = true;
            } else {
                cut(node, parent);
                cascadingCut(parent);
            }
        }
    }
    
    public void delete(Node<T> node) {
        decreaseKey(node, getMinValue());
        extractMin();
    }
    
    @SuppressWarnings("unchecked")
    private T getMinValue() {
        // Return minimal possible value for type T
        if (minNode.key instanceof Integer) {
            return (T) Integer.valueOf(Integer.MIN_VALUE);
        } else if (minNode.key instanceof Double) {
            return (T) Double.valueOf(Double.MIN_VALUE);
        } else {
            throw new UnsupportedOperationException("Unsupported type");
        }
    }
    
    public int size() { return size; }

    // Тестирование
    public static void main(String[] args) {
        FibonacciHeap<Integer> fibHeap = new FibonacciHeap<>();
        FibonacciHeap<Integer>.Node<Integer> node1 = fibHeap.insert(10);
        FibonacciHeap<Integer>.Node<Integer> node2 = fibHeap.insert(5);
        FibonacciHeap<Integer>.Node<Integer> node3 = fibHeap.insert(20);
        FibonacciHeap<Integer>.Node<Integer> node4 = fibHeap.insert(3);
        FibonacciHeap<Integer>.Node<Integer> node5 = fibHeap.insert(8);
        
        System.out.println("Min: " + fibHeap.getMin());  // 3
        System.out.println("Extract min: " + fibHeap.extractMin());  // 3
        System.out.println("New min: " + fibHeap.getMin());  // 5
        
        fibHeap.decreaseKey(node2, 2);
        System.out.println("After decrease key, min: " + fibHeap.getMin());  // 2
    }
}
3. Хеш-таблица
java
public class HashTable<K, V> {
    private static class Entry<K, V> {
        K key;
        V value;
        Entry<K, V> next;
        
        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private Entry<K, V>[] table;
    private int capacity;
    private int size;
    
    @SuppressWarnings("unchecked")
    public HashTable(int capacity) {
        this.capacity = capacity;
        this.table = new Entry[capacity];
        this.size = 0;
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % capacity;
    }
    
    public void put(K key, V value) {
        if (size >= capacity * 0.7) resize();
        
        int index = hash(key);
        Entry<K, V> newEntry = new Entry<>(key, value);
        
        if (table[index] == null) {
            table[index] = newEntry;
        } else {
            Entry<K, V> current = table[index];
            while (current.next != null) {
                if (current.key.equals(key)) {
                    current.value = value;
                    return;
                }
                current = current.next;
            }
            if (current.key.equals(key)) {
                current.value = value;
            } else {
                current.next = newEntry;
            }
        }
        size++;
    }
    
    public V get(K key) {
        int index = hash(key);
        Entry<K, V> current = table[index];
        
        while (current != null) {
            if (current.key.equals(key)) {
                return current.value;
            }
            current = current.next;
        }
        throw new RuntimeException("Key not found: " + key);
    }
    
    public void remove(K key) {
        int index = hash(key);
        Entry<K, V> current = table[index];
        Entry<K, V> prev = null;
        
        while (current != null) {
            if (current.key.equals(key)) {
                if (prev == null) {
                    table[index] = current.next;
                } else {
                    prev.next = current.next;
                }
                size--;
                return;
            }
            prev = current;
            current = current.next;
        }
        throw new RuntimeException("Key not found: " + key);
    }
    
    @SuppressWarnings("unchecked")
    private void resize() {
        capacity *= 2;
        Entry<K, V>[] oldTable = table;
        table = new Entry[capacity];
        size = 0;
        
        for (Entry<K, V> entry : oldTable) {
            Entry<K, V> current = entry;
            while (current != null) {
                put(current.key, current.value);
                current = current.next;
            }
        }
    }
    
    public boolean contains(K key) {
        try {
            get(key);
            return true;
        } catch (RuntimeException e) {
            return false;
        }
    }
    
    public int size() { return size; }

    // Тестирование
    public static void main(String[] args) {
        HashTable<String, Integer> table = new HashTable<>(10);
        table.put("apple", 1);
        table.put("banana", 2);
        table.put("cherry", 3);
        
        System.out.println("apple: " + table.get("apple"));  // 1
        table.remove("banana");
        System.out.println("Contains banana: " + table.contains("banana"));  // false
    }
}
