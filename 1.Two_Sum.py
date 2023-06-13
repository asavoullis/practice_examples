# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # In the worst case, the array will only have to be traversed once, resulting in an O(n) solution.
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in seen:
                # accessing values by key (returns index) and index of current number we are checking
                return [seen[diff], i]
            else:
                # stores in dictionary as key: value
                seen[nums[i]] = i

    def twoSum_v1(self, nums: list[int], target: int) -> list[int]:
        # O(n^2) time complexity because we traverse the array twice - uses nested loops to iterate over the list
        # The outer loop iterates from 0 to n-1, and for each iteration of the outer loop, the inner loop iterates from 0 to n-2.
        for i in range(len(nums)):
            # range after the first element of the array      
            for j in range(i+1, len(nums)):
            #If one of those pairs add together equal to the target return the answer else return None.
                if nums[i] + nums[j] == target:
                    return [i, j]
        return 'None'


nums = [2,3,4,5,7,11,15]
target = 9

sol = Solution().twoSum(nums, target)
print(sol)