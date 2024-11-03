#Merge and Sort Two or lists
def merge_sort(arr1,arr2):
    merged_list = arr1+arr2
    for val in merged_list:
        num = merged_list[0]
        if val <= num:
            merged_list[0] = val
        else:
            merged_list[0] = num
    return
lst = merge_sort([1,2,3,4,5], [6,9,8,7])
print(lst)