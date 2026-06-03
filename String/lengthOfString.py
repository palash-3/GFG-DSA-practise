s = "San Francisco is the best city in the World!"

def length_of_string(s):
    count = 0
    for i in s:
        count+=1
    return count

length = length_of_string(s)
print(length)
