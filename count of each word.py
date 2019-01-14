def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
            print(j)
        arr[j + 1] = key
        print(arr)

    # Driver code to test above


arr = [12, 11, 13, 5, 6]
insertionSort(arr)

# print(arr)

    # This code is contributed by Mohit Kumra