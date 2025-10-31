

def find_avg_cont(arr, k):
    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add next element

        # slide the window when we hit size k
        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]  # remove element going out
            window_start += 1

    return result

print(find_avg_cont([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))