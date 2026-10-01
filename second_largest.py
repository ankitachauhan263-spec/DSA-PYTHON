arr = [3, 5, 6, 7, 9, 10]

largest = arr[0]
Second_largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        Second_largest = largest 
        largest = arr[i]
    elif  arr[i] > Second_largest and arr[i] != largest:
        Second_largest = arr[i]
        
        print("largest:", largest)
        print("second Largest:",Second_largest)