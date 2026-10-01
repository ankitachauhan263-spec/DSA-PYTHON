arr = [3, 5, 6, 7, 9, 10]

target = int(input("Enter target: "))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        found = True
        break

if found == False:
    print("Not Found")