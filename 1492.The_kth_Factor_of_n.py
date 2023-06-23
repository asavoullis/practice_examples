# 1492. The kth Factor of n
# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, 
# return the kth factor in this list or return -1 if n has less than k factors.

# Example 1:
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

# Example 2:
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.

# Example 3:
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
 
# Constraints:
# 1 <= k <= n <= 1000

# Follow up:
# Could you solve this problem in less than O(n) complexity?

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=0
        # check from 1 to number (as range goes until n-1)
        for l in range(1,n+1):
            # if l is a factor (divides n without decimals)
            if(n%l==0):
                i = i+1
                if(i==k):
                    return l
        return -1
    
    def kthFactor_v2(self, n: int, k: int) -> int:
        if k > n:
            return -1

        length = 0
        for i in range(1, n+1):
            if n % i == 0:
                length += 1
            if length == k:
                break

        solution = -1
        if length == k:
            solution = i

        return solution


n1 = 12
k1 = 3

n3 = 4
k3 = 4
sol = Solution().kthFactor(n1, k1)
print(sol)

sol = Solution().kthFactor(n3, k3)
print(sol)