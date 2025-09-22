list1 = [ 1 ,1, 0, 0, 0, 2, 2 ,1 ,2]
count1 = list1.count(1)
count2 = list1.count(2)
count0 = list1.count(1)
list2 = [0]*count0 + [1] * count1 + [2]*count2
print(list2)