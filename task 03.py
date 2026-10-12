# Binary search algorithm using  divide and conquer approach. 

arr = [6, 12, 17, 23, 38, 45, 77, 84, 90]

search = 45

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2  #4

    if arr[mid] == search:
        print("Successful!!")
        print("Element found at index:", mid)
        break

    elif arr[mid] < search:
        low = mid + 1 

    else:
        high = mid - 1

else:
    print("Element not found")