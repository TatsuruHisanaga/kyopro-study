import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 払う金額の合計
result = 0

# Aをヒープに変換する
heapq.heapify(A)

# Bをソートしておく
B.sort()

# 1~M番目までの人にお菓子を渡す
for i in range(M):
    while A and A[0] < B[i]:
        heapq.heappop(A)
    if A and A[0] >= B[i]:
        result += heapq.heappop(A)
    else:
        result = -1
        break

print(result)
