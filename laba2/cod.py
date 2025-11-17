python

Мультисписок (вложенный список)
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
Очередь
python
from queue import Queue
q = Queue()
q.put(1)
q.get()  # 1
'------------------'
Дек
from collections import deque
dq = deque()
dq.append(1)
dq.appendleft(0)
dq.pop()
dq.popleft()
'------------'
Приоритетная очередь
import heapq
heap = []
heapq.heappush(heap, (2, "mid"))
heapq.heappush(heap, (1, "high"))
heapq.heappop(heap)  # (1, "high")
