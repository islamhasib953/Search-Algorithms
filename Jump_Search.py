import math

def jumpsearch(arr, x):
    n=len(arr)
    left=0
    right=0
    jump=int(math.sqrt(n))
    while arr[left]<=x and left<n:
        right=min(right+jump, n-1)
        if x>= arr[left] and x <=arr[right]:
            break
        left+=jump
    if arr[left]>x or left>=n:
        return 1
    right = min(right+jump, n-1)
    i=left
    while i<=right and arr[i]<=x:
        if arr[i] == x:
            return i
        i+=1
    return -1
print(jumpsearch([1,2,6,7,9,15,22,34,69,80],6))


# complexity time of jump search is O(sqrt(n)) or O(n/m + (m-1))