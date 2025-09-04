"""
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
"""

class Solution:
    def maxDifference(self, s: str) -> int:
        letterFreqDict = dict()
        maxOddFreq, minEvenFreq = 0, float('inf')
        for c in s:
            letterFreqDict[c] = letterFreqDict.get(c, 0) + 1
        
        for key, item in letterFreqDict.items():
            if item % 2 == 1:
                maxOddFreq = max(maxOddFreq, item)
            else:
                minEvenFreq = min(minEvenFreq, item)
        return maxOddFreq - minEvenFreq