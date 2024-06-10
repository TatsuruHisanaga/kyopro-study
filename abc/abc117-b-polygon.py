# https://atcoder.jp/contests/abc117/tasks/abc117_b

# 入力
N = int(input())
L = list(map(int, input().split()))

# 最も長い辺の長さ
max_len = max(L)
# max_len が他の辺の合計よりも短い場合、三角形は作れない
if max_len < sum(L) - max_len:
  print("Yes")
else:
  print("No")
