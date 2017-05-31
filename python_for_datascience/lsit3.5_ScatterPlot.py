import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
#csvの読み込み
iris_data = pd.read_csv("iris.csv")
iris_data.head(5)
print(iris_data)
print("リスト3.5:散布図作成")
plt.plot(iris_data["Petal Length"], iris_data["Petal Width"], "o")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()