# 入力
N , M = map(int, input().split())
edges = [ list(map(int, input().split())) for _ in range(M)]

# 隣接リストの作成
adjacent_vertices = [ list() for _ in range(N+1)]
for a, b in edges:
  adjacent_vertices[a].append(b)
  adjacent_vertices[b].append(a)

# 出力
for i in range(1, N+1):
  output = ''
  output += str(i) 
  output += ': {'
  output += ', '.join(map(str, adjacent_vertices[i]))
  output += '}'
  print(output)