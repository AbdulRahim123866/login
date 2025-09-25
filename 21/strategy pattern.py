# from abc import ABC,abstractmethod
#
# class SortStrategy(ABC):
#     @abstractmethod
#     def sort(self,data):pass
#
#
# class QuickSort(SortStrategy):
#     def sort(self,data):
#         print("Quick sorting...")
#         return sorted(data)
#
# class MergeSort(SortStrategy):
#     def sort(self,data):
#         print("Merge sorting...")
#         return sorted(data)
#
# #Usage
# data=[5,2,8,1,9]
# result=QuickSort().sort(data)
# #Switch strategy
# result=MergeSort().sort(data)
from typing import List, Callable


class SortStrategy:
    def sort(self, data: List[int]) -> List[int]:
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr=data.copy()
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
class QuickSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr=data.copy()
        if len(data)<=1:
            return data
        else:
            pivot=data[0]
            left=[x for x in data[1:] if x<=pivot]
            right=[x for x in data[1:] if x>pivot]

            return self.sort(left)+[pivot]+self.sort(right)

class SortContext:
    def __init__(self,strategy:SortStrategy):
        self._strategy=strategy

    def set_strategy(self,strategy:SortStrategy):
        self._strategy=strategy

    def sort(self,data:List[int])->List[int]:
        return self._strategy.sort(data)


if __name__=="__main__":
    data=[5,2,9,1,5,6]

    context=SortContext(BubbleSortStrategy())
    print("Bubble Sort:", context.sort(data))

    #Change to Quick Sort
    context.set_strategy(QuickSortStrategy())
    print("Quick Sort:",context.sort(data))
#طريقة اخرى
#___________________________________________________________________________


def bubble_sort(self, data: List[int]) -> List[int]:
    arr=data.copy()
    if len(data)<=1:
        return data
    else:
        pivot=data[0]
        left=[x for x in data[1:] if x<=pivot]
        right=[x for x in data[1:] if x>pivot]

        return self.sort(left)+[pivot]+self.sort(right)

def quick_sort(self, data: List[int]) -> List[int]:
    arr=data.copy()
    n=len(arr)
    for i in range(n):
       for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
from typing import List, Callable

class SortContext:
    def __init__(self,strategy:Callable[[List[int]],List[int]]):
        self._strategy=strategy

    def set_strategy(self,strategy:Callable[[List[int]],List[int]]):
        self._strategy=strategy

    def sort(self,data:List[int])->List[int]:
        return self._strategy(data)


if __name__=="__main__":

    data=[5,2,9,1,5,6]
    context=SortContext(bubble_sort)
    print("Bubble Sort:",context.sort(data))

    context.set_strategy(quick_sort)
    print("Quick Sort:",context.sort(data))

