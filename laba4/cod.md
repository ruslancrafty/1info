АЛЬТЕРНАТИВНЫЕ ПРЕДСТАВЛЕНИЯ ДЕРЕВЬЕВ
1. Универсальное дерево с произвольным количеством потомков
Python
python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # Список всех дочерних узлов
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]
    
    def traverse(self):
        """Обход дерева в глубину"""
        nodes = [self]
        while nodes:
            current = nodes.pop()
            print(current.value, end=' ')
            nodes.extend(reversed(current.children))
    
    def find(self, value):
        """Поиск узла по значению"""
        if self.value == value:
            return self
        for child in self.children:
            found = child.find(value)
            if found:
                return found
        return None

# Пример использования - организация компании
class OrganizationTree:
    def __init__(self):
        self.root = None
    
    def build_company_structure(self):
        ceo = TreeNode("CEO")
        
        cto = TreeNode("CTO")
        cfo = TreeNode("CFO")
        cmo = TreeNode("CMO")
        
        dev_lead = TreeNode("Lead Developer")
        qa_lead = TreeNode("QA Lead")
        accountant = TreeNode("Senior Accountant")
        marketer = TreeNode("Digital Marketer")
        
        dev1 = TreeNode("Developer 1")
        dev2 = TreeNode("Developer 2")
        tester = TreeNode("Tester")
        
        # Построение иерархии
        cto.add_child(dev_lead)
        cto.add_child(qa_lead)
        dev_lead.add_child(dev1)
        dev_lead.add_child(dev2)
        qa_lead.add_child(tester)
        
        cfo.add_child(accountant)
        cmo.add_child(marketer)
        
        ceo.add_child(cto)
        ceo.add_child(cfo)
        ceo.add_child(cmo)
        
        self.root = ceo
        return ceo

# Использование
org = OrganizationTree()
ceo = org.build_company_structure()
print("Структура компании:")
ceo.traverse()  # CEO CTO CFO CMO Lead Developer QA Lead Senior Accountant...

found = ceo.find("Lead Developer")
print(f"\nНайден: {found.value}" if found else "Не найден")
C++
cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class GenericTreeNode {
public:
    std::string value;
    std::vector<GenericTreeNode*> children;
    
    GenericTreeNode(const std::string& val) : value(val) {}
    
    void addChild(GenericTreeNode* child) {
        children.push_back(child);
    }
    
    void removeChild(GenericTreeNode* child) {
        children.erase(std::remove(children.begin(), children.end(), child), children.end());
    }
    
    void traverse() {
        std::cout << value << " ";
        for (auto child : children) {
            child->traverse();
        }
    }
    
    GenericTreeNode* find(const std::string& target) {
        if (value == target) {
            return this;
        }
        for (auto child : children) {
            GenericTreeNode* found = child->find(target);
            if (found != nullptr) {
                return found;
            }
        }
        return nullptr;
    }
};

// Пример - файловая система
class FileSystemTree {
public:
    GenericTreeNode* root;
    
    FileSystemTree() : root(new GenericTreeNode("/")) {}
    
    ~FileSystemTree() {
        clearTree(root);
    }
    
    void buildSampleFS() {
        GenericTreeNode* home = new GenericTreeNode("home");
        GenericTreeNode* user1 = new GenericTreeNode("user1");
        GenericTreeNode* user2 = new GenericTreeNode("user2");
        
        GenericTreeNode* docs = new GenericTreeNode("documents");
        GenericTreeNode* pics = new GenericTreeNode("pictures");
        GenericTreeNode* file1 = new GenericTreeNode("resume.txt");
        GenericTreeNode* file2 = new GenericTreeNode("photo.jpg");
        
        user1->addChild(docs);
        user1->addChild(pics);
        docs->addChild(file1);
        pics->addChild(file2);
        
        home->addChild(user1);
        home->addChild(user2);
        
        root->addChild(home);
        root->addChild(new GenericTreeNode("etc"));
        root->addChild(new GenericTreeNode("var"));
    }
    
private:
    void clearTree(GenericTreeNode* node) {
        if (node == nullptr) return;
        for (auto child : node->children) {
            clearTree(child);
        }
        delete node;
    }
};

int main() {
    FileSystemTree fs;
    fs.buildSampleFS();
    
    std::cout << "Файловая система: ";
    fs.root->traverse();
    std::cout << std::endl;
    
    auto found = fs.root->find("photo.jpg");
    if (found) {
        std::cout << "Найден файл: " << found->value << std::endl;
    }
    
    return 0;
}
Java
java
import java.util.*;

class GenericTreeNode<T> {
    T data;
    List<GenericTreeNode<T>> children;
    
    public GenericTreeNode(T data) {
        this.data = data;
        this.children = new ArrayList<>();
    }
    
    public void addChild(GenericTreeNode<T> child) {
        children.add(child);
    }
    
    public void removeChild(GenericTreeNode<T> child) {
        children.remove(child);
    }
    
