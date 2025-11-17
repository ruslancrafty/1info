Мультисписок (двусвязный список)
cpp
struct Node {
    int data;
    Node* prev;
    Node* next;
};
'---------------------------'
Очередь
cpp
#include <queue>
std::queue<int> q;
q.push(1);
q.front(); 
q.pop();
'-----------------------'
Дек
cpp
#include <deque>
std::deque<int> dq;
dq.push_back(1);
dq.push_front(0);
dq.pop_back();
dq.pop_front();
'-------------------------'
Приоритетная очередь
cpp
#include <queue>
std::priority_queue<int> pq;
pq.push(10);
pq.push(5);
pq.top(); // 10
pq.pop();
