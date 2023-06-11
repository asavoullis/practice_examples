# 744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.

class Solution:
    # To find the smallest character in the given array letters that is lexicographically greater than the target character target, we can use a binary search approach.
    # Since the array is sorted in non-decreasing order, we can apply binary search to efficiently find the desired character.
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            print("mid: ", mid)
            print(letters[mid])
            print("target", target)
            if letters[mid] > target:

                right = mid - 1
                print("right: ", right)
            else:
                left = mid + 1
                print("left: ", left)

            if left < len(letters):
                return letters[left]
            else:
                return letters[0]

    def nextGreatestLetter2(self, letters: list[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]

letters = ["a", "b", "c", "f", "j"]
target = "e"
sol = Solution().nextGreatestLetter(letters, target)
print(sol)