# arr = [ 'm' , 'na' , 'i']
# arr2 = ['y' , 'me' , 's']
# # for i in range(len(arr)):
# #     arr[i] = arr[i] + arr2[i]
# # print(arr)

# arr = [arr[x] + arr2[x] for x in range(len(arr)) ]
# print(arr)


# # arr1 , arr2 = [] , []
# # size = len(arr)
# # cut = size -1-k
# # arr1 = arr[0:cut]
# # arr2 = arr[cut :size]

# result =  arr2 + arr1 

# print(result)

# arr = [ 100 , 23, 12,3 ,1,2, 1,2,  100 ,13 , 100 , 30]
# for i in range(len(arr)-1 , -1 , -1):
#     if arr[i] == 100:
#         arr[i] = 10
#         break
# print(arr)

# arr = [100 if x == 0 else x for x in arr ]

# num = 123321
# reverse = 0 
# while num > 0 :
#     last = num % 10
#     reverse = last + 10* reverse
#     num = num // 10

# arr = [123, 321, 234, 432, 44, 55, 56, 54, 44, 9, 9, 55]
# arr1 = []

# for num in arr:
#     ele = str(num)
#     ele_rev = ele[::-1]
#     if int(ele_rev) not in arr:
#             arr1.append(num)
# print(arr1)

# from collections import Counter
# map1 = Counter(s)
# print(map1)
# map1 = {}
# for ch in s:
#     if ch not in map1:
#         map1[ch] = 1
#     map1[ch]  += 1
# print(map1)

# s = "aabbcs"
# list1, list2 = [], []

# for ch in s:
#     if ch not in list1:
#         list1.append(ch)

# for i in range(len(list1)):
#     list2.append(s.count(list1[i]))  

# for i in range(len(list1)):
#     print(list1[i], ":", list2[i])
# s = "this the is end"
# s = s.replace(" " , "")

# print(s)


# arr = [ 1,2,3,4, 5]
# for i in range(len(arr)):
#     if i == 0:
#         continue
#     arr[i] = (arr[i-1]+arr[i])
# print(arr)

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                print(arr)
arr = [ 34,5,4,2,3,5,2]
bubble(arr)