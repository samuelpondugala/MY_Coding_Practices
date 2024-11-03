def binary_search(arr, target):
    arr = sorted(arr)
    print("Sorted array: ", arr)
    low, high = 0, len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
a = list(map(int, input("enter a list: ").split(',')))
b = int(input("Enter number: "))
res = binary_search(a, b)
print("Position of given traget is:",res)