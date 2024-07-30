def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2  # Find the midpoint of the array

    left = array[:mid]  # Split the array into left half
    right = array[mid:]  # Split the array into right half

    left = merge_sort(left)  # Recursively sort the left half
    right = merge_sort(right)  # Recursively sort the right half

    return merge(left, right)  # Merge the sorted halves

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge the two sorted halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # If there are remaining elements in left, add them to result
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # If there are remaining elements in right, add them to result
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

def print_array(array):
    print(" ".join(map(str, array)))

if __name__ == "__main__":
    array = [5, 7, 1, 3, 9]  # Initial array
    print("Initial Array:")
    print_array(array)

    sorted_array = merge_sort(array)  # Sort and merge the array
    print("Sorted Array:")
    print_array(sorted_array)
