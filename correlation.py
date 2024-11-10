import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/ziya07/youth-basketball-training/versions/1/youth_basketball_training_dataset.csv')

corre_map = df.corr()
sn.heatmap(corre_map, annot=True)

figure = plt.gcf()
figure.set_size_inches(24, 20)
plt.savefig("data/correlation_map.png", dpi=100)
plt.close()