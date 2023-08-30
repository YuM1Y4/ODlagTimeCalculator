import numpy as np

import pandas as pd


def largest_slope(Xs, Ys):
    if len(Xs) != len(Ys):
        raise ValueError("The number of Xs and Ys must be equal.")

    n = len(Xs)
    max_slope = float('-inf')

    for i in range(n - 28):
        x1, y1 = Xs[i], Ys[i]
        x2, y2 = Xs[i + 28], Ys[i + 28]

        slope = (y2 - y1) / (x2 - x1)
        max_slope = max(max_slope, slope)

    return max_slope


if __name__ == "__main__":
    data = pd.read_csv("ddd.csv")
    # Example input data (replace with your actual data)
    # Xs = data[["Time/h"]]
    Xs = data["Time/h"].values.tolist()
    x = input()
    while type(x) != "int":
        Ys = data["%s"%(x)].values.tolist()
        largest_slope_val = largest_slope(Xs, Ys)

        print("The largest slope on the curve is:", largest_slope_val)
        x = input()