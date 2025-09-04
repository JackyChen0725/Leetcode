"""
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Solution: Sliding Window.
    Time complexity: O(n).
    Space complexity: O(1).
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, sum = 0, 0
        minLength = float('inf')
        
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                minLength = min(minLength, j - i + 1)
                sum -= nums[i]
                i += 1
        
        return minLength if minLength != float('inf') else 0