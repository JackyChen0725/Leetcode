"""
Link: https://leetcode.com/problems/3sum/

Solution1: Two pointers after sorting.
    1. Sort the array.
    2. Iterate through the array, and for each element, use two pointers to find pairs that sum to the negative of the current element.
    3. Skip duplicates to ensure unique triplets.
    Time Complexity: O(n^2).
    Space Complexity: O(1) (ignoring the space for the output).

Solution2: Similar to Solution1 but uses a set to store results to avoid duplicates.
    Time Complexity: O(n^2).
    Space Complexity: O(n) (for the set).
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else: # sum == 0
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return res

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return [list(t) for t in res]
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else: # sum == 0
                    res.add((nums[i], nums[left], nums[right]))
                    
                    left += 1
                    right -= 1
        return [list(t) for t in res]

# print(Solution().threeSum([-1,0,1,2,-1,-4]))
# print(Solution().threeSum([0, 1, 1]))
# print(Solution().threeSum([-1, 0, 1, 2, -1, 1]))
print(Solution().threeSum([-2, -1, 0, 0, 1, 2, 3]))

