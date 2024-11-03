def remove_duplicates(arr):
    unique_arr=[]
    for num in sorted(arr):
        if not unique_arr or unique_arr[-1] != num:
            unique_arr.append(num)
    return unique_arr
a = remove_duplicates([1,1,1,1,2,2,2,3,4,5,4,3,2,4,5,6,7,8,8,9,1,2,3])
print(a)