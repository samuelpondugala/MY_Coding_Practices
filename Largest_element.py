def largest_element(arr):
    large = 0
    for i in arr:
        if i>= large:
            large = i
    return large
a = largest_element([10,2,3,4,5,6,7,8,9])
print(a)