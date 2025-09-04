"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Solution1: Brute Force.
    Time complexity: O(n^2).
    Space complexity: O(1).

Solution2: Two Pointers.
    Time complexity: O(n).
    Space complexity: O(1).
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        num = nums[index]
        index += 1
        while index < len(nums):
            while nums[index] == num:
                del nums[index]
                if index >= len(nums):
                    break
            else:
                num = nums[index]
                index += 1
        return index

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIndex = 1
        for fastIndex in range(1, len(nums)):
            if nums[fastIndex] != nums[slowIndex - 1]:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex