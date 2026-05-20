#lst = [12,35,1,10,34,1,30,60,3]
lst = [10,10,10]

def SecondLargest(lst):
    largest = -1
    secondLargest = -1
    n = len(lst)

    for i in range(n):
        if lst[i] > largest:
            largest = lst[i]

    for i in range(n):
        if lst[i] > secondLargest:
            if lst[i] != largest:
                secondLargest = lst[i]
    
    return secondLargest

print(SecondLargest(lst))