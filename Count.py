def count(arr, digit):
    count_num = 0
    for num in arr:
        if num == digit:
            count_num += 1
    return count_num
a = count([1,2,3,3,3,3,3,4,1,2,3,4], 3 )
print('The number of reputations are:', a)