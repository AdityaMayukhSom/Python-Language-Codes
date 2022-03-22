'''

This problem was first proposed by Edsger Dijkstra.

Given an array A of integers - 0,1 and 2 (3 Different Values).
Sort this array A in linear running time using constant memory.

Time Complexity = O(n)

'''

arr = list(map(int, input().split()))
print(arr)
low, mid, high = 0, 0, (len(arr) - 1)
while(mid <= high):
    num = arr[mid]
    if(num == 0):
        # swap arr[mid] and arr[low]
        temp = arr[mid]
        arr[mid] = arr[low]
        arr[low] = temp

        low = low + 1
        mid = mid + 1
        continue
    if(num == 1):
        # If the value is one, don't do anything, just chill and increament mid by 1
        mid = mid + 1
        continue
    if(num == 2):
        # Swap arr[mid] and arr[high]
        temp = arr[high]
        arr[high] = arr[mid]
        arr[mid] = temp

        high = high - 1
        continue

print(arr)
