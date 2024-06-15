N, A = map(int, input().split())  

T = list(map(int, input().split()))


end_times = [0] * N

# 1番目の人
end_times[0] = T[0] + A

# ２番目以降の人
for i in range(1, N):
    # 前の人がチケット購入を終了した時刻と、今来た人がチケット売り場に到着する時刻を比較し、大きい方を開始時刻とする
    start_time = max(end_times[i-1], T[i])
    end_times[i] = start_time + A

for end_time in end_times:
    print(end_time)
        