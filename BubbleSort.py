# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all elements in the list
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
             # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


# List to be sorted 
arr = [64, 34, 25, 12, 22, 11, 90]
 

print ("Before Sorting: {}".format(arr))
bubbleSort(arr)
print ("After Sorting: {}".format(arr))

