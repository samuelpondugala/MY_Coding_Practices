def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1
a = binary_search([1,2,3,4,5,6,7,8,9,8,7,], 3)
print("Position of given target is:",a)
