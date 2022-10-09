# Counting Sort

# Sorting the array given
def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    # Creating a count array to store count of individual elements and initialize count array as 0

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1

    # Changing count_arr[i] so that count_arr[i] now contains actual position of this element in output array

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Building the output character array

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Copying the output array to arr, so that arr now contains sorted characters

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


# Tester program
arr = [16, 30, 95, 51, 84, 23, 62, 44]
ans = count_sort(arr)
print("Sorted character array is: " + str(ans))