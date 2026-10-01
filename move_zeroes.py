num = [0, 1, 0, 3, 13]

result = []

for num in nums:
    if num != 0:
        result.append(num)
    
    
zero_count = nums.count(0)

for i in range(zero_count):
    result.append(0)
    
    print(result)
    
        
        
