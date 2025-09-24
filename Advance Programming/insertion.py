arr = [ 1 ,3 ,3, 56 ,67 ,88 ,8 ]

def insertion(arr):
    for i in range(1 , len(arr)):
        key = arr[i]
        j = i-1 
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
insertion(arr)
print(arr)
