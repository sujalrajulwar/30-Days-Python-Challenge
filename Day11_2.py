# Given an array arr. Your task is to find the minimum and maximum elements
# in the array.

# Note: Return a Pair that contains two elements the
# first one will be a minimum element and
# the second will be a maximum.

# Examples:

# Input: arr[] = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.
# Input: arr[] = [1, 345, 234, 21, 56789]
# Output: 1 56789
# Explanation: minimum and maximum element of array are 1 and 56789.
# Input: arr[] = [56789]
# Output: 56789 56789
# Explanation: Since the array contains only one element so
# both min & max are same.
# Link : "https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/0"


arr = [3, 2, 1, 56, 10000, 167]

# Find minimum and maximum elements in the array
minimum = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]

print(minimum, maximum)
