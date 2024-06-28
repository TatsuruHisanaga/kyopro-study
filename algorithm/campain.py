# 入力
n, m = map(int, input().split())
d, y = map(int, input().split())

# 平日の場合
if d >= 1 and d <= 5:
  # 入園者が子供か大人かによる場合分け
  if y < 18:
    # 子供の場合、入場料金は500円引き
    result = m - 500
  else:
    # 大人の場合、入場料金はそのまま
    result = n
# 休日の場合
elif d >= 6 and d <= 7:
  # 入園者が子供か大人かによる場合分け
  if y < 18:
    # 子供の場合、入場料金はそのまま
    result = m
  else:
    # 大人の場合、入場料金は1000円引き
    result = n - 1000

print(result)