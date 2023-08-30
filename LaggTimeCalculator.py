import numpy as np
import pandas as pd
import math
import csv

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
    # print("maxslope",max_slope,y_intercept)
    return max_slope, y_intercept

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
    # print("minslope",min_slope,y_intercept)
    return min_slope, y_intercept


def calculate_intersection(Xs,Ys):
    m1, b1 = MaxSlope_Coeff(Xs,Ys)
    m2, b2 = Minslope_Coeff(Xs,Ys)

    if m1 == m2:
        raise ValueError("Lines are parallel and do not intersect.")

    x_intersect = (b2 - b1) / (m1 - m2)
    # y_intersect = m1 * x_intersect + b1

    return x_intersect, m1


def ReadCSV(File_path):
    data = pd.read_csv(File_path)

    Time_min = data["Time/min"].values.tolist()
    TimePerHour = [x * 1 / 60 for x in Time_min]

    log_od = []
    Names = []

    for Name in list(data)[2:26]:
        temp_od = data["%s" % Name].values.tolist()
        # print(Name)
        temp_logod = [math.log2(x) for x in temp_od]

        log_od.append(temp_logod)

        Names.append(Name)

    return TimePerHour, log_od, Names


# def write_list_to_csv(data_list, filename):
#     with open(filename, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         for item in data_list:
#             csvwriter.writerow([item])


# def main():
#     input_list = input("Enter a list of values (comma-separated): ").split(',')
#     input_list = [item.strip() for item in input_list]
#
#     output_filename = input("Enter the output CSV filename: ")
#
#     write_list_to_csv(input_list, output_filename)
#     print(f"List has been written to '{output_filename}'")


if __name__ == "__main__":
    # File_path = "20230830-J.csv"
    File_path = "20230830WT.csv"


    # x = input()

    Xs, Ys, Names = ReadCSV(File_path)

    # print(len(Ys))
    # print(len(Names))
    Result_time = []
    Max_slope = []

    for i in range(len(Ys)):
        Result_Time, max_slope = calculate_intersection(Xs, Ys[i])
        # print(Names[i], Result_Time, max_slope)
        # print(Result_Time)
        # print(max_slope)
        Result_time.append(Result_Time)
        Max_slope.append(max_slope)

    print("LagTime")
    for x in Result_time:
        print(x)
    print("Max_Slope")
    for y in Max_slope:
        print(y)