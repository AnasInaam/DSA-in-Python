def subset(arr):
    r = [[]]
    for n in arr:
        new_subset = []
        for s in r:
            new_subset.append(s+ [n])
        r.extend(new_subset)
    return r
arr= [ 1 ,2 ,3]
print(subset(arr))
