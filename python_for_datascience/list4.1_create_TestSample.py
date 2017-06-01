import scipy.stats as st
import numpy as np
#scipy.stats:統計分析を行うscipyのモジュール
print("scipyで40人分のテストデータを作成する")

#期待値
expected_value = 160
#標準偏差
standard_deviation = 10
#生成するサンプル数
create_sample = 40
print("期待値が160、標準偏差が10の正規分布の乱数生成器を40個生成する")
n,m,s = create_sample , expected_value, standard_deviation
rg = st.norm(m, s)
data = rg.rvs(n)
print(data)



print("Numpyで40人分のテストデータを生成する")
n,m,s = create_sample , expected_value, standard_deviation
data = np.random.randn(n) * s + m
print(data)