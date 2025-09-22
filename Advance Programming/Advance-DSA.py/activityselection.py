# start = [ 1 ,4 ,7 ,5 ,8]
# end = [ 2 ,6 ,8 ,7 ,12]
# z = list(zip(start , end))
# print("Before Sorting: ",z)
# z = sorted(z ,key = lambda x: x[1] )
# print(z)
# count = 0
# start , end = 0 , 0
# for s , e in z:
#     if s >= end:
#         count +=1
#         end = e
# print(count)



# a = [10 , 20 , 30]
# goal = a[0]
# for i in range(1 , len(a)):
#     if a[i] > a:
#         goal = a[i]
# print("The Greater is " , )
    

a , b , c = 4 , 6 , 8
if a > b:
    if a > c:
        print("A is Greater" , a)
    else :
        print("c is Greater" , c)
else:
    if b > c:
       print("b is Greater" , b)
    else :
       print("c is Greater" , c)