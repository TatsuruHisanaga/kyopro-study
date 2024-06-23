def solution(S):
    # 二進数の文字列を整数に変換
    V = int(S, 2)
    
    operations = 0
    
    # Vが0になるまで操作を繰り返す
    while V > 0:
        if V % 2 == 0:
            V //= 2  # 偶数の場合、2で割る（右シフト）
        else:
            V -= 1  # 奇数の場合、1を引く
        operations += 1
    
    return operations

# テストケース
print(solution("011100"))  # 7
print(solution("111"))     # 5
print(solution("11110101111"))  # 22
print(solution("1" * 400000))  # 799999
