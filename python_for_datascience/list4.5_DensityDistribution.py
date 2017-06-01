import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
print("リスト4.5:密度分布のテストデータを作成する")

rg1 = st.norm(165, 10)
rg2 = st.norm(160, 12)
data1 = rg1.rvs(40)
data2 = rg2.rvs(70)
print("リスト4.6:2つのヒストグラムを生成する")
fig, axes = plt.subplots(nrows = 2)
axes[0].hist(data1)
axes[1].hist(data2)
print("2つでは開始位置、終了位置とデータ数が異なるので、このままでは単純に比較できない")
#plt.show()
print("リスト4.7:位置を固定する")
axes[0].hist(data1, range(140, 180), normed = True)
axes[1].hist(data2, range(140, 180), normed = True)
print("binの数を変えると見え方が変わってしまう")
#plt.show()
print("リスト4.8:ヒストグラムと密度分布を重ねてみる")
#密度のモデルを構築する
kde1 = st.gaussian_kde(data1)
kde2 = st.gaussian_kde(data2)
#140~180の区間を100等分した配列を生成
plot_x = np.linspace(140, 180, 100)
#密度を計算
density1 = kde1(plot_x)
density2 = kde2(plot_x)
fig, axes = plt.subplots(nrows = 2)
axes[0].hist(data1, range(130, 200), normed = True)
axes[0].plot(plot_x, density1)
axes[1].hist(data1, range(130, 200), normed = True)
axes[1].plot(plot_x, density2)
print("密度分布を重ねてみる")
plt.fill(plot_x, density2, alpha = 0.5, label = "class1")
plt.fill(plot_x, density2, alpha = 0.5, label = "class2")
plt.legend()
plt.show()
