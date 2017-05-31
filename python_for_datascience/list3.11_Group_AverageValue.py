import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
#csvの読み込み
iris_data = pd.read_csv("iris.csv")
iris_data.head(5)

print("リスト3.11:グループ毎の平均値の計算")
grouped_data = iris_data.groupby("Species")
group_mean = grouped_data.mean()
group_mean
print("リスト3.12:グループごとの平均値を棒グラフに")
print("legend関数を使用して凡例(ラベル)を図の上部に表示する")
group_mean.plot(kind = "bar")
plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 1.2), ncol=2)
plt.show()
print("リスト3.14:転置した平均値の棒グラフを作成")
group_mean.T.plot(kind = "bar", rot=0)
plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 1.1), ncol = 3)
plt.show()