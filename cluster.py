from sklearn import cluster
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/rileythompson/.cache/kagglehub/datasets/ziya07/youth-basketball-training/versions/1/youth_basketball_training_dataset.csv')

def make_scatter(first_column, second_column):
    data = df[[first_column, second_column]]
    data.plot.scatter(x=first_column,y=second_column)
    figure = plt.gcf()
    figure.set_size_inches(24, 20)
    plt.savefig("data/scatter.png", dpi=100)
    plt.close()


if __name__ == "__main__":
    print(df.columns)
    first_column = input("Enter the first column you want: ")
    second_column = input("Enter the second column you want: ")
    make_scatter(first_column, second_column)