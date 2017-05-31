print("Pythonの標準機能でcsvを読み込む")
fp = open("iris.csv", "r")
print("csvファイル出力")
next(fp) #1行読み飛ばす
iris_data = []
for line in fp:
    record = line.strip().split(",") #","で分解する
    iris_data.append(record)
iris_data[:5]
print(iris_data);
