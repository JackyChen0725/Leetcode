"""
Link: https://leetcode.com/problems/happy-number/

Solution: Use a set to track previously seen sums to detect cycles.
    Time Complexity: O(log n). The loop in getSum runs in O(log n) time since the number of digits in n is log n.
    Space Complexity: O(log n). Variables used in getSum are O(log n) as well.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n: int) -> int:
            sum = 0
            while n:
                n, r = divmod(n, 10)
                sum += r ** 2
            return sum

        sumSet = set()
        
        while True:
            n = getSum(n)

            if n == 1:
                return True
            
            if n == 4 or n in sumSet:
                return False
            else:
                sumSet.add(n)