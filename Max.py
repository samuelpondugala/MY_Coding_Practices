def max(arr):
    maximum = 0
    for num in arr:
        if num >= maximum:
            maximum = num
    return maximum
a = max([1,2,3,4,5,6])
print(a)