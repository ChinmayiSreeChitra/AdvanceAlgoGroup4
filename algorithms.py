
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
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1
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
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = False
            counter += 1
        return array

# O(n log(n)) time | O(log(n)) space
class QuickSort(SortingAlgorithm):
    def sort(self, array):
        QuickSort.quickSortHelper(array, 0 ,len(array) - 1)
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
                rightIdx -= 1
            QuickSort.swap(pivotIdx, rightIdx, array)
        leftSubarraySmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
        if leftSubarraySmaller:
            QuickSort.quickSortHelper(array, startIdx, rightIdx - 1)
            QuickSort.quickSortHelper(array, rightIdx + 1, endIdx)
        else:
            QuickSort.quickSortHelper(array, rightIdx + 1, endIdx)
            QuickSort.quickSortHelper(array, startIdx, rightIdx - 1)

# O(n log(n)) time | O(n) space
class MergeSort(SortingAlgorithm):
    def sort(self, array):
        if len(array) <= 1:
            return array
        auxiliaryArray = array[:]
        MergeSort.mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
        return array
    
    def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
        if startIdx == endIdx:
            return
        middleIdx = (startIdx + endIdx) // 2
        MergeSort.mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
        MergeSort.mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
        MergeSort.doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

    def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
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
        