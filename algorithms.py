
class SortingAlgorithm:
    time_taken = 0
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]
    def sort(self, array):
        print('Not Implemented')
        pass

# O(n^2) time/ O(1) space
class InsertionSort(SortingAlgorithm):
    def sort(self, array):
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j-1]:
                array[i], array[j] = array[j], array[i]
                j += 1
        return array
    

# @Time to be implemented
# O(n^2) time/ O(1) space
class BubbleSort(SortingAlgorithm):    
    def sort(self, array):
        isSorted = False
        counter = 0
        while not isSorted:
            isSorted = True
            for i in range(len(array)-1 - counter): # to stop checking the last number
                if array[i] > array[i+1]:
                    array[i], array[j] = array[j], array[i]
                    isSorted = False
            counter += 1
        return array


class QuickSort(SortingAlgorithm):
    
    def sort(self, array):
        return array
    
    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]
    
    def quickSortHelper(array, startIdx, endIdx):
        if startIdx >= endIdx:
            return
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while rightIdx >= leftIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                QuickSort.swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx += 1
            QuickSort.swap(pivotIdx, rightIdx, array)
        leftSubarraySmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
        if leftSubarraySmaller:
            QuickSort.quickSortHelper(array, startIdx, rightIdx - 1)
            QuickSort.quickSortHelper(array, rightIdx + 1, endIdx)
        else:
            QuickSort.quickSortHelper(array, rightIdx + 1, endIdx)
            QuickSort.quickSortHelper(array, startIdx, rightIdx + 1)


