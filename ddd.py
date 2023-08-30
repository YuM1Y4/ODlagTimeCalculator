import numpy as np

import pandas as pd
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def largest_slope(Xs, Y):
    # print(Y)
    if len(Xs) != len(Y):
        raise ValueError("The number of Xs and Ys must be equal.")

    n = len(Xs)
    max_slope = float('-inf')

    for i in range(n - 28):
        x1, y1 = Xs[i], Y[i]
        x2, y2 = Xs[i + 28], Y[i + 28]

        slope = (y2 - y1) / (x2 - x1)
        max_slope = max(max_slope, slope)

    return max_slope

def plot_scatter(GrowthRate):
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the size of the plot as needed
    ax.scatter(Ys_name, GrowthRate)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Scatter Plot of Data Points")
    plt.xticks(rotation=90)
    # ax.axhline(y=largest_slope_val * Xs[-1], color='r', linestyle='-', label=f"Largest Slope: {largest_slope_val:.2f}")
    return fig



def read_data():
    global canvas
    global Xs
    global Ys
    global Ys_name
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    data = pd.read_csv(file_path)
    Xs = data["Time/h"].values.tolist()
    # Example input data (replace with your actual data)
    Ys = []
    Ys_name = []
    for i in range(2, len(list(data)), 2):
        Ys_name.append(list(data)[i])
        Yps = data["%s" % (list(data)[i])].values.tolist()
        Ys.append(Yps)
    # print(Ys)
    # print(len(Ys))
    # print(len(Xs))
    # Clear previous plot if any


    fig = plot_scatter(GrowthRate_diagram())
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)



def GrowthRate_diagram():
    GrowthRate = []
    for j in range (len(Ys)):
        largest_slope_val = largest_slope(Xs, Ys[j])
        GrowthRate.append(1 / largest_slope_val)

    return GrowthRate



if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("CSV File Reader")
    root.geometry("1920x1080")

    container_frame = tk.Frame(root)
    container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    plot_frame = tk.Frame(container_frame)
    plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create a button to open the CSV file
    open_button = tk.Button(container_frame, text="Open CSV File", command=read_data())
    open_button.pack(pady=10)






    # Create a label to display the result




    # Run the main application loop
    root.mainloop()


        # print("The largest slope on the curve is:", largest_slope_val)

    # x = input()
    # while type(x) != "int":
    #     Ys = data["%s"%(x)].values.tolist()
    #     largest_slope_val = largest_slope(Xs, Ys)
    #
    #     print("The largest slope on the curve is:", largest_slope_val)
    #     x = input()