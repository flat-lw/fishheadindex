import csv
import json

# CSV ファイル名の指定
csv_filename = "fishList.csv"
json_filename = "fishList.json"

data = {"fishhead": {}}

# CSV ファイルの読み込み
with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # ヘッダー取得

    for row in reader:
        number = row[0]  # "number" は 1列目にあると仮定
        data["fishhead"][number] = {
            "name": row[1],
            "day": row[3],  # 空のカラム (index=2) をスキップ
            "auther": row[4],
            "comment": row[5],
            "model": row[6],
            "ID": row[7],
            "performance": row[9]  # "IRL" (index=8) をスキップ
        }

# JSON ファイルに保存
with open(json_filename, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"JSON を {json_filename} に保存しました")

