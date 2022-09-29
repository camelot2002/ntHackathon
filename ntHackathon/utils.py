import numpy as np
import pandas as pd
import pandas as pd
import glob
import os


def fill_missing(dataset):

    nations = dataset.columns[:]
    for nation in nations:
        dataset[nation].ffill(inplace=True)
        dataset[nation].bfill(inplace=True)
    dataset.to_csv('dataset.csv')


def preprocessing():

    dataset = os.path.join("Exchange*.csv")
    dataset = glob.glob(dataset)
    df = pd.concat(map(pd.read_csv, dataset), ignore_index=True)
    df = df.rename(columns=lambda x: x.rstrip().replace(" ", "_"))
    df = df.set_index('Date')
    df.to_csv('dataset.csv')
    fill_missing(df)


if __name__ == "__main__":
    dataset = pd.read_csv('dataset.csv')
    fill_missing(dataset)
