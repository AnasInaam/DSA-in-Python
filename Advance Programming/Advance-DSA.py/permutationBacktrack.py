def permutation(arr ,left , right , res):
    if left == right:
        res.append(arr.copy())
    else :
        for i in range(left , right):
            arr[left] , arr[i] = arr[i] , arr[left]
            permutation(arr , left +1 , right , res)
            arr[left] , arr[i] = arr[i] , arr[left]
nums = [1 ,2 ,3 ]
output = []
permutation(nums , 0 , len(nums) , output)
print(output) 