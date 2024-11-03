def find_second_largest(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
a = find_second_largest([1,2,3,4,5,4,3,5,4,6,7,9,10,9])
print(a)
