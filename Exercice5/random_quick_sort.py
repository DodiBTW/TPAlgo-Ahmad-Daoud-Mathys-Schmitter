import random

class RandomQuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self._randomized_quick_sort(self.array, 0, len(self.array) - 1)

    def _randomized_quick_sort(self, arr, low, high):
        if low < high:
            pi = self._randomized_partition(arr, low, high)
            self._randomized_quick_sort(arr, low, pi - 1)
            self._randomized_quick_sort(arr, pi + 1, high)

    def _randomized_partition(self, arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return self._partition(arr, low, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1