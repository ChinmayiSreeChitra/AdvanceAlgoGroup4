from algorithms import measure_efficiency,InsertionSort,BubbleSort,QuickSort,RadixSort,MergeSort,CountingSort,HeapSort,SelectionSort
import matplotlib.pylab as plt
import matplotlib.pylab as plt1
import numpy as np
import pandas as pd
def analyze_visualization(input_array):
    sorting_algo = ["Insertion Sort", "Bubble Sort", "Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort", "Selection Sort", "Radix Sort"]
    efficiency_list = []
    
    for selected_algorithm in sorting_algo:
        if selected_algorithm == "Insertion Sort":
            #sorting_algorithm = InsertionSort()
            #InsertionSort()
            measure_efficiency(InsertionSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Bubble Sort":
            #sorting_algorithm = BubbleSort()
           # BubbleSort()
            measure_efficiency(BubbleSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Quick Sort":
            #sorting_algorithm = QuickSort()
           # QuickSort()
            measure_efficiency( QuickSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Merge Sort":
            #sorting_algorithm = MergeSort()
            #MergeSort()
            measure_efficiency(MergeSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Counting Sort":
            #sorting_algorithm = CountingSort()
            #CountingSort()
            measure_efficiency( CountingSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Heap Sort":
            #sorting_algorithm = HeapSort()
            #HeapSort()
            measure_efficiency( HeapSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Selection Sort":
            #sorting_algorithm = SelectionSort()
           # SelectionSort()
            measure_efficiency(SelectionSort(),input_array)
            efficiency_list.append(execution_time)
        elif selected_algorithm == "Radix Sort":
            #sorting_algorithm = RadixSort()
            #RadixSort()
            measure_efficiency(RadixSort(),input_array)
            efficiency_list.append(execution_time)
        #sorted_array, execution_time = measure_efficiency(sorting_algorithm,input_array)
        
        #fficiency_list.append(execution_time)
        for selected_algorithm,execution_time in sorting_algo,efficiency_list:
            print("selected_algorithm:",selected_algorithm,execution_time)

    print(efficiency_list)
    data=efficiency_list
    plt.bar(sorting_algo,data)
    plt.show()
    plt1.plot(sorting_algo,data)
    plt1.title("Linear graph", fontsize=25, color="green")
 
# Adding label on the y-axis
    plt1.ylabel('efficiency')
 
# Adding label on the x-axis
    plt1.xlabel('algorithms')
 
    plt1.show()
    return 0
