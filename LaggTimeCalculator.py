import numpy as np
import pandas as pd
import math


def MaxSlope_Coeff(List_X,List_Y):
    if len(List_X) != len(List_Y):
        raise ValueError("The number of Xs and Ys must be equal.")

    n = len(List_X)
    max_slope = float('-inf')
    max_x = float('-inf')
    max_y = float('-inf')
    for i in range(n - 28):
        x1, y1 = List_X[i], List_Y[i]
        x2, y2 = List_X[i + 28], List_Y[i + 28]

        slope = (y2 - y1) / (x2 - x1)

        if slope > max_slope:
            max_slope = slope
            max_x = x1
            max_y = y1
    y_intercept = max_y - max_slope * max_x
    print("maxslope",max_slope,y_intercept)
    return (max_slope, y_intercept)

def Minslope_Coeff(Xs,Ys):
    if len(Xs) != len(Ys):
        raise ValueError("The number of Xs and Ys must be equal.")

    n = len(Xs)
    min_slope = float('inf')
    min_x = float('inf')
    min_y = float('inf')
    for i in range(int(n/2)):
        x1, y1 = Xs[i], Ys[i]
        x2, y2 = Xs[i + 5], Ys[i + 5]

        slope = (y2 - y1) / (x2 - x1)

        if slope < min_slope and slope >= 0:
            min_slope = slope
            min_x = x1
            min_y = y1
    y_intercept = min_y - min_slope * min_x
    print("minslope",min_slope,y_intercept)
    return (min_slope, y_intercept)

def calculate_intersection(Xs,Ys):
    m1, b1 = MaxSlope_Coeff(Xs,Ys)
    m2, b2 = Minslope_Coeff(Xs,Ys)

    if m1 == m2:
        raise ValueError("Lines are parallel and do not intersect.")

    x_intersect = (b2 - b1) / (m1 - m2)
    y_intersect = m1 * x_intersect + b1

    return x_intersect, y_intersect

def ReadCSV(File_path,Name):
    data = pd.read_csv(File_path)

    Time_10min = data["Time/10min"].values.tolist()
    TimePerHour = [x * 1/6 for x in Time_10min]

    OD = data["%s" % (Name)].values.tolist()
    LogOD = [math.log2(x) for x in OD]

    return Time_10min, OD


if __name__ == "__main__":
    File_path = "ddd.csv"

    x = input()

    while type(x) != "int":
        Xs,Ys = ReadCSV(File_path,x)
        Result_Time, result_y = calculate_intersection(Xs,Ys)

        print(Result_Time,result_y)
        x = input()
