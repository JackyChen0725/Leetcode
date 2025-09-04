"""
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Solution: Two Pointers.
    Time complexity: O(n).
    Space complexity: O(n) if we count res.
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i, j, k = 0, length - 1, length - 1
        res = [0] * length
        
        while i <= j:
            val1 = nums[i] ** 2
            val2 = nums[j] ** 2
            if val1 < val2:
                res[k] = val2
                j -= 1
            else:
                res[k] = val1
                i += 1
            k -= 1
        return res