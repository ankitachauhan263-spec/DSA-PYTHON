x = int(input())

steps =  x // 5

if x % 5 != 0:
    steps = steps + 1
    
    print(steps)