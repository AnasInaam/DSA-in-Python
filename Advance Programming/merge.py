arr = [ 20,49, 70 ,50 ,25 , 100 , 333, 45, 4, 554, 54 , 54 ,30 ]
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left , right)
def merge(left , right):
    r , i , j= [] , 0 , 0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            r.append(left[i])
            i +=1
        else :
            r.append(right[j])
            j +=1
    r.extend(left[i:])
    r.extend(right[j:])
    return r

print(mergesort(arr))
