'''

Here Time Complexity = O(n)
Here Space Complexity = O(2n)

Test Case: 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Answer = 6



'''

arr = list(map(int, input().split()))

size = len(arr)
left_arr = list()
right_arr = list()

left = arr[0]
right = arr[size - 1]

water = 0

for i in range(size):
    if(left < arr[i]):
        left = arr[i]
    left_arr.append(left)
for i in reversed(range(size)):
    if(right < arr[i]):
        right = arr[i]
    right_arr.append(right)

# Reversing the order of right_arr so that indexing works properly, otherwise as we have traversed in reversed order, the indexing was reversed also.

for i in range(int(size / 2)):
    temp = right_arr[size - 1 - i]
    right_arr[size - 1 - i] = right_arr[i]
    right_arr[i] = temp

for i in range(size):
    water = water + min(left_arr[i], right_arr[i]) - arr[i]


print(water)
