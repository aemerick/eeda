"""
  A. Emerick

  Who decided that knowledge of sorting algorithms demonstrates
  anything useful?


  Probably should implement and understand:

    1) Quicksort
    2) bubble sort
    3) ??
"""



class Sort:

    def __init__(self):

        return

    def quicksort(self, arr, low, high):
        """
        Quicksort algorithm. Chooses a pivot point
        and sorts array on either side of pivot point.

        """

        if (low < high):

            pi = self._quickpartition(arr, low, high)

            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)

        return arr

    def _quickpartition(self, arr, low, high):
        pivot = arr[high]

        i = (low - 1)

        for j in range(low, high):

            if arr[j] < pivot:
                i += 1
                val    = arr[j]
                arr[j] = arr[i]
                arr[i] = val


        val       = arr[high]
        arr[high] = arr[i + 1]
        arr[i+1]  = val

        return i + 1
