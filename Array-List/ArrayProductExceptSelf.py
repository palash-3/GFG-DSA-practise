arr = [10, 3, 5, 6, 2]

def arr_product(arr):
    n = len(arr)
    array_prod = 1
    temp = []

    for i in range(n):
        array_prod *= arr[i]

    for i in range(n):
        val = int(array_prod//arr[i])
        temp.append(val)
    arr = temp
    return arr

product = arr_product(arr)
print(product)

