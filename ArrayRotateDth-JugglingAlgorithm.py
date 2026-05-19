
import math as m
arr = [1,2,3,4,5,6]
d = 2

def ArrayRotataion(arr, d):
    n = len(arr)
    d%=n
    cycle = m.gcd(n,d)

    for i in range(cycle):
        startVal = arr[i]
        currIdx = i
        
        while True:
            nextIdx = (currIdx+d)%n 
            if nextIdx == i:
                break
            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx
        
        arr[currIdx] = startVal
    
    return arr

print(ArrayRotataion(arr,d))
        


