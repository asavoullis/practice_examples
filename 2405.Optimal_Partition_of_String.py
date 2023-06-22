# 2405. Optimal Partition of String

# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
# That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.

# Example 1:
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

# Example 2:
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").

# Constraints:
# 1 <= s.length <= 105
# s consists of only English lowercase letters.



class Solution:
    def partitionString(self, s: str) -> int:

        # start from 1 because we are on the first partition (we count from 1) [ this is the count ]
        out = 1
        # create an empty strin
        sub = ""

        # loops over the characters in s
        for c in s:

            # if the character is in sub then increase the count and reset the substring to contain only that letter 
            # (only unique chras in substrings are allowed)
            if c in sub:
                out += 1
                sub = c
            else:
                # if not found then we add the next char
                sub += c
        return out


    def partitionString_slow(self, s: str) -> int:
        partition = 0
        counter = {}
        for letter in s:
            if counter.get(letter, 0) > 0:
                counter = {}
                partition += 1
                counter[letter] = 1
            else:
                counter[letter] = 1

        return partition+1


s1 = "abacaba"
s2 = "ssssss"
s3 = "hdklqkcssgxlvehva"

sol = Solution().partitionString(s1)
print(sol)

sol = Solution().partitionString(s2)
print(sol)

sol = Solution().partitionString(s3)
print(sol)