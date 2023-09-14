from algorithms import measure_efficiency,InsertionSort,BubbleSort,QuickSort,RadixSort,MergeSort,CountingSort,HeapSort,SelectionSort
import matplotlib.pylab as plt
import matplotlib.pylab as plt1
import numpy as np
import pandas as pd
def analyze_visualization(input_array):
    sorting_algo = ["Insertion Sort", "Bubble Sort", "Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort", "Selection Sort", "Radix Sort"]
    efficiency_list = []
    output = []
    for selected_algorithm in sorting_algo:
        if selected_algorithm == "Insertion Sort":
            #sorting_algorithm = InsertionSort()
            #InsertionSort()
            output = measure_efficiency(InsertionSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Bubble Sort":
            #sorting_algorithm = BubbleSort()
           # BubbleSort()
            output=measure_efficiency(BubbleSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Quick Sort":
            #sorting_algorithm = QuickSort()
           # QuickSort()
            output=measure_efficiency(QuickSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Merge Sort":
            #sorting_algorithm = MergeSort()
            #MergeSort()
            output=measure_efficiency(MergeSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Counting Sort":
            #sorting_algorithm = CountingSort()
            #CountingSort()
            output=measure_efficiency(CountingSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Heap Sort":
            #sorting_algorithm = HeapSort()
            #HeapSort()
            output=measure_efficiency(HeapSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Selection Sort":
            #sorting_algorithm = SelectionSort()
           # SelectionSort()
            output=measure_efficiency(SelectionSort(),input_array)
            efficiency_list.append(output[1])
        elif selected_algorithm == "Radix Sort":
            #sorting_algorithm = RadixSort()
            #RadixSort()
            output=measure_efficiency(RadixSort(),input_array)
            efficiency_list.append(output[1])
        #sorted_array, execution_time = measure_efficiency(sorting_algorithm,input_array)
        
        #fficiency_list.append(execution_time)
        #for selected_algorithm,execution_time in sorting_algo,efficiency_list:
            #print("selected_algorithm:",selected_algorithm,execution_time)

    print(efficiency_list)
    data=[float(val) for val in efficiency_list]
    # Create the plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(sorting_algo, data, marker='o', linestyle='-')
    plt.xlabel('Algorithms')
    plt.ylabel('Time in Seconds')
    plt.title('Efficiency of Sorting Algorithms')

# Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')  # Rotate by 45 degrees and align to the right
    # Set the y-axis limits with a specified interval
    y_min = min(data)
    y_max = max(data)
    y_interval = 0.000010
    plt.ylim(y_min - y_interval, y_max + y_interval)

# Label data points on the graph
    for x, y in zip(sorting_algo, data):
        plt.annotate(f'{y:6f}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

# Show the plot
    plt.tight_layout()  # Ensure labels are not cut off
    plt.show()
    plt.plot(sorting_algo, data)
    plt.xlabel('Algorithms')
    plt.ylabel('Time in Seconds')
    plt.title('Efficiency of Algorithms')
    #plt.bar(sorting_algo,data)
    #plt.show()
    #plt1.plot(sorting_algo,data)
    #plt1.title("Linear graph", fontsize=25, color="green")
 
# Adding label on the y-axis
    #plt1.ylabel('efficiency')
 
# Adding label on the x-axis
    #plt1.xlabel('algorithms')
 
    #plt.show()
    return 0
