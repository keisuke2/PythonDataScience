import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
#csvの読み込み
iris_data = pd.read_csv("iris.csv")
iris_data.head(5)

print("リスト3.7:平均値の計算")
iris_mean = iris_data.mean()
print(iris_mean)
print("リスト3.9:平均値棒グラフの作成")
iris_mean.plot(kind = "bar", rot = 45)
print(iris_mean.plot(kind = "bar", rot = 45))
print("リスト3.10:密度分布図の作成")
iris_data.plot(kind = "kde", subplots = True, figsize = (10,6))
