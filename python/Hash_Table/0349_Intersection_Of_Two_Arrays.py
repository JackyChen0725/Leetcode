"""
Link: https://leetcode.com/problems/intersection-of-two-arrays/

Solution1: Use a set to store unique elements from the first array and check for their presence in the second array.
    Time Complexity: O(n + m) where n and m are the lengths of the two arrays.
    Space Complexity: O(min(n, m)).

Solution2: Use a fixed-size array (hash) to track presence of elements since the range is known (0 to 1000).
    Time Complexity: O(n + m) where n and m are the lengths of the two arrays.
    Space Complexity: O(min(n, m)).
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet1 = set(nums1)
        res = set()
        
        for num in nums2:
            if num in numSet1:
                res.add(num)
        
        return list(res)

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = [0] * 1001
        for num in nums1:
            hash[num] = 1
        
        res = set()
        for num in nums2:
            if hash[num] == 1:
                res.add(num)
        
        return list(res)

sol = Solution()
print(sol.intersection([1,2,2,1], [2, 2]))