start = [ 1 ,4 ,7 ,5 ,8]
end = [ 2 ,6 ,8 ,7 ,12]
z = list(zip(start , end))
print("Before Sorting: ",z)
z = sorted(z ,key = lambda x: x[1] )
print(z)
count = 0
start , end = 0 , 0
for s , e in z:
    if s >= end:
        count +=1
        end = e
print(count)




    

