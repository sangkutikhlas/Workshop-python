#array
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
# 26932
a[1:3]
# array('H', [10, 700])

#collections
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
#Handling task1

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

#bisect
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores
# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

#heapq
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # atur ulang daftar menjadi urutan tumpukan
heappush(data, -5)                 # tambahkan entri baru
[heappop(data) for i in range(3)]  # ambil tiga entri terkecil
[-5, 0, 1]