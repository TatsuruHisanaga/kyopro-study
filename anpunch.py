def main(n, words):
    # 語尾（語頭）をキーとし、その語尾（語頭）を持つ単語のリストを値とする
    # 辞書の作成
    suffix_dict = {}
    prefix_dict = {}

    for word in words:
        if len(word) > 2:
            suffix = word[-2:]
            prefix = word[:2]
            
            if suffix not in suffix_dict:
                suffix_dict[suffix] = []
            suffix_dict[suffix].append(word)
            
            if prefix not in prefix_dict:
                prefix_dict[prefix] = []
            prefix_dict[prefix].append(word)
    
    # 求める値の初期化
    max_length = -1

    # それぞれの語尾について、一致する語頭を持つ単語の探索
    for suffix, suffix_words in suffix_dict.items():
        # 現在の語尾と同じ語頭があるか調べる
        if suffix in prefix_dict:
            # 語尾suffixを持つすべての単語について反復処理
            for word_s in suffix_words:
                # suffixと同じ語頭を持つ単語について反復処理
                for word_p in prefix_dict[suffix]:
                    if word_s != word_p:
                        # 造語の長さを計算
                        combined_length = len(word_s) + len(word_p) - 2
                        # max_lengthを更新
                        max_length = max(max_length, combined_length)
    
    return max_length


# 入力
n = int(input())
words = [input().strip() for _ in range(n)]

# 最も長い造語の長さを求める
max_length = main(n, words)

# 結果の出力
print(max_length)

