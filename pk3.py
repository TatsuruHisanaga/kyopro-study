def solution(blocks):
    N = len(blocks)

    # 各ブロックから右方向にどこまで到達できるかを保持する配列
    right = [0] * N
    for i in range(1, N):
        if blocks[i] >= blocks[i - 1]:
            right[i] = right[i - 1] + 1
        else:
            right[i] = 0

    # 各ブロックから左方向にどこまで到達できるかを保持する配列
    left = [0] * N
    for i in range(N - 2, -1, -1):
        if blocks[i] >= blocks[i + 1]:
            left[i] = left[i + 1] + 1
        else:
            left[i] = 0

    # 可能な最大距離を計算
    max_distance = 0
    for i in range(N):
        max_distance = max(max_distance, right[i] + left[i] + 1)

    return max_distance

# テストケース
print(solution([2, 6, 8, 5]))  # 3
print(solution([1, 5, 5, 2, 6]))  # 4
print(solution([1, 1]))  # 2
print(solution([4, 4, 2]))  # 2

