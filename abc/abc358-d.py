import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 払う金額の合計
result = 0

A.sort()

# 1~M番目までの人にお菓子を渡す
for i in range(M):
    # B[i]以上の最小の値のインデックスを見つける
    index = bisect.bisect_left(A, B[i])
    if index < len(A) and A[index] >= B[i]:
        result += A[index]
        A.pop(index)
    else:
        result = -1
        break
print(result)