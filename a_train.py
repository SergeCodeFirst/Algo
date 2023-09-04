import math

def findTarget(arr, target, start, end):
    if start > end:
        return -1
    
    middle = math.floor((start + end) / 2)

    if arr[middle] == target:
        return middle
    
    if arr[middle] < target:
        return findTarget(arr, target, middle + 1,len(arr) - 1)

    if arr[middle] > target:
        return findTarget(arr, target, 0, middle - 1)

arr = [1,2,3,4,5,6]
k = 7
print(findTarget(arr, k, 0, len(arr)-1))