    public void traverse() {
        System.out.print(data + " ");
        for (GenericTreeNode<T> child : children) {
            child.traverse();
        }
    }
    
    public GenericTreeNode<T> find(T target) {
        if (data.equals(target)) {
            return this;
        }
        for (GenericTreeNode<T> child : children) {
            GenericTreeNode<T> found = child.find(target);
            if (found != null) {
                return found;
            }
        }
        return null;
    }
}

// Пример - семейное дерево
class FamilyTree {
    GenericTreeNode<String> root;
    
    public FamilyTree(String ancestorName) {
        this.root = new GenericTreeNode<>(ancestorName);
    }
    
    public void buildSampleFamily() {
        GenericTreeNode<String> child1 = new GenericTreeNode<>("Child1");
        GenericTreeNode<String> child2 = new GenericTreeNode<>("Child2");
        
        GenericTreeNode<String> grandchild1 = new GenericTreeNode<>("Grandchild1");
        GenericTreeNode<String> grandchild2 = new GenericTreeNode<>("Grandchild2");
        GenericTreeNode<String> grandchild3 = new GenericTreeNode<>("Grandchild3");
        
        child1.addChild(grandchild1);
        child1.addChild(grandchild2);
        child2.addChild(grandchild3);
        
        root.addChild(child1);
        root.addChild(child2);
    }
    
    public void displayFamily() {
        System.out.print("Семейное дерево: ");
        root.traverse();
        System.out.println();
    }
}

// Использование
class Main {
    public static void main(String[] args) {
        FamilyTree family = new FamilyTree("Предок");
        family.buildSampleFamily();
        family.displayFamily();
        
        GenericTreeNode<String> found = family.root.find("Grandchild2");
        if (found != null) {
            System.out.println("Найден член семьи: " + found.data);
        }
    }
}
🕸️ АЛЬТЕРНАТИВНЫЕ ПРЕДСТАВЛЕНИЯ ГРАФОВ
2. Граф с использованием классов Vertex и Edge
Python
python
class Vertex:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.edges = []
    
    def add_edge(self, to_vertex, weight=1, directed=False):
        edge = Edge(self, to_vertex, weight)
        self.edges.append(edge)
        if not directed:
            to_vertex.add_edge(self, weight, directed=True)
    
    def __str__(self):
        return f"Vertex({self.id})"

class Edge:
    def __init__(self, from_vertex, to_vertex, weight=1):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    def __str__(self):
        return f"{self.from_vertex.id} -> {self.to_vertex.id} ({self.weight})"

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed
    
    def add_vertex(self, vertex_id, data=None):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id, data)
        return self.vertices[vertex_id]
    
    def add_edge(self, from_id, to_id, weight=1):
        from_vertex = self.add_vertex(from_id)
        to_vertex = self.add_vertex(to_id)
        from_vertex.add_edge(to_vertex, weight, self.directed)
    
    def dijkstra(self, start_id):
        """Алгоритм Дейкстры с использованием нашей структуры"""
        import heapq
        
        distances = {vertex_id: float('infinity') for vertex_id in self.vertices}
        distances[start_id] = 0
        pq = [(0, start_id)]
        
        while pq:
            current_distance, current_id = heapq.heappop(pq)
            current_vertex = self.vertices[current_id]
            
            if current_distance > distances[current_id]:
                continue
                
            for edge in current_vertex.edges:
                neighbor_id = edge.to_vertex.id
                distance = current_distance + edge.weight
                
                if distance < distances[neighbor_id]:
                    distances[neighbor_id] = distance
                    heapq.heappush(pq, (distance, neighbor_id))
        
        return distances

# Пример - транспортная сеть городов
class TransportNetwork:
    def __init__(self):
        self.graph = Graph()
    
    def build_network(self):
        # Добавляем города
        cities = ["Moscow", "SPb", "Kazan", "NNovgorod", "Voronezh"]
        
        # Добавляем дороги с расстояниями
        routes = [
            ("Moscow", "SPb", 700),
            ("Moscow", "Kazan", 800),
            ("Moscow", "Voronezh", 500),
            ("SPb", "NNovgorod", 400),
            ("Kazan", "NNovgorod", 350),
            ("NNovgorod", "Voronezh", 600)
        ]
        
        for from_city, to_city, distance in routes:
            self.graph.add_edge(from_city, to_city, distance)
    
    def find_shortest_routes(self, from_city):
        return self.graph.dijkstra(from_city)

# Использование
network = TransportNetwork()
network.build_network()
routes = network.find_shortest_routes("Moscow")
print("Кратчайшие расстояния из Москвы:")
for city, distance in routes.items():
    print(f"  {city}: {distance} км")
C++
cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <queue>
#include <limits>

class Vertex {
public:
    std::string id;
    std::string data;
    std::vector<class Edge*> edges;
    
    Vertex(const std::string& id, const std::string& data = "") 
        : id(id), data(data) {}
};

class Edge {
public:
    Vertex* from;
    Vertex* to;
    int weight;
    
