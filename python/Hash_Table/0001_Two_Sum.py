"""
Link: https://leetcode.com/problems/two-sum/

Solution: Use a hash map to store the indices of the numbers and check for complements.
    Time Complexity: O(n).
    Space Complexity: O(n).
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [hash[complement], i]
            hash[num] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))