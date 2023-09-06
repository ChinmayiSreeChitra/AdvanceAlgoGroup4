
from algorithms import BubbleSort
if __name__=='__main__':
    print('Hello World!')

bubble_sort = BubbleSort()
sorting_algorithms = [{'name':'Bubble Sort','func':bubble_sort},{'name':'Quick Sort','func':None},{'name':'Merge Sort','func':None}]

sorting_algorithms[0].func.sort([1,2,3,4,5])
sorting_algorithms[1].func.sort([1,2,3,4,5])
sorting_algorithms[2].func.sort([1,2,3,4,5])


class SortingAlgorithm:

    def sort(self, array):
        pass




# Visualization

# X: merge_sort O(nlogn), quick_sort O(nlogn), bubble_sort O(n^2)
# Y: time (ms) for each algorithm


# Documentation for Application Testing (doctest)
# testcase1 = [10,4,2,5,1,3,6,8,7,9]
# testcase2 = [10,9,8,7,6,5,4,3,2,1]
# testcase3 = [1,2,3,4,5,6,7,8,9,10]
# testcase1000 = [random.randint(0,1000) for i in range(1000)]



