def countingSort(array, significantPlace):
    size = len(array)
    outputArray = [0] * size
    countArray = [0] * 10

    # Store count of each value according to responding significant value
    for i in range(size):
        element = (array[i] // significantPlace) % 10
        countArray[element] += 1

    # Cumulate elements count in count array
    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    # Sort the element into output array according to the significant place value
    i = size - 1
    while i >= 0:
        currentElement = array[i]
        elementSignificant = (array[i] // significantPlace) % 10
        countArray[elementSignificant] -= 1
        newPosition = countArray[elementSignificant]
        outputArray[newPosition] = currentElement
        i -= 1

    return outputArray


def radixSort(array):
    largestElement = max(array)

    # Determine how many digit the largest element has
    digit = 0
    while largestElement > 0:
        largestElement //= 10
        digit += 1

    significantPlace = 1
    outputArray = array

    # Perform counting sort according to the value of significant value
    while digit > 0:
        outputArray = countingSort(outputArray, significantPlace)
        significantPlace *= 10
        digit -= 1

    return outputArray


A = [16, 30, 95, 51, 84, 23, 62, 44]
print(A)
sortedA = radixSort(A)
print(sortedA)
