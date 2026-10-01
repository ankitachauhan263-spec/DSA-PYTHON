t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr[0]  != arr[1]:
        if arr[0] == arr[2]:
            print(2)
        else:
            print(1)
    else:
        for i in range(2, n):
            if arr[i] != arr[0]:
                print(i + 1)
                break
            