arr = [4, 3, 6, 2, 1, 1]

def missing_and_repeating(arr):
    n = len(arr)
    freq = [0]*(n+1)
    temp =[]

    for num in arr:
        freq[num] = freq[num]+1
    print(freq)
    
    for i in range(1,n+1):
        if freq[i] == 0 or freq[i] > 1:
            temp.append(i)
    return temp


numbers = missing_and_repeating(arr)
print(numbers)