import ast

def solution(intervals):
    # intervalsを昇順にソート
    intervals.sort()

    merged_intervals = []
    current_interval = intervals[0]

    for i in range(1, len(intervals)): 
        # 現在の間隔の後ろの要素と次の間隔の最初の要素を比較
        if current_interval[1] >= intervals[i][0]:
            # 重複している場合はマージする
            current_interval[1] = max(current_interval[1],intervals[i][1])
            merged_intervals.append(current_interval)
            current_interval = intervals[i]
        
    merged_intervals.append(current_interval)

    return merged_intervals

intervals = ast.literal_eval(input().strip())
result = solution(intervals)
print(result)
