
# 入力
Q = int(input())
queries = [ None ] * Q
for i in range(Q):
  queries[i] = input().split()

# キューを初期化
queue = []

# クエリの処理
for query in queries:
  command = query[0]
  if command == "1":
    queue.append(query[1])
  elif command == "2":
    if queue:
      print(queue[0])
  elif command == "3":
    if queue:
      x = queue.pop(0)
      # print(x + "を取り出しました")
      # print("現在のキュー： " + str(queue))


