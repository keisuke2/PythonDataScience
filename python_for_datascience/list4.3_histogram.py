#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

#期待値
expected_value = 160
#標準偏差
standard_deviation = 10
#生成するサンプル数
create_sample = 40
print("Numpyで40人分のテストデータを生成する")
n,m,s = create_sample , expected_value, standard_deviation
data = np.random.randn(n) * s + m
print(data)
print("ヒストグラムを描画する")
#bin: データをいくつに分けて数え上げたいか
divide_histgram_count = 10
c, x, _ = plt.hist(data, divide_histgram_count)
print("リスト4.4:結果を表示")
#cは各binのサンプル数
print(c)
#xは各binの値がどこから始まり、どこで終わるかを記載
print(x)
plt.show()
