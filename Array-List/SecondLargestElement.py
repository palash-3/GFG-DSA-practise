lst = [10,10,10]

def second_largest(lst):
    lst.sort()
    n = len(lst)

    for i in range(n-2, -1, -1):
        if lst[i] != lst[i+1]:
            return lst[i]
        
    return -1

print(second_largest(lst))