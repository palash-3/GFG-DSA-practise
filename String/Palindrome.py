s = 'abccba'

def is_palindrone(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left+=1
        right-=1
    return True

palindrone = is_palindrone(s)
print(palindrone)