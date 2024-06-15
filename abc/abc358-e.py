K = int(input())
C = list(map(int, input().split()))

MOD = 998244353  # 定数MODを設定

# DPテーブルを初期化
dp = [[0] * (K + 1) for _ in range(27)]
dp[0][0] = 1  # 初期条件

for i in range(26):
    for j in range(K + 1):
        if dp[i][j] != 0:
            for k in range(C[i] + 1):
                if j + k <= K:
                    dp[i + 1][j + k] = (dp[i + 1][j + k] + dp[i][j]) % MOD

result = dp[26][K]
print(result)

