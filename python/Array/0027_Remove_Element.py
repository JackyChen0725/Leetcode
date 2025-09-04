"""
Link: https://leetcode.com/problems/remove-element/

Solution1: Brute Force.
    Time complexity: O(n^2).
    Space complexity: O(1).

Solution2: Two Pointers.
    Time complexity: O(n).
    Space complexity: O(1).
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] != val:
                index += 1
            else:
                del nums[index]
        return len(nums)

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex