import math

def get_received_amount(D, Y, I):
  # I を%を使わずに表現
  I /= 100

  # 単利、複利の計算
  if Y < 3:
    simple_interest = math.floor(D * I * ( Y * 365 / 365 ))
    D += simple_interest
    return D
  else:
    for _ in range(Y):
      # 初めの半年間の利息と預入金額を計算
      interest = math.floor(D * I * 182 / 365 )
      D += interest
      # 残りの半年間の利息と預入金額を計算
      interest = math.floor(D * I *  183 / 365 )
      D += interest
    return D

# 入力
D, Y, I = input().split()

print(get_received_amount(int(D), int(Y), float(I)))