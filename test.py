import array
import unittest
from algorithms import *

#Test that it can algorithm can sort all the positive numbers
class PositiveNumSortData(unittest.TestCase):
    #testing for INSERTION sort
    def test_list_int(self):
        data = [10,89,45,34,90,0,4]
        result = InsertionSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

    #testing for BUBBLE sort
    def test_list_int(self):
        data = [10,89,45,34,90,0,4]
        result = BubbleSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for QUICKSORT 
    def test_list_int(self):
        data = [10,89,45,34,90,0,4]
        result = QuickSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for MERGE sort
    def test_list_int(self):
        data = [10,89,45,34,90,0,4]
        result = MergeSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    


#Test if algorithm can sort all big numbers
class LargeNumSortData(unittest.TestCase):
    #testing for INSERTION sort
    def test_list_int(self):
        data = [101,6545,231,2313,564,100,986521,789]
        result = InsertionSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

    #testing for BUBBLE sort
    def test_list_int(self):
        data = [101,6545,231,2313,564,100,986521,789]
        result = BubbleSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for QUICKSORT 
    def test_list_int(self):
        data = [101,6545,231,2313,564,100,986521,789]
        result = QuickSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for MERGE sort
    def test_list_int(self):
        data = [101,6545,231,2313,564,100,986521,789]
        result = MergeSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
#Test if algorithm can sort floating numbers
class FloatNumSortData(unittest.TestCase):
    #testing for INSERTION sort
    def test_list_int(self):
        data = [10.6,1.2,7.8,3.4,0.03,2.3,9.5,7.8]
        result = InsertionSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

    #testing for BUBBLE sort
    def test_list_int(self):
        data = [10.6,1.2,7.8,3.4,0.03,2.3,9.5,7.8]
        result = BubbleSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for QUICKSORT 
    def test_list_int(self):
        data = [10.6,1.2,7.8,3.4,0.03,2.3,9.5,7.8]
        result = QuickSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for MERGE sort
    def test_list_int(self):
        data = [10.6,1.2,7.8,3.4,0.03,2.3,9.5,7.8]
        result = MergeSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)   

    #Test if algorithm can sort floating numbers

#Test if algorithm can sort mixed (floating and int) numbers
class MixedNumSortData(unittest.TestCase):
    #testing for INSERTION sort
    def test_list_int(self):
        data = [2,7.8,10,0.03,2.3,9.5,7.8]
        result = InsertionSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

    #testing for BUBBLE sort
    def test_list_int(self):
        data = [2,7.8,10,0.03,2.3,9.5,7.8]
        result = BubbleSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for QUICKSORT 
    def test_list_int(self):
        data = [2,7.8,10,0.03,2.3,9.5,7.8]
        result = QuickSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for MERGE sort
    def test_list_int(self):
        data = [2,7.8,10,0.03,2.3,9.5,7.8]
        result = MergeSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data) 

#Test if algorithm can sort negative numbers
class NegativeNumSortData(unittest.TestCase):
    #testing for INSERTION sort
    def test_list_int(self):
        data = [-1,3,-6,2,-2.3,1,-9.3,-0.002]
        result = InsertionSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

    #testing for BUBBLE sort
    def test_list_int(self):
        data = [-1,3,-6,2,-2.3,1,-9.3,-0.002]
        result = BubbleSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for QUICKSORT 
    def test_list_int(self):
        data = [-1,3,-6,2,-2.3,1,-9.3,-0.002]
        result = QuickSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)
    
    #testing for MERGE sort
    def test_list_int(self):
        data = [-1,3,-6,2,-2.3,1,-9.3,-0.002]
        result = MergeSort.sort(self, data)
        data.sort()
        self.assertEqual(result, data)

if __name__== '__main__':
    unittest.main()
    
