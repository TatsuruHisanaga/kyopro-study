# クエリの数を入力として受け取る
Q = int(input())

# 各クエリを保存するためのリストを初期化
queries = [None] * Q

# 各クエリを入力として受け取り、リストに保存
for i in range(Q):
    queries[i] = input().split()

# スタックを初期化
stack = []

# クエリの処理
for query in queries:
    command = query[0]

    if command == "1":
        book_title = query[1]
        stack.append(book_title)
    elif command == "2":
        print(stack[-1])
    elif command == "3":
        stack.pop()

