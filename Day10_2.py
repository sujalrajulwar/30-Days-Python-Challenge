# Given a string s consisting of lowercase English Letters.
# return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string,
# 'f' is the first character in the string which does not repeat.
# Input: s = "racecar"
# Output: 'e'
# Explanation: In the given string,
# 'e' is the only character in the string which does not repeat.
# Input: s = "aabbccc"
# Output: -1
# Explanation: All the characters in the given string are repeating.

s = "geeksforgeeks"
out = {}
for char in s:
    if char in out:
        out[char] = out[char] + 1
    else:
        out[char] = 1

for key, val in out.items():
    if val == 1:
        print(key)
        break
    else:
        continue
