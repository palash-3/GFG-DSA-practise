arr = [16, 17, 4, 3, 5, 2]

def array_leader(arr):
    n = len(arr)
    temp_arr = []

    for i in range(n):
        flag = 0
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                flag+=1
                break
        if flag == 0:
            temp_arr.append(arr[i])
                
    return temp_arr


leader = array_leader(arr)
print(leader)