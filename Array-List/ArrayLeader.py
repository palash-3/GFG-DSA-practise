arr = [16, 17, 4, 3, 5, 2]

def array_leader(arr):
    n = len(arr)
    temp = []

    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                break
            else:
                temp.append(arr[i])
    return temp

leader = array_leader(arr)
print(leader)