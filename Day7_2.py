# Given an array arr[],
# swap the kth element from the beginning
# with the kth element from the end.

# Note: 1-based indexing is followed.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
# Output: [1, 2, 6, 4, 5, 3, 7, 8]
# Explanation: 3rd element from beginning is 3
# and 3rd element from end is 6, so we replace 3 & 6.
# Input: arr[] = [5, 3, 6, 1, 2], k = 2
# Output: [5, 1, 6, 3, 2]
# Explanation: 2nd element from beginning is 3
# and from end is 1.

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
li = []
for i in range(len(arr)):
    if i == k - 1:
        for j in arr:
            if j == arr[-k]:
                arr[k - 1], arr[-k] = arr[-k], arr[k - 1]
                break   
        break
print(arr)
