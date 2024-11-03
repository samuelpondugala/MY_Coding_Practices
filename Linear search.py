def search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print('Item is Present in the given list')
            break
a = search([1,2,4,5,6,7,8],5)
print(a)