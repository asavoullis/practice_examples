# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
# https://www.youtube.com/watch?v=q6IEA26hvXc

class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # O((m + n)log(m + n)) time complexity
        # # Time: O(NLogN) and Space: O(1) 
        list3 = nums1 + nums2 #nums1.extend(nums2)
        list3.sort()  #  list3 = sorted(nums1)

        n = len(list3)

        if n % 2 == 0:
            return (list3[n // 2] + list3[(n // 2) - 1]) / 2
        else:
            return list3[n // 2]
        # return (s[n // 2 -` 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None

        # a = sorted(nums1)
        # n = len(a)
        # m = n // 2
        # if n == 1:
        #     return a[0]
        # elif n % 2 == 0:
        #     return (a[m] + a[m - 1]) / 2
        # else:
        #     return a[m]

    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        # Time: O(log(min(m, n))) and Space: O(n)
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):    # for our solution we are assuming that B will be bigger than A, if it's not given than make it
            A, B = B, A

        l, r = 0, len(A) - 1   # we also assume that A is exactly half of B

        while True:            # when any return statement is executed it will stop
            i = (l + r) // 2   # A[mid]

            # B[mid] = total//2(divide by 2 will get us mid B ) - A[mid](if we sub A from total, B's left) -
            # 2(to make it align with starting index 0 of A & B, else it will go out of bounds)
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")  # if index i is in negative than assign -infinity to Aleft
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")  # if index i+1 is greater than the size of A assign infinity to Aright
            Bleft = B[j] if j >= 0 else float("-infinity")  # if index j is in negative than assign -infinity to Bleft
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")  # if index j+1 is greater than the size of B assign infinity to Bright

            # A = [1, 2, 3(left), 4(right), 5] and B = [1, 2, 3(left), 4(right), 5, 6, 7, 8]  # B = 6 - 2 - 2 = 2(i.e 0,1,2)
            if Aleft <= Bright and Bleft <= Aright:  # 3 <= 4 and 3 <= 4
                if total % 2:                                         # odd: min(4, 4)
                    return min(Aright, Bright) 
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # even: max(3, 3) + min(4, 4)  / 2
            elif Aleft > Bright:  # A = [1, 2, 3(left), 4(right), 5, 6] and B = [1, 2(left), 3(right), 4, 5]
                r = i - 1         # r = 3 - 1 = 2(i.e. index 0,1,2) --> A = [1, 2(L), 3(R), 4, 5, 6] and B = [1, 2, 3(L), 4(R), 5, 6]
            else:                 # when Bleft > Aright, we will increase l so L becomes R, and R pointer is shifted to R+1 index
                l = i + 1




nums1 = [1, 3, 4, 5, 6]
nums2 = [2, 4, 5, 6]

sol = Solution().findMedianSortedArrays2(nums1, nums2)
print(sol)