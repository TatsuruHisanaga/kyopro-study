import sys
import csv
from collections import defaultdict

# データを格納する辞書の初期化
sales_data = defaultdict(lambda: defaultdict(int))
prefecture_totals = defaultdict(int)
national_total = 0

# 入力
input_data = sys.stdin.read().strip().split('\n')
reader = csv.reader(input_data)

for row in reader:
    if len(row) == 3:
        prefecture, store, sales = row
        sales = int(sales)
        sales_data[prefecture][store] += sales
        prefecture_totals[prefecture] += sales
        national_total += sales

def format_result(prefecture, store_data):
    result = [f"* {prefecture}"]
    for store, sales in store_data.items():
        result.append(f"{store} {sales}")
    result.append(f"{prefecture}合計 {prefecture_totals[prefecture]}")
    return "\n".join(result)

# 各都道府県の出力の生成
result_lines = []
for prefecture in sales_data.keys():
    result_lines.append(format_result(prefecture, sales_data[prefecture]))

# 全国合計値の出力への追加
result_lines.append(f"全国合計 {national_total}")

print("\n".join(result_lines))
