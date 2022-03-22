'''
Here Time Complexity = O(n)
Here Space Complexity = O(1)
'''

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Answer = 6

left = 0
right = len(arr) - 1

leftmax = arr[left]
rightmax = arr[right]

water = 0

while(left < right):
    if(arr[left] <= arr[right]):
        if(leftmax > arr[left]):
            water = water + (leftmax - arr[left])
        else:
            leftmax = arr[left]

        left = left + 1
    else:
        if(rightmax > arr[right]):
            water = water + (rightmax - arr[right])
        else:
            rightmax = arr[right]
        right = right - 1

print(water)
