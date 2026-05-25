arr = [9,9,9]

def add_to_array(arr):
    number = 0

    for i in arr:
        number = number*10+i
    
    number+=1
    print(number)

    add_to_array(arr)

