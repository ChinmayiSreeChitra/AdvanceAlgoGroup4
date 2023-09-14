

import tkinter as tk
from tkinter import ttk
import statistics
import time
import math

class SortingAlgorithm:
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

    def sort(self, array):
        pass


class InsertionSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                self.swap(j, j - 1, array)
                j -= 1
        end_time = time.time()
        return array, end_time - start_time


class BubbleSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        isSorted = False
        counter = 0
        while not isSorted:
            isSorted = True
            for i in range(len(array) - 1 - counter):
                if array[i] > array[i + 1]:
                    self.swap(i, i + 1, array)
                    isSorted = False
            counter += 1
        end_time = time.time()
        return array, end_time - start_time


class QuickSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        self.quickSortHelper(array, 0, len(array) - 1)
        end_time = time.time()
        return array, end_time - start_time

    def quickSortHelper(self, array, startIdx, endIdx):
        if startIdx >= endIdx:
            return
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while rightIdx >= leftIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                self.swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        self.swap(pivotIdx, rightIdx, array)
        leftSubarraySmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
        if leftSubarraySmaller:
            self.quickSortHelper(array, startIdx, rightIdx - 1)
            self.quickSortHelper(array, rightIdx + 1, endIdx)
        else:
            self.quickSortHelper(array, rightIdx + 1, endIdx)
            self.quickSortHelper(array, startIdx, rightIdx - 1)


class MergeSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        if len(array) <= 1:
            return array, 0.0
        auxiliaryArray = array[:]
        self.mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
        end_time = time.time()
        return array, end_time - start_time

    def mergeSortHelper(self, mainArray, startIdx, endIdx, auxiliaryArray):
        if startIdx == endIdx:
            return
        middleIdx = (startIdx + endIdx) // 2
        self.mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
        self.mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
        self.doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

    def doMerge(self, mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
        k = startIdx
        i = startIdx
        j = middleIdx + 1
        while i <= middleIdx and j <= endIdx:
            if auxiliaryArray[i] <= auxiliaryArray[j]:
                mainArray[k] = auxiliaryArray[i]
                i += 1
            else:
                mainArray[k] = auxiliaryArray[j]
                j += 1
            k += 1
        while i <= middleIdx:
            mainArray[k] = auxiliaryArray[i]
            i += 1
            k += 1
        while j <= endIdx:
            mainArray[k] = auxiliaryArray[j]
            j += 1
            k += 1


class CountingSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        max_value = max(array)
        min_value = min(array)
        range_of_elements = max_value - min_value + 1
        count_array = [0] * range_of_elements
        output_array = [0] * len(array)

        for num in array:
            count_array[num - min_value] += 1

        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]

        for i in range(len(array) - 1, -1, -1):
            output_array[count_array[array[i] - min_value] - 1] = array[i]
            count_array[array[i] - min_value] -= 1

        for i in range(len(array)):
            array[i] = output_array[i]

        end_time = time.time()
        return array, end_time - start_time


class HeapSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        self.build_max_heap(array)
        for i in range(len(array) - 1, 0, -1):
            self.swap(0, i, array)
            self.max_heap(array, index=0, size=i)
        end_time = time.time()
        return array, end_time - start_time

    def build_max_heap(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heap(array, index=i, size=n)

    def max_heap(self, array, index, size):
        largest = index
        leftNumber = 2 * index + 1
        rightNumber = 2 * index + 2
        if leftNumber < size and array[leftNumber] > array[largest]:
            largest = leftNumber
        if rightNumber < size and array[rightNumber] > array[largest]:
            largest = rightNumber
        if largest != index:
            self.swap(index, largest, array)
            self.max_heap(array, largest, size)

    def heap_sort(self, array):
        return self.sort(array)

class SelectionSort(SortingAlgorithm):
    def find_min_index(self, array, start):
        min_index = start
        for j in range(start + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        return min_index

    def sort(self, array):
        start_time = time.time()
        for i in range(len(array)):
            min_index = self.find_min_index(array, i)
            self.swap(i, min_index, array)
        end_time = time.time()
        return array, end_time - start_time

class RadixSort(SortingAlgorithm):
    def sort(self, array):
        start_time = time.time()
        max_value = max(array, key=abs)
        num_digits = int(math.log10(abs(max_value))) + 1 if max_value != 0 else 1

        for digit_place in range(num_digits):
            counting_sort = CountingSort()
            sorted_array, _ = counting_sort.sort(array)
            array = sorted_array

        end_time = time.time()
        return array, end_time - start_time

def measure_efficiency(sorting_algorithm, input_array):
    sorted_array, execution_time = sorting_algorithm.sort(input_array.copy())
    return sorted_array, execution_time


def sort_button_clicked():
    input_str = input_entry.get()
    input_array = list(map(int, input_str.split()))
    
    selected_algorithm = algorithm_combobox.get()

    if selected_algorithm == "Insertion Sort":
        sorting_algorithm = InsertionSort()
    elif selected_algorithm == "Bubble Sort":
        sorting_algorithm = BubbleSort()
    elif selected_algorithm == "Quick Sort":
        sorting_algorithm = QuickSort()
    elif selected_algorithm == "Merge Sort":
        sorting_algorithm = MergeSort()
    elif selected_algorithm == "Counting Sort":
        sorting_algorithm = CountingSort()
    elif selected_algorithm == "Heap Sort":
        sorting_algorithm = HeapSort()
    elif selected_algorithm == "Selection Sort":
        sorting_algorithm = SelectionSort()
    elif selected_algorithm == "Radix Sort":
        sorting_algorithm = RadixSort()
    else:
        return


    sorted_array, execution_time = measure_efficiency(sorting_algorithm, input_array)
    
    # Update the result labels to display the sorted array and execution time
    result_label.config(text=f"Sorted Array: {sorted_array}")
    time_label.config(text=f"Execution Time: {execution_time:.6f} seconds")

# Create the main window
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

# Create input label and entry
input_label = tk.Label(root, text="Enter space-separated integers:")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

# Create algorithm selection dropdown
algorithm_label = tk.Label(root, text="Select Sorting Algorithm:")
algorithm_label.pack()

algorithm_combobox = ttk.Combobox(root, values=["Insertion Sort", "Bubble Sort", "Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort", "Selection Sort", "Radix Sort"])
algorithm_combobox.pack()

# Create a sort button
sort_button = tk.Button(root, text="Sort", command=sort_button_clicked)
sort_button.pack()

# Create labels to display the sorted array and execution time
result_label = tk.Label(root, text="Sorted Array: ")
result_label.pack()

time_label = tk.Label(root, text="Execution Time: ")
time_label.pack()

# Start the GUI event loop
root.mainloop()

