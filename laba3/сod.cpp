1. Бинарная куча
cpp
#include <iostream>
#include <vector>
#include <stdexcept>

template<typename T>
class MinHeap {
private:
    std::vector<T> heap;
    
    int parent(int i) { return (i - 1) / 2; }
    int left(int i) { return 2 * i + 1; }
    int right(int i) { return 2 * i + 2; }
    
    void heapifyUp(int i) {
        while (i > 0 && heap[i] < heap[parent(i)]) {
            std::swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
    
    void heapifyDown(int i) {
        int smallest = i;
        int l = left(i);
        int r = right(i);
        
        if (l < heap.size() && heap[l] < heap[smallest])
            smallest = l;
        if (r < heap.size() && heap[r] < heap[smallest])
            smallest = r;
        
        if (smallest != i) {
            std::swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    void insert(T key) {
        heap.push_back(key);
        heapifyUp(heap.size() - 1);
    }
    
    T extractMin() {
        if (heap.empty()) throw std::runtime_error("Heap is empty");
        
        T min = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
        return min;
    }
    
    T getMin() {
        if (heap.empty()) throw std::runtime_error("Heap is empty");
        return heap[0];
    }
    
    bool empty() { return heap.empty(); }
    size_t size() { return heap.size(); }
};

// Тестирование
int main() {
    MinHeap<int> heap;
    heap.insert(5);
    heap.insert(3);
    heap.insert(8);
    heap.insert(1);
    
    std::cout << "Min: " << heap.getMin() << std::endl;  // 1
    std::cout << "Extract min: " << heap.extractMin() << std::endl;  // 1
    std::cout << "New min: " << heap.getMin() << std::endl;  // 3
    
    return 0;
}
.................................................
    #include <iostream>
#include <vector>
#include <algorithm>

struct BinomialNode {
    int key;
    int degree;
    BinomialNode* parent;
    BinomialNode* child;
    BinomialNode* sibling;
    
    BinomialNode(int k) : key(k), degree(0), parent(nullptr), 
                         child(nullptr), sibling(nullptr) {}
};

class BinomialHeap {
private:
    BinomialNode* head;
    
    BinomialNode* merge(BinomialNode* h1, BinomialNode* h2) {
        if (!h1) return h2;
        if (!h2) return h1;
        
        BinomialNode* result = nullptr;
        BinomialNode** current = &result;
        
        while (h1 && h2) {
            if (h1->degree <= h2->degree) {
                *current = h1;
                h1 = h1->sibling;
            } else {
                *current = h2;
                h2 = h2->sibling;
            }
            current = &((*current)->sibling);
        }
        
        *current = h1 ? h1 : h2;
        return result;
    }
    
    void link(BinomialNode* y, BinomialNode* z) {
        y->parent = z;
        y->sibling = z->child;
        z->child = y;
        z->degree++;
    }
    
    BinomialNode* unionHeaps(BinomialNode* h1, BinomialNode* h2) {
        BinomialNode* newHead = merge(h1, h2);
        if (!newHead) return nullptr;
        
        BinomialNode* prev = nullptr;
        BinomialNode* x = newHead;
        BinomialNode* next = x->sibling;
        
        while (next) {
            if (x->degree != next->degree || 
                (next->sibling && next->sibling->degree == x->degree)) {
                prev = x;
                x = next;
            } else if (x->key <= next->key) {
                x->sibling = next->sibling;
                link(next, x);
            } else {
                if (!prev) {
                    newHead = next;
                } else {
                    prev->sibling = next;
                }
                link(x, next);
                x = next;
            }
            next = x->sibling;
        }
        
        return newHead;
    }
    
    BinomialNode* reverseList(BinomialNode* node) {
        BinomialNode* prev = nullptr;
        BinomialNode* current = node;
        
        while (current) {
            BinomialNode* next = current->sibling;
            current->sibling = prev;
            current->parent = nullptr;
            prev = current;
            current = next;
        }
        
        return prev;
    }

public:
    BinomialHeap() : head(nullptr) {}
    
    bool is_empty() const {
        return head == nullptr;
    }
    
    void insert(int key) {
        BinomialHeap newHeap;
        BinomialNode* newNode = new BinomialNode(key);
        newHeap.head = newNode;
        head = unionHeaps(head, newHeap.head);
    }
    
    int get_min() {
        if (!head) throw std::runtime_error("Heap is empty");
        
        BinomialNode* minNode = head;
        BinomialNode* current = head->sibling;
        
        while (current) {
            if (current->key < minNode->key) {
                minNode = current;
            }
            current = current->sibling;
        }
        
        return minNode->key;
    }
    
    int extract_min() {
        if (!head) throw std::runtime_error("Heap is empty");
        
        // Find min node and its previous
        BinomialNode* minNode = head;
        BinomialNode* prevMin = nullptr;
        BinomialNode* prev = nullptr;
        BinomialNode* current = head;
        
        while (current) {
            if (current->key < minNode->key) {
                minNode = current;
                prevMin = prev;
            }
            prev = current;
            current = current->sibling;
        }
        
        // Remove min node from list
        if (prevMin) {
            prevMin->sibling = minNode->sibling;
        } else {
            head = minNode->sibling;
        }
        
        // Create heap from min node's children
        BinomialNode* childHeap = reverseList(minNode->child);
        
        // Union with main heap
        head = unionHeaps(head, childHeap);
        
        int minKey = minNode->key;
        delete minNode;
        return minKey;
    }
    
    void print_heap() {
        BinomialNode* current = head;
        while (current) {
            std::cout << "Tree degree " << current->degree << ": " << current->key;
            if (current->sibling) std::cout << " -> ";
            current = current->sibling;
        }
        std::cout << std::endl;
    }
    
    ~BinomialHeap() {
        while (!is_empty()) {
            extract_min();
        }
    }
};

// Тестирование
int main() {
    BinomialHeap heap;
    heap.insert(10);
    heap.insert(5);
    heap.insert(20);
    heap.insert(3);
    heap.insert(8);
    
    std::cout << "Min: " << heap.get_min() << std::endl;  // 3
    std::cout << "Extract min: " << heap.extract_min() << std::endl;  // 3
    std::cout << "New min: " << heap.get_min() << std::endl;  // 5
    
    heap.print_heap();
    return 0;
}
...............................................
2. куча Фибоначи
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

template<typename T>
class FibonacciHeap {
private:
    struct Node {
        T key;
        int degree = 0;
        Node* parent = nullptr;
        Node* child = nullptr;
        Node* left = this;
        Node* right = this;
        bool marked = false;
        
        Node(T k) : key(k) {}
    };
    
    Node* min_node = nullptr;
    int node_count = 0;
    
    void _link(Node* y, Node* x) {
        // Remove y from root list
        y->left->right = y->right;
        y->right->left = y->left;
        
        // Make y a child of x
        y->parent = x;
        if (x->child == nullptr) {
            x->child = y;
            y->right = y;
            y->left = y;
        } else {
            y->left = x->child->left;
            y->right = x->child;
            x->child->left->right = y;
            x->child->left = y;
        }
        
        x->degree++;
        y->marked = false;
    }
    
    void _consolidate() {
        if (!min_node) return;
        
        int max_degree = static_cast<int>(log2(node_count)) + 1;
        std::vector<Node*> degree_table(max_degree + 1, nullptr);
        
        std::vector<Node*> roots;
        Node* current = min_node;
        Node* first = current;
        
        do {
            roots.push_back(current);
            current = current->right;
        } while (current != first);
        
        for (Node* node : roots) {
            int degree = node->degree;
            while (degree_table[degree] != nullptr) {
                Node* other = degree_table[degree];
                if (node->key > other->key) {
                    std::swap(node, other);
                }
                
                _link(other, node);
                degree_table[degree] = nullptr;
                degree++;
            }
            degree_table[degree] = node;
        }
        
        min_node = nullptr;
        for (Node* node : degree_table) {
            if (node) {
                if (!min_node) {
                    min_node = node;
                    node->left = node;
                    node->right = node;
                } else {
                    node->left = min_node->left;
                    node->right = min_node;
                    min_node->left->right = node;
                    min_node->left = node;
                    
                    if (node->key < min_node->key) {
                        min_node = node;
                    }
                }
            }
        }
    }
    
    void _cut(Node* node, Node* parent) {
        if (node->right == node) {
            parent->child = nullptr;
        } else {
            node->left->right = node->right;
            node->right->left = node->left;
            if (parent->child == node) {
                parent->child = node->right;
            }
        }
        
        parent->degree--;
        
        node->left = min_node->left;
        node->right = min_node;
        min_node->left->right = node;
        min_node->left = node;
        
        node->parent = nullptr;
        node->marked = false;
    }
    
    void _cascading_cut(Node* node) {
        Node* parent = node->parent;
        if (parent) {
            if (!node->marked) {
                node->marked = true;
            } else {
                _cut(node, parent);
                _cascading_cut(parent);
            }
        }
    }

public:
    bool is_empty() const { return min_node == nullptr; }
    
    Node* insert(T key) {
        Node* new_node = new Node(key);
        
        if (!min_node) {
            min_node = new_node;
        } else {
            new_node->left = min_node->left;
            new_node->right = min_node;
            min_node->left->right = new_node;
            min_node->left = new_node;
            
            if (key < min_node->key) {
                min_node = new_node;
            }
        }
        
        node_count++;
        return new_node;
    }
    
    T get_min() {
        if (!min_node) throw std::runtime_error("Heap is empty");
        return min_node->key;
    }
    
    T extract_min() {
        if (!min_node) throw std::runtime_error("Heap is empty");
        
        Node* min_node_ptr = min_node;
        T min_key = min_node_ptr->key;
        
        // Add children to root list
        if (min_node_ptr->child) {
            Node* child = min_node_ptr->child;
            Node* first_child = child;
            do {
                Node* next_child = child->right;
                child->left->right = child->right;
                child->right->left = child->left;
                child->left = min_node->left;
                child->right = min_node;
                min_node->left->right = child;
                min_node->left = child;
                child->parent = nullptr;
                child = next_child;
            } while (child != first_child);
        }
        
        // Remove min_node from root list
        min_node_ptr->left->right = min_node_ptr->right;
        min_node_ptr->right->left = min_node_ptr->left;
        
        if (min_node_ptr == min_node_ptr->right) {
            min_node = nullptr;
        } else {
            min_node = min_node_ptr->right;
            _consolidate();
        }
        
        delete min_node_ptr;
        node_count--;
        return min_key;
    }
    
    void decrease_key(Node* node, T new_key) {
        if (new_key > node->key) {
            throw std::invalid_argument("New key must be smaller");
        }
        
        node->key = new_key;
        Node* parent = node->parent;
        
        if (parent && node->key < parent->key) {
            _cut(node, parent);
            _cascading_cut(parent);
        }
        
        if (node->key < min_node->key) {
            min_node = node;
        }
    }
    
    void delete_node(Node* node) {
        decrease_key(node, std::numeric_limits<T>::min());
        extract_min();
    }
    
    ~FibonacciHeap() {
        while (!is_empty()) {
            extract_min();
        }
    }
};

// Тестирование
int main() {
    FibonacciHeap<int> fib_heap;
    auto node1 = fib_heap.insert(10);
    auto node2 = fib_heap.insert(5);
    auto node3 = fib_heap.insert(20);
    auto node4 = fib_heap.insert(3);
    auto node5 = fib_heap.insert(8);
    
    std::cout << "Min: " << fib_heap.get_min() << std::endl;  // 3
    std::cout << "Extract min: " << fib_heap.extract_min() << std::endl;  // 3
    std::cout << "New min: " << fib_heap.get_min() << std::endl;  // 5
    
    fib_heap.decrease_key(node2, 2);
    std::cout << "After decrease key, min: " << fib_heap.get_min() << std::endl;  // 2
    
    return 0;
}
.........................................
3. Хеш-таблица
cpp
#include <iostream>
#include <list>
#include <vector>
#include <functional>

template<typename K, typename V>
class HashMap {
private:
    std::vector<std::list<std::pair<K, V>>> table;
    size_t capacity;
    size_t count;
    
    size_t hash(const K& key) {
        return std::hash<K>{}(key) % capacity;
    }
    
    void resize() {
        capacity *= 2;
        std::vector<std::list<std::pair<K, V>>> newTable(capacity);
        
        for (auto& bucket : table) {
            for (auto& pair : bucket) {
                size_t index = hash(pair.first);
                newTable[index].push_back(pair);
            }
        }
        table = std::move(newTable);
    }

public:
    HashMap(size_t cap = 10) : capacity(cap), count(0) {
        table.resize(capacity);
    }
    
    void put(const K& key, const V& value) {
        if (count >= capacity * 0.7) resize();
        
        size_t index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        table[index].emplace_back(key, value);
        count++;
    }
    
    V get(const K& key) {
        size_t index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        throw std::runtime_error("Key not found");
    }
    
    void remove(const K& key) {
        size_t index = hash(key);
        auto& bucket = table[index];
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->first == key) {
                bucket.erase(it);
                count--;
                return;
            }
        }
        throw std::runtime_error("Key not found");
    }
    
    bool contains(const K& key) {
        size_t index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) return true;
        }
        return false;
    }
    
    size_t size() { return count; }
};

// Тестирование
int main() {
    HashMap<std::string, int> map;
    map.put("apple", 1);
    map.put("banana", 2);
    map.put("cherry", 3);
    
    std::cout << "apple: " << map.get("apple") << std::endl;  // 1
    map.remove("banana");
    std::cout << "Contains banana: " << map.contains("banana") << std::endl;  // 0
    
    return 0;
