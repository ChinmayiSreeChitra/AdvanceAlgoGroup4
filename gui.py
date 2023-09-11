from utils import *

# for algo in algos: --> run as needed
#     algo.run(arr)

# Layout
#  Input text box
#  browser button for input file
#  log box
#  visualize button


#  input file browser button (input.txt)
#  Visualize button
#  output1.txt (sorted array)
#  input data from user (array of numbers) (comma separated)
#  from gui import logger
#  log('Hello World!')
#  visualtization of sorting algorithm visualize() --> matplotlib (bar graph) with close button
#  [] run all algorithms and compare memory usage

# Necessary libraries import
import PySimpleGUI as psg
import random
import time
import matplotlib.pyplot as plt
import re
import subprocess,sys
import PIL
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# DEFINE SORTING ALGORITHMS HERE
def sort(nums):
    nums.sort()
    return nums

# function to VALIDATE AND PREPROCESS the user input string
def preprocess(string):
    try:
        string = string.strip()  # removing leading and trailing space
        string = re.sub(' +', ' ',string)  # removal of extra spaces from string
        print(string)
        string = re.sub(',+', ' ', string)
        print(string)
        string = string.split(" ")  # string to list of string conversion
        nums = [int(i) for i in string]
        return nums
    except:
        return "Error!!! Enter valid data in valid format!!!"

#window to plot the graph(this is generating sample graph and this muSt be changed)
def update_plot(window):
    # Generate your Matplotlib plot here
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])  # Example data
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Matplotlib Plot")

    # Embedding the matplotlib plot in the PySimpleGUI window
    canvas_elem = window["-CANVAS-"]
    canvas = FigureCanvasTkAgg(fig, canvas_elem.Widget)
    canvas.get_tk_widget().pack(fill='both', expand=1)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=1)
    canvas.get_tk_widget().update()


# layout of the application
layout =[
    [psg.Titlebar("Algorithm Analysis Visualizer")],
    [psg.Text("Please enter the numbers separated by commas or space")],
    [psg.Input("", key="-INPUT-")],
    [psg.Text("Select algorithms"), psg.Checkbox("Bubble Sort",key="-BUBBLE-"),psg.Checkbox("Quick Sort",key="-QUICK-"),psg.Checkbox("Merge Sort",key="-MERGE-")],
    [psg.Checkbox("Selection Sort",key="-SELECTION-"),psg.Checkbox("Radix Sort",key="-RADIX-"),psg.Checkbox("Counting Sort",key="-COUNTING-"), psg.Checkbox("Heap Sort",key="-HEAP-"),psg.Checkbox("Insertion Sort",key="-INSERTION-")],
    [psg.Text("Sorted Elements:",key="-HOLDER-", visible=False), psg.Text("", key="-OUTPUT-", visible=False)],
    [psg.Text("Verbosity", key="verbosity"), psg.Radio("ON", "verbosity", key='verbose_ON', enable_events=True, default=False), psg.Radio("OFF", "verbosity", key="verbose_OFF", enable_events=True, default=True)],
    [psg.Output(size=(85, 10), background_color='white', text_color='black', key='Status_Box', visible=False)],
    [psg.Canvas(key="-CANVAS-")],
    [psg.Button("Start Sorting", key="-START-"), psg.Button("Plot", key="-PLOT-"), psg.Button("Exit")],


]

# Making GUI here
def GUI():
    global layout
    window = psg.Window("DarkViz", layout=layout,element_justification="center") # window instance creation

    while True:
        event, values = window.read() # read all the content from the window instance
        if event in (None, "Exit"): # if user wants to exit
            break
        if event == "-START-": # IF USER CLICKS ON START BUTTON
            try:
                # preprocessing and validating input
                nums = preprocess(values["-INPUT-"])
                print(values)
                print(nums)

                # checking the choice of sorting algos
                if values["-BUBBLE-"]:
                    # call BUBBBLE sort and do stuff
                    pass
                if values["-QUICK-"]:
                    # call QUICK sort and do stuff
                    pass
                if values["-RADIX-"]:
                    # call RADIX sort and do stuff
                    pass
                if values["-MERGE-"]:
                    # call MERGE sort and do stuff
                    pass
                if values["-SELECTION-"]:
                    # call SELECTION sort and do stuff
                    pass
                if values["-COUNTING-"]:
                    # call COUNTING sort and do stuff
                    pass
                if values["-HEAP-"]:
                    # call HEAP sort and do stuff
                    pass
                if values["-INSERT-"]:
                    # call INSERTION sort and do stuff
                    pass


                res = sort(nums)
                print(res)
                res = map(str, res)
                res = " ".join(list(res))
                print(res)
                window.Element("-HOLDER-").update(visible=True)
                window.Element("-OUTPUT-").update(visible=True)
                window.Element("-OUTPUT-").update(res)
            except:
                psg.Popup('Invalid Input', keep_on_top=True)
        if values["verbose_ON"] == True:
            window.Element("Status_Box").Update(visible=True)

        if values["verbose_OFF"] == True:
            window.Element("Status_Box").Update(visible=False)

        verbosity = values['verbose_ON']
        if event == "-PLOT-":
            update_plot(window)


if __name__ == '__main__':
    GUI()


# WindOW for the terminal logs. UNCOMMENT IF FACING ANY ERROR OTHERWISE LEAVE AS IT IS.
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me
    retval = p.wait(timeout)
    return (retval, output)                         # also return the output just for fun
