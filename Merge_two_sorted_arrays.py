def merge(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[1] < arr2[j]:
            merged.append(arr1[i])
            i +=1
        else:
            merged.append(arr2[j])
            j +=1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return sorted(merged)
a = merge([1,2,3,4,5,6], [34,5,87,5,4,5,6,7])
print(a)