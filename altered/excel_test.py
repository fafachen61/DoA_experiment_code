import pandas as pd
import numpy as np
data2 = pd.read_excel('/Users/chenfayu/Documents/@@台灣大學電機系＿三上專題研究/演算法/DoA_experiment_code/ground_truth.xlsx')
x = np.linspace(0, 50, 51)
y = data2.iloc[x, 2]

print(x)
print(y)