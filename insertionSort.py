def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i
        while j > 0 and arr[j - 1] > current_value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = current_value

# Initial unsorted array
arr = [2, 6, 5, 1, 3, 4]
print("Unsorted array:", arr)

# Insert a new value
new_value = 7
arr.append(new_value)
print("Array after inserting new value:", arr)

# Sort the array
insertion_sort(arr)
print("Sorted array:", arr)
