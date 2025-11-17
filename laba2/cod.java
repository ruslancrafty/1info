Мультисписок (двусвязный список)
class Node {
    int data;
    Node prev, next;
    Node(int data) { this.data = data; }
}
'---------------------'
Очередь
import java.util.*;
Queue<Integer> q = new LinkedList<>();
q.add(1);
q.poll(); 
'------------------------'
Дек
Deque<Integer> dq = new ArrayDeque<>();
dq.addLast(1);
dq.addFirst(0);
dq.pollLast();
dq.pollFirst();
'----------------------'
Приоритетная очередь
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(10);
pq.offer(5);
pq.poll(); 
