"""
Link: https://leetcode.com/problems/4sum-ii/

Solution: Use a hash map to store sums of pairs from the first two lists and count complements from the last two lists.
    Time Complexity: O(n^2).
    Space Complexity: O(n^2).
"""

from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = dict()
        
        for n1 in nums1:
            for n2 in nums2:
                sum = n1 + n2
                hash[sum] = hash.get(sum, 0) + 1
        
        cnt = 0
        for n3 in nums3:
            for n4 in nums4:
                complement = -(n3 + n4)
                if complement in hash:
                    cnt += hash[complement]
        
        return cnt