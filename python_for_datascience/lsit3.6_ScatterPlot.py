import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
#csvの読み込み
iris_data = pd.read_csv("iris.csv")
iris_data.head(5)
print(iris_data)
print("リスト3.6:花の種類別にマーカーシンボルを変えて散布図作成")
for name, symbol in zip(("setosa", "versicolor", "virginica"),("o", "s", "*")):
	data = iris_data[iris_data["Species"] == name]
	plt.plot(iris_data["Petal Length"], iris_data["Petal Width"], symbol, label = name)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend(loc=0)
plt.show()