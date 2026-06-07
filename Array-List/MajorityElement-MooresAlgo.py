arr = [1, 1, 2, 1, 3, 5, 1]

def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count+=1
        else:
            count-=1
    
    count = 0
    for num in arr:
        if num == candidate:
            count+=1
    
    if count > (len(arr)//2):
        return candidate
    else:
        return -1

element = majority_element(arr)
print(element)