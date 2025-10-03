"""
Link: https://leetcode.com/problems/4sum/

Solution: Similar to 3Sum with an additional loop. The key is pruning and skipping duplicates.
    1. Sort the array.
    2. Pruning and skipping duplicates for the first two numbers.
    3. Use two pointers to find pairs that sum to the target minus the first two numbers.
    Time Complexity: O(n^3).
    Space Complexity: O(1) (ignoring the space for the output).
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        for k in range(n - 3):
            if nums[k] > target and nums[k] > 0:
                break
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            for i in range(k + 1, n - 2):
                if nums[k] + nums[i] > target and nums[k] + nums[i] > 0:
                    break

                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                
                left, right = i + 1, n - 1
                while left < right:
                    sum = nums[k] + nums[i] + nums[left] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        res.append([nums[k], nums[i], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
        return res

# print(Solution().fourSum([1,0,-1,0,-2,2], 0))
print(Solution().fourSum([2,2,2,2,2], 8))
