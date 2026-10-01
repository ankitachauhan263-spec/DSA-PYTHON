arr = list(map(int, input().split()))

target = int(input())

found = False 

for i in range (len(arr)):
    if arr[i] == target:
        found = True
        break 
    
    if found:
        print("Found")
    else:
        print("Not Found")
    
        