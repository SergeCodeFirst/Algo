import math

# def findTarget(arr, target, start, end):
#     if start > end:
#         return -1
    
#     middle = math.floor((start + end) / 2)

#     if arr[middle] == target:
#         return middle
    
#     if arr[middle] < target:
#         return findTarget(arr, target, middle + 1,len(arr) - 1)

#     if arr[middle] > target:
#         return findTarget(arr, target, 0, middle - 1)

# arr = [1,2,3,4,5,6]
# k = 7
# print(findTarget(arr, k, 0, len(arr)-1))


def bin_search(arr, target):
    lo = 0
    hi = len(arr) - 1

    if len(arr) == 0:
        return "Not Found"

    while lo < hi:
        mid = (lo + hi) // 2
        
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            lo = mid + 1

        else:
            hi = mid - 1

    return "Not Found"


print(bin_search([2,3,4,5,6,7,8,9], 7))
print(bin_search([2,3,4,5,6], 7))
print(bin_search([], 7))
