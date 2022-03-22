'''

KADANE'S ALGORITHM
Kadane's algorithm is used to find the maximum subarray sum in an array

Kadan's Algorithm is used to find the maximum subarray sum in a given array.
The logic behind the algorithm is that we carry formard the sum of a subarray, if the sum is positive
Though the subarray can contain negative numbers which decreases the overall sum, but the sum should be positive

Time complexity = O(n)

'''
arr = list(map(int, input().split()))

subArraySum = 0
maxArraySum = 0
negativeMaxSum = arr[0]
for i in range(len(arr)):
    # This one is used as an exception handling if there is only negative numbers in the array
    if(negativeMaxSum < arr[i]):
        negativeMaxSum = arr[i]

    # Basic Kadane's Algorithm starts from here
    # Adding individual elements to the subArraySum value
    subArraySum = subArraySum + arr[i]
    if(subArraySum < 0):
        # If the sum of continuous elements become negative, we change that negative value to 0 i.e. do not take that subarray for maximum sum
        subArraySum = 0
        continue
    if(subArraySum > maxArraySum):
        maxArraySum = subArraySum

# Print maxArraySum if maxArraySum is changed from 0 because maxArraySum can only become greater than zero, and not less that zero
if(maxArraySum != 0):
    print(maxArraySum)
else:
    # This is my modification to Kadane's algorithm
    # If the array contains no positive integer, then maxArraySum would not have been changed from 0, in that case, the largest number in the given array would be our answer
    print(negativeMaxSum)
