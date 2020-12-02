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


    def mergesort(self, arr, low, high):

        if high <= low:
            return

        middle  = (low + high) // 2

        self.mergesort(arr,low,middle)
        self.mergesort(arr,middle+1,high)

        i=j=k=0

        while i < (middle-low) and j < (high-(middle+1)):
            print(low,high, arr)
            if arr[i] < arr[j]:
                arr[k], arr[low+i] = arr[low+i], arr[k]
                i += 1

            else:
                arr[k], arr[middle+1+j] = arr[middle+1+j], arr[k]
                j += 1

            k += 1

        while i < middle-low:
            arr[k], arr[low+i] = arr[low+i], arr[k]
            i += 1
            k += 1

        while j < high-(middle+1):
            arr[k], arr[middle+1+j] = arr[middle+1+j], arr[k]
            j += 1
            k += 1

        return

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

if __name__ == "__main__":


    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end ="\n")
    printList(arr)
    s = Sort()
    s.mergesort(arr,0,len(arr))
    print("Sorted array is: ", end ="\n")
    printList(arr)