    Edge(Vertex* from, Vertex* to, int weight = 1)
        : from(from), to(to), weight(weight) {}
};

class ObjectGraph {
private:
    std::unordered_map<std::string, Vertex*> vertices;
    bool directed;
    
public:
    ObjectGraph(bool directed = false) : directed(directed) {}
    
    ~ObjectGraph() {
        for (auto& pair : vertices) {
            delete pair.second;
        }
    }
    
    Vertex* addVertex(const std::string& id, const std::string& data = "") {
        if (vertices.find(id) == vertices.end()) {
            vertices[id] = new Vertex(id, data);
        }
        return vertices[id];
    }
    
    void addEdge(const std::string& fromId, const std::string& toId, int weight = 1) {
        Vertex* from = addVertex(fromId);
        Vertex* to = addVertex(toId);
        
        from->edges.push_back(new Edge(from, to, weight));
        if (!directed) {
            to->edges.push_back(new Edge(to, from, weight));
        }
    }
    
    void printGraph() {
        for (const auto& pair : vertices) {
            Vertex* vertex = pair.second;
            std::cout << vertex->id << " -> ";
            for (Edge* edge : vertex->edges) {
                std::cout << edge->to->id << "(" << edge->weight << ") ";
            }
            std::cout << std::endl;
        }
    }
};

// Пример - социальная сеть
class SocialNetwork {
private:
    ObjectGraph graph;
    
public:
    void buildNetwork() {
        // Добавляем пользователей
        std::vector<std::string> users = {"Alice", "Bob", "Charlie", "Diana", "Eve"};
        
        // Добавляем дружеские связи (вес = сила связи)
        graph.addEdge("Alice", "Bob", 5);
        graph.addEdge("Alice", "Charlie", 3);
        graph.addEdge("Bob", "Diana", 4);
        graph.addEdge("Charlie", "Diana", 2);
        graph.addEdge("Diana", "Eve", 6);
    }
    
    void displayNetwork() {
        std::cout << "Социальная сеть:" << std::endl;
        graph.printGraph();
    }
};

int main() {
    SocialNetwork sn;
    sn.buildNetwork();
    sn.displayNetwork();
    return 0;
}
Java
java
import java.util.*;

class Vertex<T> {
    T id;
    String data;
    List<Edge<T>> edges;
    
    public Vertex(T id, String data) {
        this.id = id;
        this.data = data;
        this.edges = new ArrayList<>();
    }
    
    public void addEdge(Vertex<T> to, int weight) {
        this.edges.add(new Edge<>(this, to, weight));
    }
    
    @Override
    public String toString() {
        return "Vertex{" + id + "}";
    }
}

class Edge<T> {
    Vertex<T> from;
    Vertex<T> to;
    int weight;
    
    public Edge(Vertex<T> from, Vertex<T> to, int weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }
    
    @Override
    public String toString() {
        return from.id + " -> " + to.id + " (" + weight + ")";
    }
}

class ObjectGraph<T> {
    private Map<T, Vertex<T>> vertices;
    private boolean directed;
    
    public ObjectGraph(boolean directed) {
        this.vertices = new HashMap<>();
        this.directed = directed;
    }
    
    public void addVertex(T id, String data) {
        vertices.putIfAbsent(id, new Vertex<>(id, data));
    }
    
    public void addEdge(T fromId, T toId, int weight) {
        Vertex<T> from = vertices.computeIfAbsent(fromId, id -> new Vertex<>(id, ""));
        Vertex<T> to = vertices.computeIfAbsent(toId, id -> new Vertex<>(id, ""));
        
        from.addEdge(to, weight);
        if (!directed) {
            to.addEdge(from, weight);
        }
    }
    
    public void printGraph() {
        for (Vertex<T> vertex : vertices.values()) {
            System.out.print(vertex.id + " -> ");
            for (Edge<T> edge : vertex.edges) {
                System.out.print(edge.to.id + "(" + edge.weight + ") ");
            }
            System.out.println();
        }
    }
}

// Пример - сеть знаний
class KnowledgeGraph {
    private ObjectGraph<String> graph;
    
    public KnowledgeGraph() {
        this.graph = new ObjectGraph<>(true); // Ориентированный граф
    }
    
    public void buildKnowledgeBase() {
        // Концепции и связи между ними
        graph.addEdge("AI", "Machine Learning", 8);
        graph.addEdge("AI", "Natural Language Processing", 7);
        graph.addEdge("Machine Learning", "Deep Learning", 9);
        graph.addEdge("Machine Learning", "Neural Networks", 9);
        graph.addEdge("Deep Learning", "CNN", 8);
        graph.addEdge("Deep Learning", "RNN", 8);
    }
    
    public void displayKnowledge() {
        System.out.println("Сеть знаний:");
        graph.printGraph();
    }
}

class Main {
    public static void main(String[] args) {
        KnowledgeGraph kg = new KnowledgeGraph();
        kg.buildKnowledgeBase();
        kg.displayKnowledge();
    }
