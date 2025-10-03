"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Solution: Use two pointers to find the two numbers that add up to the target.
    Time Complexity: O(n).
    Space Complexity: O(1).
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

# print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([-1, 0], -1))
