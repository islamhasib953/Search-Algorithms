def exponentialsearch(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    n=len(arr)
    while i < n and arr[i] <= x:
        if arr[i]==x:
            return i
        i*=2
    return binarysearch(arr, i//2, min(i,n-1), x)

def binarysearch(arr, start, end, x):
    while start<=end:
        mid = start + (end - start) // 2
        if arr[mid]>x:
            end=mid-1
        elif arr[mid]<x:
            start=mid+1
        else:
            return mid
    return -1


arr = [1, 2, 6, 7, 9, 15, 22, 34, 69, 80]
print(exponentialsearch(arr,  34))

# complexity time of  exponential search is O(log n)
