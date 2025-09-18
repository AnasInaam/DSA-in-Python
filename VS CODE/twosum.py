# x = [ 23 ,56, 32,55,34,2,45]
# print(x.index(34))
# for i in range(len(x)):
# list1 = [1,2,3,4,5]
# for i in range(len(list1)):
#     # made list2 from the elements of list1[i:len(list1)]
#     list2 = list1[i:len(list1)]
#     if list2 in list1:
#         print(list2)
list1 = [1, 2, 3, 4, 5 , 5, 4 , 3]
list2 = [3, 4]

if all(item in list1 for item in list2):
    print("All elements of list2 are in list1")
    # now in list1 i have to change the value is -1 but remember the list2 element are list2 one postion at 1 , 2 index only that change not the list1 last and second last element


