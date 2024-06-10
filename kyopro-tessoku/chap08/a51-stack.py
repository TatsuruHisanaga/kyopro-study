# 入力
Q = int(input())
queries = [None] * Q
for i in range(Q):
    queries[i] = input().split()

# クエリの処理
S = []
for q in queries:
    if q[0] == "1":
        S.append(q[1])
    elif q[0] == "2":
        print(S[-1])
    elif q[0] == "3":
        S.pop()
