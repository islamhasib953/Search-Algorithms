def interpolationsearch(arr, x):
    start = 0
    end = len(arr) - 1
    while start<=end and x >= arr[start] and x <= arr[end]:
        mid = start + (x - arr[start]) * (end - start) // (arr[end] - arr[start])
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [1, 2, 6, 7, 9, 15, 22, 34, 69, 80]
print(interpolationsearch(arr,  7))


# mid = start + (x - arr[start]) * (end - start) // (arr[end] - arr[start])
# complexity time of jump search in worst case is O(n) and best case is O(log log n)
