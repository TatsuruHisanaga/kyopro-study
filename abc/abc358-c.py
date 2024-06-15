N, M = map(int, input().split())

S = [ None ] * N

for i in range(N):
  S[i] = str(input())

# S_i はN個の長さMの文字列
# S_iのj文字目がoならば、売り場iが味jのポップコーンを売っている、xならば売っていない
# 全ての味のポップコーンを買うための最小の買い物回数を求める
import itertools

# 1からNまでの売り場について、各売り場で売っているポップコーンの種類を数える
for r in range(1, N+1):
  for combo in itertools.combinations(S, r):
    taste = set()
    for stall in combo:
      for j in range(M):
        if stall[j] == "o":
          taste.add(j)
    # r番目まで探して見つけた味の数が全ての味の数Mと同じ時、その時のrが答え
    if len(taste) == M:
      print(r)
      exit()