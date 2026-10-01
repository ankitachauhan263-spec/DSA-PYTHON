t = int(input())

for _ in range(t):
    n = input()
    
    result = []
    
    length = len(n)
    for i in range(length):
        digit = int(n[i])
        
        if digit != 0:
            place = length - i -1
            value = digit * (10 ** place)
            result.append(value)
            
            print(len(result))
            print(*result)
    
    
    
    