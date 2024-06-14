import heapq

# 入力
Q = int(input())
queries = [ None ] * Q
for i in range(Q):
  queries[i] = input().split()

# 優先度付きキューを初期化
T = []
for q in queries:
  if q[0] == "1":
    x = int(q[1])
    heapq.heappush(T, x)
  if q[0] == "2":
    print(T[0])
  if q[0] == "3":
    heapq.heappop(T)