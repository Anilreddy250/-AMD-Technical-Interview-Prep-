# list = [1,2,4,5]
def sum(lst, target):
    n =len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i]+lst[j] ==target:
                return [i, j]
    return 1
lst = [1,2,4,5]
target = 6
print(sum(lst,target))
